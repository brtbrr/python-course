from eazy_patex import table_generation, image_generation

data = [[1_1, 1_2, 1_3], [2_1, 2_2, 2_3], [3_1, 3_2, 3_3]]
image_path = "mem.png"

table = table_generation(data)
image = image_generation(image_path)
doc_start = "\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}"
doc_end = "\end{document}"

with open("hw_2/task2.tex", "w") as handle:
    handle.write("\n".join([doc_start, table, image, doc_end]))