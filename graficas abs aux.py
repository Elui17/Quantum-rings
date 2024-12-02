import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Ruta donde se encuentran las tablas (archivos .csv)
data_path = r"E:\Trabajo de Maestria\programas\nuevo porgrama de comsol\Graficas abs"

# Listas de archivos .csv para cada gráfica (pares de tablas)
table_files = [
    ("NOSOI_impureza_B_0_P_10_T_0.csv", "NOSOI_Sin_impureza_B_0_P_10_T_0.csv"),
    ("SOI_impureza_B_0_P_10_T_0.csv", "SOI_Sin_impureza_B_0_P_10_T_0.csv"),
    ("NOSOI_impureza_B_0_P_10_T_300.csv", "NOSOI_impureza_B_0_P_10_T_300.csv"),
    ("SOI_impureza_B_0_P_10_T_300.csv", "SOI_Sin_impureza_B_0_P_10_T_300.csv")
]

# Leyendas personalizadas
custom_legend_names = [
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$, $E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"]
]

# Definir el tamaño de la figura (ancho total, alto total) en pulgadas
fig_width = 10  # Ancho total de la figura
fig_height = 4  # Alto total de la figura
spine_width = 2  # Ancho de los bordes de las gráficas

# Parámetros de la leyenda
legend_location = 'upper right'
legend_fontsize = 6
legend_title = ''
legend_framealpha = 0.9

# Función para crear una imagen con 4 subgráficas
def create_image(
    image_index, tables, legends,
    xlabel='Energía del fotón incidente (meV)',
    ylabel='Coef. Absor ($10^{5}m^{-1}$)',
    xlabel_pos=(0.5, -0.03), ylabel_pos=(0.08, 0.5),
    xlim=(0, 50), ylim=(0, 1.5), spine_width=1.5,
    x_step=10, y_step= 1, labels=["a)", "b)", "c)", "d)"]
):
    fig, axes = plt.subplots(2, 2, figsize=(fig_width, fig_height))

    # Iterar sobre los pares de tablas y los ejes para crear las subgráficas
    for (table_file1, table_file2), legend_names, ax, label in zip(tables, legends, axes.flat, labels):
        # Leer las dos tablas
        df1 = pd.read_csv(os.path.join(data_path, table_file1))
        df2 = pd.read_csv(os.path.join(data_path, table_file2))
        
        # Eje X para ambas tablas (siempre la primera columna)
        x1 = df1.iloc[:, 0]
        x2 = df2.iloc[:, 0]
        
        # Verificar el número de columnas en las tablas
        num_columns1 = len(df1.columns) - 1
        num_columns2 = len(df2.columns) - 1

        # Ajustar la lista de leyendas si es necesario
        legend_names = legend_names[:num_columns1 + num_columns2]
        if len(legend_names) < num_columns1 + num_columns2:
            additional_names = [f"Term {i+1}" for i in range(len(legend_names), num_columns1 + num_columns2)]
            legend_names.extend(additional_names)
        
        # Graficar cada columna Y de las tablas con nombres de leyendas personalizados
        for i, col in enumerate(df1.columns[1:num_columns1 + 1]):
            ax.plot(x1, df1[col], label=legend_names[i], linestyle='-', alpha=0.7)
        
        for i, col in enumerate(df2.columns[1:num_columns2 + 1], start=num_columns1):
            ax.plot(x2, df2[col], label=legend_names[i], linestyle='--', alpha=0.7)
        
        # Establecer los límites de los ejes x e y
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        
        # Configurar el grosor de los bordes
        for spine in ax.spines.values():
            spine.set_linewidth(spine_width)
        
        # Hacer que los números de los ejes estén en negrita
        ax.tick_params(axis='x', labelsize=10, width=spine_width)
        ax.tick_params(axis='y', labelsize=10, width=spine_width)
        
        # Configurar los ticks de los ejes X e Y para que tengan el paso deseado
        #ax.set_xticks(np.arange(xlim[0], xlim[1] + x_step, x_step))
        ax.set_yticks(np.arange(ylim[0], ylim[1] + y_step, y_step))
  
        
        if ax in axes[0, :]:
            ncol_value = 3 if ax in axes[:, 1] else 1  # 2 columnas de leyenda en la segunda columna
            ax.legend(
                title=legend_title,
                loc=legend_location,
                fontsize=legend_fontsize,
                title_fontsize=legend_fontsize + 2,
                framealpha=legend_framealpha,
                ncol=ncol_value
            )
        # Añadir la etiqueta a cada subgráfica (a), b), c), d))
        ax.text(0.05, 0.95, label, transform=ax.transAxes,
                fontsize=12, fontweight='bold', va='top', ha='left')
    # Eliminar etiquetas del eje Y en la segunda columna
    for ax in axes[:, 1]:
        ax.set_yticklabels([])

    # Eliminar etiquetas del eje X en la primera fila
    for ax in axes[0, :]:
        ax.set_xticklabels([])

     # Configurar el título global de los ejes X e Y con ajuste de `labelpad`
    fig.text(xlabel_pos[0], xlabel_pos[1], xlabel, ha='center', va='center', fontsize=12, fontweight='bold')
    fig.text(ylabel_pos[0], ylabel_pos[1], ylabel, ha='center', va='center', rotation='vertical', fontsize=12, fontweight='bold')
    # Ajustar el espacio entre las subgráficas
    plt.subplots_adjust(wspace=0.08, hspace=0.18)
    
    # Guardar la figura
    filename = f"imagen_{image_index}.png"
    full_path = os.path.join(data_path, filename)
    plt.savefig(full_path, dpi=300, bbox_inches='tight')
    
    # Mostrar la figura
    plt.show()

# Crear la primera imagen con los primeros 4 pares de tablas y las leyendas personalizadas
create_image("B_0_P_10", table_files, custom_legend_names, xlim=(-1, 50), ylim=(0, 5), x_step=10, y_step=1)

# Crear la segunda imagen con los siguientes 4 pares de tablas y las leyendas personalizadas
table_files_2 = [
    ("NOSOI_impureza_B_10_P_10_T_0.csv", "NOSOI_Sin_impureza_B_10_P_10_T_0.csv"),
    ("SOI_impureza_B_10_P_10_T_0.csv", "SOI_Sin_impureza_B_10_P_10_T_0.csv"),
    ("NOSOI_impureza_B_10_P_10_T_300.csv", "NOSOI_Sin_impureza_B_10_P_10_T_300.csv"),
    ("SOI_impureza_B_10_P_10_T_300.csv", "SOI_Sin_impureza_B_10_P_10_T_300.csv")
]

# Leyendas personalizadas para la segunda imagen
custom_legend_names_2 = [
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"]
]
create_image("B_10_P_10", table_files_2, custom_legend_names_2, xlim=(-1, 50), ylim=(0, 5), spine_width=2, x_step=10, y_step=1)

table_files_3 = [
    ("NOSOI_impureza_B_0_P_15_T_0.csv", "NOSOI_Sin_impureza_B_0_P_15_T_0.csv"),
    ("SOI_impureza_B_0_P_15_T_0.csv", "SOI_Sin_impureza_B_0_P_15_T_0.csv"),
    ("NOSOI_impureza_B_0_P_15_T_300.csv", "NOSOI_Sin_impureza_B_0_P_15_T_300.csv"),
    ("SOI_impureza_B_0_P_15_T_300.csv", "SOI_Sin_impureza_B_0_P_15_T_300.csv")
]

# Leyendas personalizadas para la segunda imagen
custom_legend_names_3 = [
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"]
]

create_image("B_0_P_15", table_files_3, custom_legend_names_3, xlim=(-1, 50), ylim=(0, 5), x_step=10, y_step=1)

table_files_4 = [
    ("NOSOI_impureza_B_10_P_15_T_0.csv", "NOSOI_Sin_impureza_B_10_P_15_T_0.csv"),
    ("SOI_impureza_B_10_P_15_T_0.csv", "SOI_Sin_impureza_B_10_P_15_T_0.csv"),
    ("NOSOI_impureza_B_10_P_15_T_300.csv", "NOSOI_Sin_impureza_B_10_P_15_T_300.csv"),
    ("SOI_impureza_B_10_P_15_T_300.csv", "SOI_Sin_impureza_B_10_P_15_T_300.csv")
]

# Leyendas personalizadas para la segunda imagen
custom_legend_names_4 = [
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{12}$", "$E_{13}$"],
    ["$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$", "$E_{12}$", "$E_{13}$", "$E_{14}$", "$E_{15}$", "$E_{16}$"]
]

create_image("B_10_P_15", table_files_4, custom_legend_names_4, xlim=(-1, 50), ylim=(0, 5), x_step=10, y_step=1)

 