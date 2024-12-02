# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:58:25 2024

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:06:58 2024

@author: User
"""

#codigo para abosrcion
import numpy as np
import os
#import sympy as sp
import matplotlib.pyplot as plt
import math
import pandas as pd  # Importar pandas para guardar los datos en CSV

save_path = r"E:\Trabajo de Maestria\programas\nuevo porgrama de comsol\Graficas abs"

# Constantes
sigma_v = 3 * 10**22  # Densidad de portadores, en m^-3
q = 1.602 * 10**-19  # Carga del electrón, en C
e0 = 8.85 * 10**-12  # Constante de permitividad del vacío, en F/m
er = 12.58 * e0  # Permitividad relativa
hbar = 1.0546 * 10**-34  # Constante reducida de Planck, en J·s
gamma12 = (0.5 / 1000)* q   # Factor de amortiguamiento entre los estados, en J
miu0 = 2 * np.pi * 10**-7  # Permeabilidad magnética, en H/m

n = math.sqrt(3)  # Índice de refracción
Ir = 30 * 10**6  # Intensidad de radiación, en W/m^2
c = 3 * 10**8  # Velocidad de la luz, en m/s

#Vectores Condicion
B = [0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10]
P = [0, 0, 10, 10, 15, 15, 0, 0, 10, 10, 15, 15]
T = [0, 300, 0, 300, 0, 300, 0, 300, 0, 300, 0, 300]

def er_function(T, P):
    if T <= 200:
        return 12.74 * np.exp(-1.67e-2 * P) * np.exp(9.4e-5 * (T - 75.6))*e0
    else:
        return 13.18 * np.exp(-1.73e-2 * P) * np.exp(20.4e-5 * (T - 300))*e0
#declaramos los elementos de dipolo para cada transicion
#SOI_NOIMP
M12_SOI_NoImp = [1.97E-31, 8.26E-32, 3.67E-31, 1.53E-29, 9.81E-32, 4.40E-31, 7.42E-16, 7.49E-16, 7.35E-16, 7.42E-16, 7.33E-16, 7.39E-16]

M13_SOI_NoImp = [8.60E-17, 6.55E-17, 4.43E-17, 1.94E-16, 3.64E-16, 2.99E-16, 2.81E-17, 2.29E-17, 3.42E-17, 2.84E-17, 3.57E-17, 3.03E-17]

M14_SOI_NoImp = [3.11E-16, 3.34E-16, 3.58E-16, 2.04E-16, 3.71E-17, 1.00E-16, 1.83E-25, 1.60E-25, 2.04E-25, 1.78E-25, 1.74E-25, 1.64E-25]

M15_SOI_NoImp = [3.98E-16, 3.24E-18, 3.92E-16, 6.89E-17, 3.89E-20, 3.96E-16, 8.09E-28, 9.16E-28, 7.76E-28, 7.56E-28, 5.87E-28, 6.07E-28]

M16_SOI_NoImp = [1.95E-18, 3.97E-16, 7.88E-18, 3.35E-16, 4.00E-16, 4.55E-18, 8.56E-18, 8.81E-18, 7.88E-18, 8.44E-18, 6.92E-18, 7.90E-18]

#NOSOI_NOIMP
M12_NoSOI_NoImp = [4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 7.92E-16, 7.92E-16, 7.92E-16, 7.92E-16, 7.92E-16, 7.92E-16]

M13_NoSOI_NoImp = [4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 4.00E-16, 1.74E-27, 1.62E-27, 1.81E-27, 1.68E-27, 1.50E-27, 1.50E-27]

M14_NoSOI_NoImp = [5.24E-29, 4.96E-29, 5.34E-29, 5.08E-29, 4.52E-29, 4.59E-29, 9.69E-28, 9.74E-28, 9.53E-28, 9.56E-28, 8.86E-28, 9.09E-28]

#SOI_IMP
M12_SOI_Imp = [6.89E-17, 1.65E-16, 3.60E-18, 8.48E-17, 1.98E-17, 4.47E-16, 1.42E-22, 1.93E-22, 5.08E-23, 6.87E-23, 2.97E-23, 4.01E-23]

M13_SOI_Imp = [3.71E-18, 4.51E-18, 2.50E-20, 1.07E-19, 2.14E-18, 2.53E-18, 1.79E-18, 2.21E-18, 1.01E-18, 1.27E-18, 7.10E-19, 9.10E-19]

M14_SOI_Imp = [5.03E-19, 3.68E-19, 2.89E-18, 3.28E-18, 2.29E-19, 6.72E-19, 5.12E-21, 7.80E-21, 1.56E-21, 2.28E-21, 8.19E-22, 1.20E-21]

M15_SOI_Imp = [5.74E-20, 7.45E-20, 9.29E-22, 3.57E-21, 6.77E-21, 8.57E-21, 5.93E-20, 6.64E-20, 4.68E-20, 5.13E-20, 4.23E-20, 4.58E-20]

M16_SOI_Imp = [1.30E-20, 5.38E-21, 5.83E-20, 6.04E-20, 5.16E-20, 5.49E-20, 4.83E-20, 7.71E-20, 1.16E-20, 1.87E-20, 5.06E-21, 8.33E-21]

#NOSOI_IMP
M12_NoSOI_Imp = [4.25E-18, 4.92E-18, 2.95E-18, 3.43E-18, 2.41E-18, 2.81E-18, 1.81E-18, 2.23E-18, 1.03E-18, 1.29E-18, 7.21E-19, 9.23E-19]

M13_NoSOI_Imp = [7.10E-20, 7.91E-20, 5.98E-20, 6.45E-20, 5.89E-20, 6.15E-20, 5.96E-20, 6.69E-20, 4.69E-20, 5.14E-20, 4.23E-20, 4.58E-20]

M14_NoSOI_Imp = [4.78E-19, 1.44E-20, 2.91E-19, 3.49E-19, 2.38E-19, 2.77E-19, 1.35E-19, 1.66E-19, 7.65E-20, 9.59E-20, 5.32E-20, 6.87E-20]



#Declaramos las transiciones energeticas

E12_SOI_NoImp = [-3.63E-16, -3.85E-16, -5.36E-16, 1.11E-16, 8.14E-16, 4.96E-16, 1.07E-04, 1.14E-04, 9.96E-05, 1.06E-04, 9.30E-05, 1.00E-04]

E13_SOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 3.41E-04, 3.63E-04, 3.19E-04, 3.38E-04, 3.09E-04, 3.27E-04]

E14_SOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 6.75E-04, 7.14E-04, 6.33E-04, 6.69E-04, 6.06E-04, 6.42E-04]

E15_SOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 0.0010176, 0.001081, 9.53E-04, 0.0010103, 9.20E-04, 9.75E-04]

E16_SOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 0.0012673, 0.0012698, 0.0012639, 0.0012669, 0.0012612, 0.0012649]

#NOSOI_NOIMP
E12_NoSOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 1.32E-04, 1.37E-04, 1.26E-04, 1.31E-04, 1.19E-04, 1.25E-04]

E13_NoSOI_NoImp = [3.67E-04, 3.89E-04, 3.46E-04, 3.65E-04, 3.36E-04, 3.54E-04, 3.95E-04, 4.17E-04, 3.72E-04, 3.92E-04, 3.61E-04, 3.80E-04]

E14_NoSOI_NoImp = [0.001466, 0.0015537, 0.0013805, 0.0014572, 0.001342, 0.0014138, 8.31E-04, 8.71E-04, 7.88E-04, 8.24E-04, 7.56E-04, 7.94E-04]

#SOI_IMP
E12_SOI_Imp = [2.69E-15, -1.21E-16, -1.14E-15, 9.16E-16, -2.71E-15, -1.01E-15, 0.0012324, 0.0012324, 0.0012342, 0.0012341, 0.0012351, 0.001235]

E13_SOI_Imp = [0.026568, 0.024139, 0.035859, 0.032748, 0.041792, 0.038294, 0.026809, 0.024484, 0.035802, 0.032814, 0.041531, 0.038171]

E14_SOI_Imp = [0.026568, 0.024139, 0.035859, 0.032748, 0.041792, 0.038294, 0.027908, 0.025576, 0.036933, 0.033943, 0.042674, 0.039312]

E15_SOI_Imp = [0.02828, 0.025668, 0.038179, 0.034876, 0.044439, 0.040759, 0.029404, 0.026838, 0.039264, 0.036004, 0.045528, 0.04188]

E16_SOI_Imp = [0.02828, 0.025668, 0.038179, 0.034876, 0.044439, 0.040759, 0.030242, 0.027642, 0.040206, 0.036932, 0.046507, 0.04285]

#NOSOI_IMP
E12_NoSOI_Imp = [0.026439, 0.024032, 0.035641, 0.032566, 0.041508, 0.038055, 0.026638, 0.024337, 0.035546, 0.032594, 0.041211, 0.037896]

E13_NoSOI_Imp = [0.028154, 0.025563, 0.037967, 0.034699, 0.044164, 0.040526, 0.029128, 0.026579, 0.038929, 0.035702, 0.04514, 0.041534]

E14_NoSOI_Imp = [0.029522, 0.026771, 0.039932, 0.036443, 0.046561, 0.042653, 0.03058, 0.027862, 0.040997, 0.037558, 0.047604, 0.043761]


#definimos los calulos de absorcion
i=[1,2,3,4,5,6]
j=[1,2,3,4,5,6]


Mij_SOI_NoImp = [ M12_SOI_NoImp, M13_SOI_NoImp, M14_SOI_NoImp, M15_SOI_NoImp, M16_SOI_NoImp]
Mij_NoSOI_NoImp = [ M12_NoSOI_NoImp, M13_NoSOI_NoImp, M14_NoSOI_NoImp]
Mij_SOI_Imp = [ M12_SOI_Imp, M13_SOI_Imp, M14_SOI_Imp, M15_SOI_Imp, M16_SOI_Imp]
Mij_NoSOI_Imp = [  M12_NoSOI_Imp, M13_NoSOI_Imp, M14_NoSOI_Imp]

Eij_SOI_NoImp = [ E12_SOI_NoImp, E13_SOI_NoImp, E14_SOI_NoImp, E15_SOI_NoImp, E16_SOI_NoImp]
Eij_NoSOI_NoImp = [ E12_NoSOI_NoImp, E13_NoSOI_NoImp, E14_NoSOI_NoImp]
Eij_SOI_Imp = [ E12_SOI_Imp, E13_SOI_Imp, E14_SOI_Imp, E15_SOI_Imp, E16_SOI_Imp]
Eij_NoSOI_Imp = [  E12_NoSOI_Imp, E13_NoSOI_Imp, E14_NoSOI_Imp]

# Definir la función
def valores_por_posicion(indice):
    if 0 <= indice < len(B):  # Comprobar si el índice está en el rango válido
        return B[indice], P[indice], T[indice], M12_SOI_NoImp[indice], M13_SOI_NoImp[indice], M14_SOI_NoImp[indice], M15_SOI_NoImp[indice], M16_SOI_NoImp[indice], E12_SOI_NoImp[indice], E13_SOI_NoImp[indice], E14_SOI_NoImp[indice], E15_SOI_NoImp[indice], E16_SOI_NoImp[indice], M12_NoSOI_NoImp[indice], M13_NoSOI_NoImp[indice], M14_NoSOI_NoImp[indice], E12_NoSOI_NoImp[indice], E13_NoSOI_NoImp[indice], E14_NoSOI_NoImp[indice], M12_SOI_Imp[indice], M13_SOI_Imp[indice], M14_SOI_Imp[indice], M15_SOI_Imp[indice], M16_SOI_Imp[indice], E12_SOI_Imp[indice], E13_SOI_Imp[indice], E14_SOI_Imp[indice], E15_SOI_Imp[indice], E16_SOI_Imp[indice], M12_NoSOI_Imp[indice], M13_NoSOI_Imp[indice], M14_NoSOI_Imp[indice], E12_NoSOI_Imp[indice], E13_NoSOI_Imp[indice], E14_NoSOI_Imp[indice]
    else:
        return "Índice fuera de rango"

# Ejemplo de uso
indice_values= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for indice in indice_values:
    resultado = valores_por_posicion(indice)
    print(f"Para el índice {indice}, los valores son: B={resultado[0]}, P={resultado[1]}, T={resultado[2]}, M12_SOI_NoImp={resultado[3]}, M13_SOI_NoImp={resultado[4]}, M14_SOI_NoImp={resultado[5]}, M15_SOI_NoImp={resultado[6]}, M16_SOI_NoImp={resultado[7]}, E12_SOI_NoImp={resultado[8]}, E13_SOI_NoImp={resultado[9]}, E14_SOI_NoImp={resultado[10]}, E15_SOI_NoImp={resultado[11]}, E16_SOI_NoImp{resultado[12]}")

    
    T_value = T[indice]
    P_value = P[indice]

    def term1(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2)* ((sigma_v * (E12_SOI_NoImp[indice] * q - (ei * q /1000)) * M12_SOI_NoImp[indice]  * q**2) / (hbar * ((E12_SOI_NoImp[indice] * q - (ei * q/1000 ))**2 + gamma12**2)))
        
    def term2(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E13_SOI_NoImp[indice] * q - (ei * q /1000)) * M13_SOI_NoImp[indice]  * q**2) / (hbar * ((E13_SOI_NoImp[indice] * q - (ei * q /1000))**2 + gamma12**2)))

    def term3(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E14_SOI_NoImp[indice] * q - (ei * q /1000)) * M14_SOI_NoImp[indice]  * q**2) / (hbar * ((E14_SOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term4(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E15_SOI_NoImp[indice] * q - (ei * q /1000)) * M15_SOI_NoImp[indice]  * q**2) / (hbar * ((E15_SOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term5(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E16_SOI_NoImp[indice] * q - (ei * q /1000)) * M16_SOI_NoImp[indice]  * q**2) / (hbar * ((E16_SOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))
        
    def alpha1(ei):
        return term1(ei) + term2(ei) + term3(ei) + term4(ei) + term5(ei)
        
    # Crear una lista de valores de ei
    ei_values = np.arange(0, 50, 0.01)

    # Calcular valores de los terminos y alpha1
    term1_values = [term1(ei) for ei in ei_values]
    term2_values = [term2(ei) for ei in ei_values]
    term3_values = [term3(ei) for ei in ei_values]
    term4_values = [term4(ei) for ei in ei_values]
    term5_values = [term5(ei) for ei in ei_values]
    alpha1_values = [alpha1(ei) for ei in ei_values]
    
    # Crear DataFrame con los resultados para guardar como CSV
    data = {
       "Energía (meV)": ei_values,
       "Term1": term1_values,
       "Term2": term2_values,
       "Term3": term3_values,
       "Term4": term4_values,
       "Term5": term5_values,
        }

    df = pd.DataFrame(data)

   # Guardar la tabla de datos como CSV
    filename_csv = f"IndiceSOI_Sin_impureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.csv"
    full_path_csv = os.path.join(save_path, filename_csv)
    df.to_csv(full_path_csv, index=False)

    # Graficar term1, term2 y alpha1
    plt.figure(figsize=(10, 6))

    
    def term11(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E12_NoSOI_NoImp[indice] * q - (ei * q / 1000)) * M12_NoSOI_NoImp[indice]  * q**2) / (hbar * ((E12_NoSOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))
        
    def term22(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E13_NoSOI_NoImp[indice] * q - (ei * q / 1000)) * M13_NoSOI_NoImp[indice]  * q**2) / (hbar * ((E13_NoSOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term33(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E14_NoSOI_NoImp[indice] * q - (ei * q / 1000)) * M14_NoSOI_NoImp[indice]  * q**2) / (hbar * ((E14_NoSOI_NoImp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

  
    def alpha11(ei):
        return term11(ei) + term22(ei) + term33(ei) 
        

    # Calcular valores de los terminos y alpha1
    term11_values = [term11(ei) for ei in ei_values]
    term22_values = [term22(ei) for ei in ei_values]
    term33_values = [term33(ei) for ei in ei_values]
    
    data1 = {
       "Energía (meV)": ei_values,
       "Term1": term11_values,
       "Term2": term22_values,
       
    }

    df1 = pd.DataFrame(data1)

   # Guardar la tabla de datos como CSV
    filename_csv1 = f"IndiceNOSOI_Sin_impureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.csv"
    full_path_csv1 = os.path.join(save_path, filename_csv1)
    df1.to_csv(full_path_csv1, index=False)

    # Graficar term1, term2 y alpha1
    plt.figure(figsize=(10, 6))
    
    alpha11_values = [alpha11(ei) for ei in ei_values]
    
    

    # Graficar term1, term2 y alpha1
    plt.figure(figsize=(10, 4))

    # Graficar term1
    plt.plot(ei_values, term11_values, label='E12NoSOI', color='blue')
    # Graficar term2
    plt.plot(ei_values, term22_values, label='E13NoSOI', color='green')
    # Graficar term3
    plt.plot(ei_values, term33_values, label='E14NoSOI', color='cyan')
    
    # Graficar term1
    plt.plot(ei_values, term1_values, label='E12SOI', color='blue' , linestyle='--')
    # Graficar term2
    plt.plot(ei_values, term2_values, label='E13SOI', color='green', linestyle='--')
    # Graficar term3
    plt.plot(ei_values, term3_values, label='E14SOI', color='cyan', linestyle='--')
    # Graficar term4
    plt.plot(ei_values, term4_values, label='E15SOI', color='orange', linestyle='--')
    # Graficar term5
    plt.plot(ei_values, term5_values, label='E16SOI', color='purple', linestyle='--')
    
    for spine in plt.gca().spines.values():
        spine.set_linewidth(2)  # Cambia el valor para hacer los bordes más gruesos
    
    # Configurar gráfico
    plt.xlim(-1, 50)
    plt.ylim(0, 450000/10**5)
    plt.xlabel("Energía del fotón incidente (meV)", fontweight='bold')
    plt.ylabel("Delta Ind. ($10^{5}m^{-1}$) ", fontweight='bold')
    plt.title(f"Sin impureza, B={resultado[0]} T, P={resultado[1]} kbar, T={resultado[2]} K")
    # Poner los números de los ejes en negrita
    plt.xticks(fontweight='bold')
    plt.yticks(fontweight='bold')
    plt.legend()
    plt.grid(True)
    # Guardar la gráfica con un nombre que incluya los parámetros
    filename = f"IndiceSin_impureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.png"
    full_path = os.path.join(save_path, filename)
    plt.savefig(full_path, dpi=300)  # Guardar con una resolución de 300 dpi
     
    plt.show()
    
   

    def term111(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E12_SOI_Imp[indice] * q - (ei * q / 1000)) * M12_SOI_Imp[indice]  * q**2) / (hbar * ((E12_SOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))
        
    def term222(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E13_SOI_Imp[indice] * q - (ei * q / 1000)) * M13_SOI_Imp[indice]  * q**2) / (hbar * ((E13_SOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term333(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E14_SOI_Imp[indice] * q - (ei * q / 1000)) * M14_SOI_Imp[indice]  * q**2) / (hbar * ((E14_SOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term444(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E15_SOI_Imp[indice] * q - (ei * q / 1000)) * M15_SOI_Imp[indice]  * q**2) / (hbar * ((E15_SOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term555(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E16_SOI_Imp[indice] * q - (ei * q / 1000)) * M16_SOI_Imp[indice]  * q**2) / (hbar * ((E16_SOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))
        
    def alpha111(ei):
        return term111(ei) + term222(ei) + term333(ei) + term444(ei) + term555(ei)
        
    # Crear una lista de valores de ei
    

    # Calcular valores de los terminos y alpha1
    term111_values = [term111(ei) for ei in ei_values]
    term222_values = [term222(ei) for ei in ei_values]
    term333_values = [term333(ei) for ei in ei_values]
    term444_values = [term444(ei) for ei in ei_values]
    term555_values = [term555(ei) for ei in ei_values]
    alpha111_values = [alpha111(ei) for ei in ei_values]
    
    data2 = {
       "Energía (meV)": ei_values,
       "Term1": term111_values,
       "Term2": term222_values,
       "Term3": term333_values,
       "Term4": term444_values,
       "Term5": term555_values,
    }

    df2 = pd.DataFrame(data2)

   # Guardar la tabla de datos como CSV
    filename_csv2 = f"IndiceSOI_impureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.csv"
    full_path_csv2 = os.path.join(save_path, filename_csv2)
    df2.to_csv(full_path_csv2, index=False)

    # Graficar term1, term2 y alpha1
    plt.figure(figsize=(10, 6))


    
    def term1111(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E12_NoSOI_Imp[indice] * q - (ei * q / 1000)) * M12_NoSOI_Imp[indice]  * q**2) / (hbar * ((E12_NoSOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))
        
    def term2222(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E13_NoSOI_Imp[indice] * q - (ei * q / 1000)) * M13_NoSOI_Imp[indice]  * q**2) / (hbar * ((E13_NoSOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

    def term3333(ei):
        return (1/10**5)*(ei * q / 1000) * (2*np.pi)/(n**2) * ((sigma_v * (E14_NoSOI_Imp[indice] * q - (ei * q / 1000)) * M14_NoSOI_Imp[indice]  * q**2) / (hbar * ((E14_NoSOI_Imp[indice] * q - (ei * q / 1000))**2 + gamma12**2)))

  
    def alpha1111(ei):
        return term1111(ei) + term2222(ei) + term3333(ei) 
        
    # Crear una lista de valores de ei
    

    # Calcular valores de los terminos y alpha1
    term1111_values = [term1111(ei) for ei in ei_values]
    term2222_values = [term2222(ei) for ei in ei_values]
    term3333_values = [term3333(ei) for ei in ei_values]
    
    alpha1111_values = [alpha1111(ei) for ei in ei_values]
    
    data3 = {
       "Energía (meV)": ei_values,
       "Term1": term1111_values,
       "Term2": term2222_values,
       
    }

    df3 = pd.DataFrame(data3)

   # Guardar la tabla de datos como CSV
    filename_csv3 = f"IndiceNOSOI_impureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.csv"
    full_path_csv3 = os.path.join(save_path, filename_csv3)
    df3.to_csv(full_path_csv3, index=False)

    

    # Graficar term1, term2 y alpha1
    plt.figure(figsize=(10, 4))
    
    # Graficar term1
    plt.plot(ei_values, term1111_values, label='E12NoSOI', color='blue')
    # Graficar term2
    plt.plot(ei_values, term2222_values, label='E13NoSOI', color='green')
    # Graficar term3
    plt.plot(ei_values, term3333_values, label='E14NoSOI', color='cyan')
    
    
    # Graficar term1
    plt.plot(ei_values, term111_values, label='E12SOI', color='blue', linestyle='--')
    # Graficar term2
    plt.plot(ei_values, term222_values, label='E13SOI', color='green', linestyle='--')
    # Graficar term3
    plt.plot(ei_values, term333_values, label='E14SOI', color='cyan', linestyle='--')
    # Graficar term4
    plt.plot(ei_values, term444_values, label='E15SOI', color='orange', linestyle='--')
    # Graficar term5
    plt.plot(ei_values, term555_values, label='E16SOI', color='purple', linestyle='--')
    
    for spine in plt.gca().spines.values():
        spine.set_linewidth(2)  # Cambia el valor para hacer los bordes más gruesos
    
    plt.ylim(0, 450000/10**5)
    plt.xlim(-1, 50)
    # Configurar gráfico
    plt.xlabel("Energía del fotón incidente (meV)", fontweight='bold')
    plt.ylabel("Delta Ind. ($10^{5}m^{-1}$)", fontweight='bold')
    plt.title(f"Impureza en 40 nm, B={resultado[0]} T, P={resultado[1]} kbar, T={resultado[2]} K")
    # Poner los números de los ejes en negrita
    plt.xticks(fontweight='bold')
    plt.yticks(fontweight='bold')
    plt.legend()
    plt.grid(True)
    # Guardar la gráfica con un nombre que incluya los parámetros
    filename1 = f"Indiceimpureza_B_{resultado[0]}_P_{resultado[1]}_T_{resultado[2]}.png"
    full_path = os.path.join(save_path, filename1)
    plt.savefig(full_path, dpi=300)  # Guardar con una resolución de 300 dpi
    
    plt.show()
    