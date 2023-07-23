# ------------------------------------------------------------------
# allows access to files in different folders
from sys import path
from os.path import abspath, getsize
CURRENT_PATH = abspath("")

PATH_HELPERS = f"{CURRENT_PATH}/helpers"
PATH_VALIDATOR = f"{CURRENT_PATH}/validator"
PATH_EXAMPLES = f"{CURRENT_PATH}/xml_examples"

path.append(PATH_HELPERS)
path.append(PATH_VALIDATOR)
# ------------------------------------------------------------------
from file_opener import open_xml_file
from validator import validator
from interpreter import Interpreter
from tag import *
from time import perf_counter


def main():
    time_start = perf_counter()

    file_path = PATH_EXAMPLES + "/example01.xml"

    code = open_xml_file(file_path)
    xml_validator = validator(code)
    interpreter = Interpreter()
    root_tag = interpreter.get_tags_hierarchy(
        xml_validator.all_tags_and_content,
          xml_validator.validate_tag_structure
    )

    time_end = perf_counter()

    file_size = [getsize(file_path), "Bytes"] # Byte
    file_size_KB = [file_size[0] * 0.001, "Kilobytes"] # Kilobyte
    # file_size_MB = [file_size[0] * 0.000_001, "Megabytes"] # Megabyte

    print(f"File size: {file_size_KB[0]} {file_size_KB[1]}")
    print(f"This lasts:\n{(time_end - time_start) * 1000} ms\n{time_end - time_start} s")


if __name__ == "__main__":
    main()
