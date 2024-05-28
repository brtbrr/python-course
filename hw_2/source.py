def table_generation(table):
    begin = "\\begin{center}\n\\begin{tabular}{ c c c }"
    end = "\end{tabular}\n\end{center}"
    content = " \\\\\n".join([" & ".join(map(str, line)) for line in table])

    return "\n".join([begin, content, end])

def image_generation(image):
    start = "\\begin{figure}[ht]\n\centering\n"
    content = f"\includegraphics[width=0.8\\textwidth]{{{image}}}"
    end = "\n\end{figure}"

    return start + content + end