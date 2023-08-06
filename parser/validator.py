from find_all_chars import find_all_chars
from tag import *
from typing import Iterator

class Validator:

    # ----------- Public methods ----------- #

    def validate_xml(self, xml_code: str) -> list[str]:
        # This will validate the ">" (gt) and "<" (lt)
        tag_open = find_all_chars(xml_code, "<")
        tag_close = find_all_chars(xml_code, ">")

        self.__check_lengths_of_open_and_close_chars(tag_open, tag_close)

        return self.__separate_tags(xml_code, zip(tag_open, tag_close))
    
    def validate_tag(self, tag : str) -> list:
        inside_tag_information = tag[1:-1].split(" ") # Ignores ">" and "<", and separates name and attributes
        tag_name = ""
        tag_attrs = {}
        if inside_tag_information[0][0] == "!": # It is a commentary
            return [tag_name, tag_attrs]

        # Next lines will interpret tag's attributes and save them as key-value pairs
        tag_name = inside_tag_information[0]
        
        for data in inside_tag_information[1:]:
            if "=" in data:
                key, value = data.split("=")
                tag_attrs[key] = value[1 : -1]
        
        return [tag_name, tag_attrs]

    # ----------- Private methods ----------- #

    def __separate_tags(self, xml_code: str, tags_index: Iterator[tuple[int, int]]) -> list[str]:
        last_gt_index = -1 # ">" of last tag
        tags_and_content : list[str] = []
        for lt, gt in tags_index: # "< ... >"
            self.__validate_order_of_open_close_chars(last_gt_index, lt, gt)
            if lt != last_gt_index + 1:
                tags_and_content.append(xml_code[last_gt_index + 1 : lt]) # Push tag's content
            last_gt_index = gt
            tags_and_content.append(xml_code[lt : gt+1]) # Push tag's inside information
        return tags_and_content
    
    def __check_lengths_of_open_and_close_chars(self, tag_open : list[int], tag_close : list[int]) -> None:
        if not (len(tag_open) == len(tag_close)): # There should same number of "<" than ">"
            raise Exception("The syntax of the file is wrong")
    
    def __validate_order_of_open_close_chars(self, last_gt_index : int, lt : int, gt : int) -> None:
        if gt == lt + 1: # "<>"
            raise Exception("There is an empty tag")
        if lt > gt: # "> ... <"
            raise Exception("The syntax of the file is wrong")
        if lt < last_gt_index or gt < last_gt_index: # Last ">" can't be between a pair "<>"
            raise Exception("The syntax of the file is wrong")
