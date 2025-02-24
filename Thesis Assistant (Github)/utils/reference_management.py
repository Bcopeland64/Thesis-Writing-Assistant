# utils/reference_management.py
def generate_citation(title, author, year, style="apa"):
    if style == "apa":
        return f"{author} ({year}). {title}."
    elif style == "mla":
        return f"{author}. \"{title}\" {year}."
    elif style == "chicago":
        return f"{author}, \"{title}\", {year}."
    else:
        return "Unsupported citation style."