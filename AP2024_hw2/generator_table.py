from latex_generator import generate_latex_table

data = [
    [1, 1, 2, 3, 5],
    [8, 13, 21, 34, 55],
    [89, 144, 233, 377, 610]
]

latex_table = generate_latex_table(data)

with open('generate_table.tex', 'w') as file:
    file.write(latex_table)