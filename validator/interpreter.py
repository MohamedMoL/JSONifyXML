from tag import *


class Interpreter:
    def __init__(self) -> None:
        ...
    
    def get_tags_hierarchy(self, tags_and_texts : list, separate_name_attrs) -> Tag:
        if tags_and_texts[0][1] == "?":
            del tags_and_texts[0]
        for element in tags_and_texts[:-1]:
            if element[0] == "<": # It is tag
                current_tag_name, current_tag_attrs = separate_name_attrs(element)
                
                # If next conditional doesn't meet, it is a commentary (it's useless, so skip it)
                if current_tag_name:

                    if not current_tag_name[0] == "/": # Tag is opening
                        current_tag = Tag()
                        current_tag.name = current_tag_name
                        current_tag.attributes = current_tag_attrs
                        tags_waiting_for_being_closed.append(current_tag)
                        
                    else: # Tag is closing
                        tags_waiting_for_being_closed[-2].children_tags = tags_waiting_for_being_closed[-1]
                        tags_waiting_for_being_closed.pop()
            else: # It is text
                tags_waiting_for_being_closed[-1].text = element

        # Verify last tag out of the loop
        root_tag_closing = separate_name_attrs(tags_and_texts[-1])
        if root_tag_closing[0][1:] == tags_waiting_for_being_closed[0].name:
            return tags_waiting_for_being_closed[0]
