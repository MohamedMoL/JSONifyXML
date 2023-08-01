import paths
from os.path import getsize
from file_opener import open_xml_file
from validator import Validator
from interpreter import Interpreter
from tag import *
from time import perf_counter # Test performance purpose


def main():
    time_start = perf_counter() # Starts time measurement

    # --------------------- File working --------------------- #
    file_path = paths.get_example_route("example01.xml")
    xml = open_xml_file(file_path)

    # --------------------- Validator working --------------------- #
    validator = Validator()
    xml_tags_and_contents = validator.validate_xml(xml)

    # --------------------- Interpreter working --------------------- #
    interpreter = Interpreter()
    root_tag = interpreter.parse_xml_to_python_object(xml_tags_and_contents, validator)
    litle_parsed_obj = interpreter.parse_python_object_to_json(root_tag)

    time_end = perf_counter() # Ends time measurement

    # --------------------- Prints file size + time spend --------------------- #
    # file_size = [getsize(file_path), "Bytes"] # Byte
    # file_size_KB = [file_size[0] * 0.001, "Kilobytes"] # Kilobyte
    # file_size_MB = [file_size[0] * 0.000_001, "Megabytes"] # Megabyte
    # print(f"File size: {file_size_KB[0]} {file_size_KB[1]}")
    print(f"This lasts:\n{(time_end - time_start) * 1000} ms\n{time_end - time_start} s")


if __name__ == "__main__":
    main()
