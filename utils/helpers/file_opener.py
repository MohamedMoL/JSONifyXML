def open_xml_file(file_path : str) -> str:
    xml_code : list[str] = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            current_line = line.rstrip("\n").lstrip(" ")
            if current_line != "":
                xml_code.append(current_line)
    return "".join(xml_code)
