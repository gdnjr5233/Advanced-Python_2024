from latex_generator import generate_latex_document

table_data = [
    [1, 1, 2, 3, 5],
    [8, 13, 21, 34, 55],
    [89, 144, 233, 377, 610]
]

image_path = r"C:\Users\gdnjr5233_YOLO\Desktop\AP2024_hw2\artifacts\els.png"

latex_code = generate_latex_document(table_data, image_path)

with open("output.tex", "w") as f:
    f.write(latex_code)