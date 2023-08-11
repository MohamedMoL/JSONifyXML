from sys import path
from os.path import abspath

def get_example_route(xml_name : str) -> str:
    return f"{PATH_EXAMPLES}/{xml_name}"

CURRENT_PATH = abspath("")

PATH_EXAMPLES = f"{CURRENT_PATH}/assets/xml_examples"
PATH_PARSER = f"{CURRENT_PATH}/JSONifyXML/parser"
PATH_DEV_HELPERS = f"{CURRENT_PATH}/local_dev/helpers"
PATH_HELPERS = f"{CURRENT_PATH}/JSONifyXML/parser/helpers"

# Allows access to files in different folders
path.append(PATH_HELPERS)
path.append(PATH_PARSER)
path.append(PATH_DEV_HELPERS)
