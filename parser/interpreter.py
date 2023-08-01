from tag import *
from validator import Validator
from lifo import LiFo


class Interpreter:

    def parse_xml_to_python_object(self, tags_and_contents : list, validator : Validator) -> dict:
        if tags_and_contents[0][1] == "?": # Ignore xml tag, at this moment it's useless
            del tags_and_contents[0]

        tags_LiFo = LiFo()

        tags_hierarchy = {} # This dict will contain all xml's information
        # Key: will be an integer which is the level of the tag
        # Value: will be an array of all tags in that level
    
        for element in tags_and_contents:
            current_tag : Tag
            if element[0] == "<": # It is tag
                current_tag_name, current_tag_attrs = validator.validate_tag(element)
                
                # If next conditional doesn't meet, it is a commentary (it's useless, so skip it)
                if current_tag_name:

                    if not current_tag_name[0] == "/": # Tag is opening
                        current_tag = Tag()
                        current_tag.name = current_tag_name
                        current_tag.attributes = current_tag_attrs
                        tags_LiFo.push(current_tag)

                        index_of_current_level = len(tags_LiFo.array) - 1

                        if not tags_hierarchy.get(index_of_current_level):
                            tags_hierarchy[index_of_current_level] = []

                        if index_of_current_level == 1:
                            tags_hierarchy[index_of_current_level].append(current_tag)
                        else:
                            tags_hierarchy[index_of_current_level].append(
                                [len(tags_hierarchy.get(index_of_current_level - 1, "")) - 1, current_tag]
                            )
                        
                    else: # Tag is closing
                        if current_tag_name[1::] != tags_LiFo.array[-1].name: # Search in other moment if this is OK
                            raise Exception("Different tag name when it's closing")
                        tags_LiFo.pop()

            else: # It is content
                current_tag.content = element
        
        return tags_hierarchy
    
    def parse_python_object_to_json(self, obj : dict) -> str:
        json_str = ""
        little_parsed_obj = obj
        reversed_keys_obj = list(obj.keys())[::-1]
        for level in reversed_keys_obj:
            if level != 1:
                for parent_index, tag in obj[level]:
                    if tag.content and not tag.attributes:
                        little_parsed_obj[level - 1][parent_index][1].attributes = {tag.name : tag.content}

        return little_parsed_obj