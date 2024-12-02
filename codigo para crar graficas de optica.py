# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 06:55:11 2024

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Definir la ruta base donde se guardan las tablas de soluciones
TXT_PATH = r'D:\Trabajo de Maestria\programas\tablas barrido de nergia foton incidente R1=30 R2=50 R3=80'
TXT1_PATH = r'D:\Trabajo de Maestria\programas\tablas barrido de nergia foton incidente R1=30 R2=50 R3=80\graficas de absorcion'
# Definir los rangos de los valores variables en los nombres de los archivos
B_values = [0, 15]
T_values = [0, 300]
P_values = [0, 10, 15]
x0_values = [0, 15, 55]
k3_Values=[0, 1]

# Función para leer y procesar el archivo CSV, seleccionando las primeras 7 columnas
def read_csv_file(filepath):
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath)
            if df.shape[1] >= 7:
                return df.iloc[:, :7]  # Selecciona las primeras 7 columnas
        except Exception as e:
            print(f"Error al procesar el archivo {filepath}: {e}")
            return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error
    else:
        print(f"No se pudo encontrar el archivo: {filepath}")
        return pd.DataFrame()

# Función para graficar las series y guardar las gráficas en un archivo
def plot_series(df, label, title, ylabel, linestyle='-', save_path=None):
    if not df.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        for i in range(1, 7):  # Graficar las columnas 2 a 7
            ax.plot(df.iloc[:, 0], df.iloc[:, i], linestyle=linestyle, label=f'{label} Columna {i+1}')
        ax.set_title(title)
        ax.set_xlabel('Eje X (Primera Columna)')
        ax.set_ylabel(ylabel)
        ax.legend()
        
        if save_path:
            plt.savefig(save_path)  # Guardar la gráfica en el archivo especificado
            print(f'Gráfico guardado en {save_path}')
        else:
            plt.show()

for B in B_values:
    for T in T_values:
        for P in P_values:
            for k3 in k3_Values:
                if k3 == 0:
                    x0_values = [0]
                else:
                    x0_values = [15, 40, 55]
                    
                for x0 in x0_values:
                    # Archivos de absorción lineal en X sin espín
                    filename_abs_x_no_spin = os.path.join(TXT_PATH, f"AbsorcionLinealX_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(NOSOI).csv")
                    df_abs_x_no_spin = read_csv_file(filename_abs_x_no_spin)
                    if not df_abs_x_no_spin.empty:
                        plot_series(
                            df_abs_x_no_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, sin impureza", 
                            'Absorción Lineal en X sin espín', 
                            'Absorción Lineal en X',
                            save_path=os.path.join(TXT1_PATH, f"AbsX_B{B}_T{T}_P{P}_x0{x0}_no_spin.png")
                        )

                    # Archivos de absorción lineal en X con espín
                    filename_abs_x_spin = os.path.join(TXT_PATH, f"AbsorcionLinealX_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(SOI).csv")
                    df_abs_x_spin = read_csv_file(filename_abs_x_spin)
                    if not df_abs_x_spin.empty:
                        plot_series(
                            df_abs_x_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, con impureza", 
                            'Absorción Lineal en X con espín', 
                            'Absorción Lineal en X',
                            save_path=os.path.join(TXT1_PATH, f"AbsX_B{B}_T{T}_P{P}_x0{x0}_spin.png")
                        )

                    # Archivos de absorción circular en Y sin espín
                    filename_abs_y_no_spin = os.path.join(TXT_PATH, f"AbsorcionCircularDerecha_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(NOSOI).csv")
                    df_abs_y_no_spin = read_csv_file(filename_abs_y_no_spin)
                    if not df_abs_y_no_spin.empty:
                        plot_series(
                            df_abs_y_no_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, sin impureza", 
                            'Absorción Circular derecha sin espín', 
                            'Absorción Circular en Y', 
                            linestyle='--',
                            save_path=os.path.join(TXT1_PATH, f"AbsY_B{B}_T{T}_P{P}_x0{x0}_no_spin.png")
                        )

                    # Archivos de absorción circular en Y con espín
                    filename_abs_y_spin = os.path.join(TXT_PATH, f"AbsorcionCircularDerecha_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(SOI).csv")
                    df_abs_y_spin = read_csv_file(filename_abs_y_spin)
                    if not df_abs_y_spin.empty:
                        plot_series(
                            df_abs_y_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, con impureza", 
                            'Absorción Circular derecha con espín', 
                            'Absorción Circular en Y', 
                            linestyle='--',
                            save_path=os.path.join(TXT1_PATH, f"AbsY_B{B}_T{T}_P{P}_x0{x0}_spin.png")
                        )

                    # Archivos de cambios en el índice de refracción sin espín
                    filename_delta_index_no_spin = os.path.join(TXT_PATH, f"DeltaIndiceRefraccion_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(NOSOI).csv")
                    df_delta_index_no_spin = read_csv_file(filename_delta_index_no_spin)
                    if not df_delta_index_no_spin.empty:
                        plot_series(
                            df_delta_index_no_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, sin impureza", 
                            'Cambios en el Índice de Refracción sin espín', 
                            'Índice de Refracción', 
                            linestyle='-.',
                            save_path=os.path.join(TXT1_PATH, f"DeltaIndex_B{B}_T{T}_P{P}_x0{x0}_no_spin.png")
                        )

                    # Archivos de cambios en el índice de refracción con espín
                    filename_delta_index_spin = os.path.join(TXT_PATH, f"DeltaIndiceRefraccion_B_{B}T_{T}impureza_{k3}P_{P}x0_{x0}(SOI).csv")
                    df_delta_index_spin = read_csv_file(filename_delta_index_spin)
                    if not df_delta_index_spin.empty:
                        plot_series(
                            df_delta_index_spin, 
                            f"B={B}, T={T}K, x0={x0} nm, con impureza", 
                            'Cambios en el Índice de Refracción con espín', 
                            'Índice de Refracción', 
                            linestyle='-.',
                            save_path=os.path.join(TXT1_PATH, f"DeltaIndex_B{B}_T{T}_P{P}_x0{x0}_spin.png")
                        )
