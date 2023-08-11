from os.path import getsize


def get_size(file_path : str) -> tuple[float, str]:
    file_size_B = getsize(file_path)
    # -------- Gigabytes -------- #
    if file_size_B > 1_000_000_000:
        return (file_size_B * 0.000_000_001, "Gigabytes")
    # -------- Megabytes -------- #
    if file_size_B > 1_000_000:
        return (file_size_B * 0.000_001, "Megabytes")
    # -------- Kilobytes -------- #
    if file_size_B > 1_000:
        return (file_size_B * 0.001, "Kilobytes")
    # -------- Bytes -------- #
    return (file_size_B, "Bytes")
