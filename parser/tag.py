class Tag:
    def __init__(self) -> None:
        self._name : str
        self._attributes = {}
        self._content = ""
        self._parent_index : int

    def __str__(self) -> str:
        return self.name

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
    def parent_index(self):
        return self._parent_index
    
    # ---------------------- Setters ---------------------- #
    @name.setter
    def name(self, value : str):
        self._name = value
    
    @attributes.setter
    def attributes(self, attrs : dict):
        self._attributes.update(attrs)
    
    @content.setter
    def content(self, value : str):
        self._content += value

    @parent_index.setter
    def parent_index(self, value : int):
        self._parent_index = value
