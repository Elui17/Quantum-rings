from pathlib import Path
import pandas as pd
import mph
import numpy as np
import matplotlib.pyplot as plt
import math

# Definir constantes físicas
sigma_v = 3e22  # Densidad de portadores, en m^-3
q = 1.602e-19   # Carga elemental, en C
epsilon_0 = 8.85e-12  # Permisividad del vacío, en F/m
hbar = 1.0546e-34  # Constante de Planck reducida, en J·s
Gamma_12 = (0.5 / 1000) * q  # Ancho de línea de transición, en J
mu_0 = 4 * math.pi * 1e-7  # Permeabilidad magnética del vacío, en H/m
n = math.sqrt(3.2)  # Índice de refracción del material
Ir = 30e6  # Intensidad de radiación, en W/m^2
c = 3e8  # Velocidad de la luz en el vacío, en m/s

# Cargar el programa de COMSOL
MODEL_PATH = r'E:\Trabajo de Maestria\programas\nuevo porgrama de comsol\QR_SOI_P_T_NoSOI.mph'

# Definir las rutas donde se guardarán las tablas y las imágenes
TXT_PATH = r'E:\Trabajo de Maestria\programas\nuevo programa de comsol\Resultados'
IMG_PATH = r'E:\Trabajo de Maestria\programas\nuevo programa de comsol\Resultados\Graficas'

# Crear directorios si no existen
Path(TXT_PATH).mkdir(parents=True, exist_ok=True)
Path(IMG_PATH).mkdir(parents=True, exist_ok=True)

# Iniciar el cliente
try:
    client = mph.start()
    print("Cliente COMSOL conectado con éxito.")
except (RuntimeError, ValueError) as e:
    print(f"Ocurrió un error al conectar con COMSOL: {e}")
    exit()

# Cargar el modelo
model = client.load(MODEL_PATH)

# Definir los rangos de los parámetros para los barridos
T_values = [1, 300]  # Evitar T=0 K
P_values = [0, 10, 15]
S1_values = [0, 1]

# Crear listas para almacenar los resultados
delta_energy_results = []
sigmaplus_results = []
alpha_results = []

# Definir la función er(T, P) fuera del bucle
def er_function(T, P):
    if T <= 200:
        return 12.74 * np.exp(-1.67e-2 * P) * np.exp(9.4e-5 * (T - 75.6))
    else:
        return 13.18 * np.exp(-1.73e-2 * P) * np.exp(20.4e-5 * (T - 300))

# Definir la función alpha1 fuera del bucle
def alpha1(ei, Mij, Eij, T, P):
    # Convertir ei a Joules (ei en meV)
    ei_joules = (ei / 1000) * q  # meV a eV, luego a J

    # Calcular er para los valores actuales de T y P
    er_value = er_function(T, P)

    # Factor común
    common_factor = ei_joules * np.sqrt(mu_0 / (er_value * epsilon_0))

    # Inicializar alpha
    alpha = np.zeros_like(ei_joules)

    # Calcular alpha sumando sobre todos los Mij y Eij disponibles
    for mij, eij in zip(Mij, Eij):
        numerator = sigma_v * Gamma_12 * mij * q**2
        denominator = hbar * ((eij - ei_joules)**2 + Gamma_12**2)
        term = numerator / denominator
        alpha += common_factor * term

    return alpha

# Rango de valores para ei (en meV)
ei_values = np.arange(0, 5.01, 0.01)  # De 0 a 5 meV

# Realizar los barridos paramétricos
print()
for T in T_values:
    for P in P_values:
        for S1 in S1_values:
            print(f"Evaluando: T -> {T} | P -> {P} | S1 -> {S1}")

            try:
                # Establecer los parámetros en COMSOL para esta iteración
                model.parameter('T', T)
                model.parameter('P', P)
                model.parameter('S1', S1)

                # Resolver el modelo con manejo de errores
                try:
                    model.solve()
                except Exception as e:
                    print(f"Error al resolver el modelo en T={T}, P={P}, S1={S1}: {e}")
                    messages = model.message('get')
                    if messages:
                        print("Mensajes de COMSOL:")
                        for message in messages:
                            print(message)
                    continue  # Saltar a la siguiente iteración

                # Verificar si la solución existe
                if not model.solution():
                    print(f"No se obtuvo ninguna solución para T={T}, P={P}, S1={S1}")
                    continue  # Saltar a la siguiente iteración

                # Evaluar 'delta_energy' y 'sigmaplus'
                # Asegúrate de que 'dd' y 'sigmaplus' están definidos y disponibles
                try:
                    result_delta_energy = model.evaluate('dd')
                    result_sigmaplus = model.evaluate('sigmaplus')
                except Exception as e:
                    print(f"Error al evaluar variables en T={T}, P={P}, S1={S1}: {e}")
                    continue  # Saltar a la siguiente iteración

                # Asegurar que delta_energy y sigmaplus son arrays de numpy
                result_delta_energy = np.array(result_delta_energy, dtype=np.float64)
                result_sigmaplus = np.array(result_sigmaplus, dtype=np.float64)

                # Verificar que los resultados contienen al menos 4 valores
                if len(result_delta_energy) < 4 or len(result_sigmaplus) < 4:
                    print("Advertencia: Los resultados no contienen al menos 4 valores en esta iteración.")
                    continue  # Saltar a la siguiente iteración

                # Tomar solo los primeros 4 valores de los resultados
                first_4_delta_energy = result_delta_energy[:4]
                first_4_sigmaplus = result_sigmaplus[:4]

                # Calcular alpha para esta combinación de parámetros
                alpha = alpha1(ei_values, first_4_sigmaplus, first_4_delta_energy, T, P)

                # Almacenar los resultados
                alpha_data = {
                    'T': T,
                    'P': P,
                    'S1': S1,
                    'ei_values': ei_values,
                    'alpha_values': alpha
                }
                alpha_results.append(alpha_data)

                # Crear un DataFrame para los valores de alpha y ei
                df_alpha = pd.DataFrame({
                    'ei (meV)': ei_values,
                    'alpha(ei)': alpha
                })

                # Guardar los resultados en un archivo CSV
                filename_csv = f"alpha_T{T}_P{P}_S1{S1}.csv"
                df_alpha.to_csv(Path(TXT_PATH) / filename_csv, index=False)

                # Graficar alpha para esta iteración
                plt.figure(figsize=(8, 6))
                plt.plot(ei_values, alpha, label=f'Absorción T={T}, P={P}, S1={S1}')
                plt.xlabel(r'$ei$ (meV)')
                plt.ylabel(r'$\alpha(ei)$')
                plt.title('Absorción vs Energía Incidente')
                plt.legend()
                plt.grid(True)

                # Guardar el gráfico en un archivo
                filename_png = f"alpha_T{T}_P{P}_S1{S1}.png"
                plt.savefig(Path(IMG_PATH) / filename_png)
                plt.close()

                # Crear diccionarios con los valores de los parámetros y resultados para delta_energy y sigmaplus
                delta_energy_data = {
                    'T': T,
                    'P': P,
                    'S1': S1,
                    'delta_energy_1': first_4_delta_energy[0],
                    'delta_energy_2': first_4_delta_energy[1],
                    'delta_energy_3': first_4_delta_energy[2],
                    'delta_energy_4': first_4_delta_energy[3],
                }

                sigmaplus_data = {
                    'T': T,
                    'P': P,
                    'S1': S1,
                    'sigmaplus_1': first_4_sigmaplus[0],
                    'sigmaplus_2': first_4_sigmaplus[1],
                    'sigmaplus_3': first_4_sigmaplus[2],
                    'sigmaplus_4': first_4_sigmaplus[3],
                }

                # Añadir los datos a las listas de resultados
                delta_energy_results.append(delta_energy_data)
                sigmaplus_results.append(sigmaplus_data)

            except Exception as e:
                print(f"Ocurrió un error en la iteración T={T}, P={P}, S1={S1}: {e}")
                continue  # Saltar a la siguiente iteración

# Crear DataFrames a partir de las listas de resultados
df_delta_energy = pd.DataFrame(delta_energy_results)
df_sigmaplus = pd.DataFrame(sigmaplus_results)

# Mostrar las tablas en Python
print("\nTabla de Delta de Energía:")
print(df_delta_energy)

print("\nTabla de Elementos de Dipolo (sigmaplus):")
print(df_sigmaplus)

# Guardar los DataFrames en archivos CSV
delta_energy_file_path = Path(TXT_PATH) / 'DeltaEnergy.csv'
sigmaplus_file_path = Path(TXT_PATH) / 'Sigmaplus.csv'

df_delta_energy.to_csv(delta_energy_file_path, index=False)
df_sigmaplus.to_csv(sigmaplus_file_path, index=False)

# Cerrar el modelo y el cliente
client.remove(model)


