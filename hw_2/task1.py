from source import table_generation

data = [[1_1, 1_2, 1_3], [2_1, 2_2, 2_3], [3_1, 3_2, 3_3]]

table = table_generation(data)
doc_start = "\documentclass{article}\n\\begin{document}"
doc_end = "\end{document}"

with open("hw_2/task1.tex", "w") as handle:
    handle.write("\n".join([doc_start, table, doc_end]))