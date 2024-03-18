from latex_generator import generate_latex_table, generate_latex_image

data = [
    [1, 1, 2, 3, 5],
    [8, 13, 21, 34, 55],
    [89, 144, 233, 377, 610]
]

table_latex = generate_latex_table(data)
image_path = r"C:\Users\gdnjr5233_YOLO\Desktop\AP2024_hw2\latexgenerator5233\els.png"
image_latex = generate_latex_image(image_path)

# Создаем LaTeX файл
latex_code = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}} % Required for inserting images

\\title{{AP2024\_HW\_2.1}}
\\author{{Wang Quanyu}}
\\date{{March 2024}}

\\begin{{document}}

\\maketitle

\\section{{Generate table}}
{table_latex}

\\section{{Generate image}}
{image_latex}

\\end{{document}}
"""

with open("output.tex", "w") as f:
    f.write(latex_code)