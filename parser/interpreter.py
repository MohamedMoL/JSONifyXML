from tag import *
from validator import Validator
from lifo import LiFo
from typing import Dict
from copy import deepcopy


class Interpreter:

    # ---------------------- Public Methods ---------------------- #
    def parse_xml_to_python_object(self, tags_and_contents : list, validator : Validator) -> Dict[int, list]:
        if tags_and_contents[0][1] == "?": # Ignore xml tag, at this moment it's useless
            del tags_and_contents[0]

        tags_LiFo = LiFo()

        tags_hierarchy : Dict[int, list] = {} # This dict will contain all xml's information
        # Key: will be an integer which is the level of the tag
        # Value: will be an array of all tags in that level
    
        for element in tags_and_contents:
            current_tag : Tag
            if element[0] == "<": # It is tag
                current_tag_name, current_tag_attrs = validator.validate_tag(element)
                
                if current_tag_name: # If this doesn't meet, it is a commentary (should skip)

                    if not current_tag_name[0] == "/": # Tag is opening
                        
                        current_level = len(tags_LiFo.array)

                        current_tag = self.__update_tag(
                            tags_hierarchy, current_tag_name, 
                            current_tag_attrs, current_level
                        )

                        tags_LiFo.push(current_tag)
                        
                        if not tags_hierarchy.get(current_level):
                            tags_hierarchy[current_level] = []

                        tags_hierarchy[current_level].append(current_tag)
                        
                    else: # Tag is closing
                        if current_tag_name[1::] != tags_LiFo.array[-1].name:
                            raise Exception("Different tag name when it's closing")
                        tags_LiFo.pop()

            else: # It is content
                current_tag.content = element
        
        return tags_hierarchy
    
    def parse_python_object_to_json(self, obj : Dict[int, list[Tag]]) -> str:
        json_str = "{"
        reversed_keys_obj = list(obj.keys())[::-1]
        for level in reversed_keys_obj:
            if level > 1: # Parent tag. Level 1 is different from others
                for tag in obj[level]:
                    
                    parent_attrs : Dict[str, list] = obj[level - 1][tag.parent_index].attributes
                    current_tag_name = parent_attrs.get(tag.name, False)
                    
                    if current_tag_name and (type(current_tag_name) != list): # The key exists, but there is only one tag
                        parent_attrs[tag.name] = [parent_attrs[tag.name]]
                    
                    if current_tag_name: # The key exists and the value is a list (there is minimum two tags)
                        parent_attrs[tag.name].append(tag)

                    if tag.content and (not tag.attributes) and (not current_tag_name): # Tags without children and attributes
                        parent_attrs.update({tag.name : tag.content})
                    
                    elif not current_tag_name: # The key does not exist
                        parent_attrs[tag.name] = tag

        for tags in obj[1]:
            json_str += f'"{tags.name}"' + ":{"
            for key, value in tags.attributes.items():

                json_str += f'"{key}":'

                if type(value) == list:
                    json_str += self.__parse_list_of_tags_to_json(value)

                elif type(value) == Tag:
                    json_str += self.__parse_tag_to_json(value)

                else:
                    json_str += f'"{value}"'

                json_str += ","

            json_str = json_str[:-1]
            json_str += "}}"
        
        return json_str
    
    # ---------------------- Private Methods ---------------------- #
    def __update_tag(self, hierarchy : dict, name : str, attrs : dict, level : int) -> Tag:
        # All params are related with tags
        current_tag = Tag()
        current_tag.name = name
        current_tag.attributes = attrs
        current_tag.parent_index = len(hierarchy.get(level - 1, "")) - 1
        return current_tag
    
    def __parse_list_of_tags_to_json(self, list_of_tags : list[Tag]) -> str:
        slice_of_json = "["
        for tag in list_of_tags:  

            slice_of_json += self.__parse_tag_to_json(tag)
            slice_of_json += ","

        slice_of_json = slice_of_json[:-1]
        slice_of_json += "]"
        return slice_of_json
    
    def __parse_tag_to_json(self, tag : Tag) -> str:
        slice_of_json = "{"
        for key, value in tag.attributes.items():
            slice_of_json += f'"{key}":'
            if type(value) == list:
                slice_of_json += self.__parse_list_of_tags_to_json(value)
            else:
                slice_of_json += f'"{value}"'
            slice_of_json += ","
        slice_of_json = slice_of_json[:-1]
        slice_of_json += "}"
        return slice_of_json
            