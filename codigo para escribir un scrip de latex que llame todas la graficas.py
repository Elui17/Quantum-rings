# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 07:05:41 2024

@author: User
"""

# Definir los valores
B_values = [0, 15]
T_values = [0, 300]
P_values = [0, 10, 15]
k3_values = [0, 1]

# Nombre del archivo LaTeX de salida
output_tex_path = r'C:\Users\User\Desktop\graficos_latex.tex'


# Abrir el archivo LaTeX para escritura
with open(output_tex_path, 'w') as tex_file:
    for B in B_values:
        for T in T_values:
            for P in P_values:
                for k3 in k3_values:
                    if k3 == 0:
                        x0_values = [0]  # Lista con un solo valor cuando k3 es 0
                    else:
                        x0_values = [15, 40, 55]  # Lista con varios valores cuando k3 es 1

                    for x0 in x0_values:
                        # Generar los nombres de archivo
                        no_spin_abs_x = f"AbsX_B{B}_T{T}_P{P}_x0{x0}_no_spin"
                        spin_abs_x = f"AbsX_B{B}_T{T}_P{P}_x0{x0}_spin"
                        no_spin_abs_y = f"AbsY_B{B}_T{T}_P{P}_x0{x0}_no_spin"
                        spin_abs_y = f"AbsY_B{B}_T{T}_P{P}_x0{x0}_spin"
                        no_spin_delta_index = f"DeltaIndex_B{B}_T{T}_P{P}_x0{x0}_no_spin"
                        spin_delta_index = f"DeltaIndex_B{B}_T{T}_P{P}_x0{x0}_spin"

                        # Generar el código LaTeX
                        tex_code = f"""
\\begin{{frame}}
    \\begin{{figure}}
        \\centering
        % Fila 1: Absorción Lineal en X
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{no_spin_abs_x}.png}}
            %\\caption{{{no_spin_abs_x}}}
        \\end{{subfigure}}
        \\hfill
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{spin_abs_x}.png}}
            %\\caption{{{spin_abs_x}}}
        \\end{{subfigure}}
        \\\\
        % Fila 2: Absorción Circular en Y
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{no_spin_abs_y}.png}}
            %\\caption{{{no_spin_abs_y}}}
        \\end{{subfigure}}
        \\hfill
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{spin_abs_y}.png}}
            %\\caption{{{spin_abs_y}}}
        \\end{{subfigure}}
        \\\\
        % Fila 3: Cambios en el Índice de Refracción
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{no_spin_delta_index}.png}}
            %\\caption{{{no_spin_delta_index}}}
        \\end{{subfigure}}
        \\hfill
        \\begin{{subfigure}}{{0.45\\textwidth}}
            \\includegraphics[width=\\linewidth]{{{spin_delta_index}.png}}
            %\\caption{{{spin_delta_index}}}
        \\end{{subfigure}}
    \\end{{figure}}
\\end{{frame}}
"""
                        # Escribir el código LaTeX en el archivo
                        tex_file.write(tex_code)

print(f"El archivo LaTeX se ha generado y guardado en: {output_tex_path}")

