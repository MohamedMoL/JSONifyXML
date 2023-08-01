class Tag:
    def __init__(self) -> None:
        self._name : str
        self._attributes = {}
        self._content = ""
        self._children_tags = []

    # Next lines will create a getter and a setter for each variable
    # ---------------------- Getters ---------------------- #

    @property
    def name(self):
        return self._name
    
    @property
    def attributes(self):
        return self._attributes
    
    @property
    def content(self):
        return self._content
    
    @property
    def children_tags(self):
        return self._children_tags
    
    # ---------------------- Setters ---------------------- #
    
    @name.setter
    def name(self, value : str):
        self._name = value
    
    @attributes.setter
    def attributes(self, attrs : dict):
        self._attributes.update(attrs)
    
    @content.setter
    def text(self, value : str):
        self._content += value
        
    @children_tags.setter
    def children_tags(self, value):
        self._children_tags.append(value)
