# This code ONLY expects django's uploaded files
def format_lines(lines : str) -> str:
    separated_lines : list[str] = lines.split("\r\n")
    formated_lines : list[str] = [line.lstrip(" ") for line in separated_lines]
    return ''.join(formated_lines)
