class LiFo:

    def __init__(self) -> None:
        self.array = ["floor"] # 'Floor' is used as default value for the first value of the array. It is not important

    def pop(self) -> None:
        self.array.pop()
    
    def push(self, element) -> None:
        self.array.append(element)
