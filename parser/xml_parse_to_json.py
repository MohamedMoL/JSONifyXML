from .validator import Validator
from .interpreter import Interpreter


def xml_parse_to_json(xml : str) -> str:
    # --------------------- Validator working --------------------- #
    validator = Validator()
    xml_tags_and_contents = validator.validate_xml(xml)

    # --------------------- Interpreter working --------------------- #
    interpreter = Interpreter()
    root_tag = interpreter.parse_xml_to_python_object(xml_tags_and_contents, validator)
    json = interpreter.parse_python_object_to_json(root_tag)

    return json
