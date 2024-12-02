# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:32:10 2024

@author: User
"""

import pandas as pd
import numpy as np
import json
import os

# Definir la ruta base donde se guardan las tablas de soluciones
TXT_PATH = r'C:\Users\User\Documents\Cursos Maestria en Fisica\investigacion 2\Programas J-D\Programas para trabajo\QR_PT\datos con barrido de presion y varias posiciones de la impureza\soluciones'
#ruta donde se gurdaran las nuevas tablas
TXT_SAVEF = r'D:\Trabajo de Maestria\programas\barridos de presion\tablas de estados fundamentales'
TXT_SAVE1 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 1 estado energetico'
TXT_SAVE2 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 2 estado energetico'
TXT_SAVE3 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 3 estado energetico'
TXT_SAVE4 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 4 estado energetico'
TXT_SAVE5 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 5 estado energetico'
TXT_SAVE6 = r'D:\Trabajo de Maestria\programas\barridos de presion\tabla de 6 estado energetico'
# Definir los rangos de los valores variables en los nombres de los archivos
B_values = [0, 15]
T_values = [0, 300]
x0_values = [0, 15, 50]
K3_values = [0,1]  # Ejemplo de impurezas

# Lista para almacenar cada DataFrame de datos
list_of_dataframes_NOIMP = []
list_of_dataframes_IMP = []

# Función para leer y procesar el archivo CSV
def read_csv_file(filepath):
    if os.path.exists(filepath):
        try:
            # Leer el archivo CSV directamente a un DataFrame
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"Error al procesar el archivo {filepath}: {e}")
    else:
        print(f"No se pudo encontrar el archivo: {filepath}")
    return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

# Leer los datos para archivos sin impureza
for B in B_values:
    for T in T_values:
        filename = os.path.join(TXT_PATH, f"B_{B}T_{T}posicion_0impureza_0.csv")
        df = read_csv_file(filename)
        if not df.empty:
            list_of_dataframes_NOIMP.append(df)

# Concatenar todas las columnas en un solo DataFrame, si hay alguna
if list_of_dataframes_NOIMP:
    combined_df_NOIMP = pd.concat(list_of_dataframes_NOIMP, axis=2)
    # Guardar el DataFrame combinado como CSV
    combined_df_NOIMP.to_csv(os.path.join(TXT_SAVEF, 'combined_NOIMP_estadofundamental(NOSOI).csv'), index=False)

# Leer los datos para archivos con impureza
for B in B_values:
    for T in T_values:
        for x0 in x0_values:
            filename = os.path.join(TXT_PATH, f"B_{B}T_{T}posicion_{x0}impureza_1.csv")
            df = read_csv_file(filename)
            if not df.empty:
                list_of_dataframes_IMP.append(df)

if list_of_dataframes_IMP:
    combined_df_IMP = pd.concat(list_of_dataframes_IMP, axis=2)
    # Guardar el DataFrame combinado como CSV
    combined_df_IMP.to_csv(os.path.join(TXT_SAVEF, 'combined_IMP_estadofundamental(NOSOI).csv'), index=False)
