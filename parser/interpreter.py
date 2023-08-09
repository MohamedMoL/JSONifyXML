from .tag import *
from .validator import Validator
from lifo import LiFo
from typing import Dict


class Interpreter:

    # ---------------------- Public Methods ---------------------- #
    def parse_xml_to_python_object(self, tags_and_contents : list, validator : Validator) -> Dict[int, list]:
        tags_LiFo = LiFo()

        tags_hierarchy : Dict[int, list] = {} # This dict will contain all xml's information
        # Key: will be an integer which is the level of the tag
        # Value: will be an array of all tags in that level
    
        for element in tags_and_contents:
            current_tag : Tag
            if element[0] == "<": # It is tag
                current_tag_name, current_tag_attrs = validator.validate_tag(element)
                
                # This conditional will see if the tag starts with "!" or "?"
                if current_tag_name: 

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
        
        # ----------------------- WARNING ----------------------- #
        # This method modifies the item 'obj' (given as parameter)
        # It is a BAD practise. So far, there is no alternatives which does not sacrify the performance

        self.__move_data_between_tags(obj)

        json_str = "{"
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
    
    def __move_data_between_tags(self, obj : Dict[int, list[Tag]]) -> None:
        reversed_keys_obj = list(obj.keys())[::-1]
        reversed_keys_obj.remove(1) # level 1 is unnecesary to be iterated in the next loop
        
        for level in reversed_keys_obj:
            for tag in obj[level]:

                parent_attrs : Dict[str, list] = obj[level - 1][tag.parent_index].attributes
                current_tag_name = parent_attrs.get(tag.name, False)

                if tag.content and tag.attributes: # Tags with content and attributes
                    tag.attributes = {"_content" : tag.content}
                    
                if current_tag_name and (type(current_tag_name) == list): # Key: exists - Value: list (there is minimum two tags)
                    parent_attrs[tag.name].append(tag)
                
                elif current_tag_name and (type(current_tag_name) != list): # Key: exists - Value: Tag
                    parent_attrs[tag.name] = [parent_attrs[tag.name], tag]

                elif tag.content and (not tag.attributes) and (not current_tag_name): # Tags without children and attributes
                    parent_attrs.update({tag.name : tag.content})
                    
                elif not current_tag_name: # The key does not exist
                    parent_attrs[tag.name] = tag
                    