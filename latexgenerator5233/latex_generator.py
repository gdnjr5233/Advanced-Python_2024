def generate_latex_table(data):
    rows = []
    for row in data:
        row_str = " & ".join(map(str, row)) + " \\\\"
        rows.append(row_str)
    table_str = "\n".join(rows)
    latex_code = "\\begin{tabular}{|c|c|c|c|c|}\n"
    latex_code += "\\hline\n"
    latex_code += table_str + "\n"
    latex_code += "\\hline\n"
    latex_code += "\\end{tabular}"
    return latex_code

def generate_latex_image(image_path):
    latex_code = "\\begin{figure}[h]\n"
    latex_code += "\\raggedright\n"
    latex_code += "\\includegraphics[scale=0.4]{" + image_path + "}\n"
    latex_code += "\\end{figure}"
    return latex_code