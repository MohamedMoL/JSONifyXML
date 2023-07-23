from find_all_chars import find_all_chars
from tag import *


class validator:
    def __init__(self, xml_code : str) -> None:
        self.xml_code = xml_code
        self.info = {}

        # This will validate the ">" (gt) and "<" (lt)
        self.tag_open = find_all_chars(self.xml_code, "<")
        self.tag_close = find_all_chars(self.xml_code, ">")
        self.tags_index = [(lt, gt) for lt, gt in zip(self.tag_open, self.tag_close)]

        self.all_tags_and_content = self.separate_tags()

    def separate_tags(self) -> None:
        if not (len(self.tag_open) == len(self.tag_close)): # There should same number of "<" than ">"
            raise Exception("The syntax of the file is wrong")
        current_highest_index = -1 # ">" of last tag
        tags_and_content = []
        for lt, gt in self.tags_index: # "< ... >"
            if gt == lt + 1: # "<>"
                raise Exception("There is an empty tag")
            if lt > gt: # "> ... <"
                raise Exception("The syntax of the file is wrong")
            if lt < current_highest_index or gt < current_highest_index: # Last ">" can't be between a pair "<>"
                raise Exception("The syntax of the file is wrong")
            current_highest_index = gt
            tags_and_content.append(self.xml_code[lt : gt+1])
        return tags_and_content

    def validate_tag_structure(self, tag : str) -> list:
        inside_tag_information = tag[1:-1].split(" ") # Ignores ">" and "<", and separates name and attributes
        tag_name = ""
        tag_attrs = {}
        if inside_tag_information[0][0] == "!": # It is a commentary
            return [tag_name, tag_attrs]

        # Next lines will interpret tag's attributes and save them as key-value pairs
        for data in inside_tag_information:
            if "=" in data:
                key, value = data.split("=")
                tag_attrs[key] = value
            else:
                tag_name = data
        
        return [tag_name, tag_attrs]
