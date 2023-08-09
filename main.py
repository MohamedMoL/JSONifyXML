import paths
from get_file_size import get_size
from file_opener import open_xml_file
from tag import *
from xml_parse_to_json import xml_parse_to_json
from create_json import create_json
from time import perf_counter # Test performance purpose


def main():
    time_start = perf_counter() # Starts time measurement

    # --------------------- File working --------------------- #
    file_name = "example01_large"
    file_path = paths.get_example_route(f"{file_name}.xml")
    xml = open_xml_file(file_path)

    json_string = xml_parse_to_json(xml)

    create_json(json_string, file_name)

    time_end = perf_counter() # Ends time measurement
    
    # --------------------- Prints file size + time spend --------------------- #
    file_size = get_size(file_path)
    print(f"File size: {file_size[0]:.3f} {file_size[1]}")

    time = time_end - time_start
    print(f"This lasts:\n{(time * 1000):.5f} ms\n{time:.5f} s")


if __name__ == "__main__":
    main()
