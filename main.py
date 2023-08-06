import paths
from get_file_size import get_size
from file_opener import open_xml_file
from validator import Validator
from interpreter import Interpreter
from tag import *
from time import perf_counter # Test performance purpose


def main():
    time_start = perf_counter() # Starts time measurement

    # --------------------- File working --------------------- #
    file_name = "example01_large"
    file_path = paths.get_example_route(f"{file_name}.xml")
    xml = open_xml_file(file_path)

    # --------------------- Validator working --------------------- #
    validator = Validator()
    xml_tags_and_contents = validator.validate_xml(xml)

    # --------------------- Interpreter working --------------------- #
    interpreter = Interpreter()
    root_tag = interpreter.parse_xml_to_python_object(xml_tags_and_contents, validator)
    json = interpreter.parse_python_object_to_json(root_tag)

    # --------------------- JSON --------------------- #
    with open(f"{file_name}.json", "w") as file:
        file.write(json)

    time_end = perf_counter() # Ends time measurement
    
    # --------------------- Prints file size + time spend --------------------- #
    file_size = get_size(file_path)
    print(f"File size: {file_size[0]:.3f} {file_size[1]}")

    time = time_end - time_start
    print(f"This lasts:\n{(time * 1000):.5f} ms\n{time:.5f} s")


if __name__ == "__main__":
    main()
