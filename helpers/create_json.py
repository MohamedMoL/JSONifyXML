def create_json(json_string : str, file_name : str) -> None:
    with open(f"{file_name}.json", "w") as file:
        file.write(json_string)
        