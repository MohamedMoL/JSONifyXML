def find_all_chars(text : str, char : str) -> list[int]:
    return [i for i, ltr in enumerate(text) if ltr == char]
