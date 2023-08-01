class LiFo:

    default_value = "floor"

    def __init__(self) -> None:
        self.array = [self.default_value]

    def pop(self) -> None:
        self.array.pop()
    
    def push(self, element) -> None:
        self.array.append(element)
