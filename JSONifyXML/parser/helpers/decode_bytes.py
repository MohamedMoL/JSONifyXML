# This code ONLY expects django's uploaded files
def decode_bytes(data_byte) -> str:
    list_raw_data : list[str] = [chunk.decode('utf-8') for chunk in data_byte.chunks()]
    raw_data = ''.join(list_raw_data)
    return raw_data
