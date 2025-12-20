import zlib

NAME = "CRC32"

def run(data: str) -> str:
    crc = zlib.crc32(data.encode()) & 0xFFFFFFFF
    return f"{crc:08x}"