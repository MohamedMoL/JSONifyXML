def open_xml_file(file_path : str) -> str:
    xml_code : str
    with open(file_path, "r") as file:
        xml_code = [line.rstrip("\n").lstrip(" ") for line in file.readlines()]
        xml_code = "".join(xml_code)
    return xml_code
