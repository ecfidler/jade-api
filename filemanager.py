import glob
import os
from pathlib import Path

PATH = Path('.') / 'files'
FILETYPES = {'.stl', '.gcode'}


def get_files_of_types(path: Path, types: set):
    return list(p.resolve() for p in path.glob("**/*") if p.suffix in types)


def get_file_listing():
    files = get_files_of_types(PATH, FILETYPES)
    return [{"name": file.name, "type": file.suffix} for file in files]


def read_file_from_filename(filename: str):
    filepath = PATH / filename
    if not filepath.is_file():
        raise FileNotFoundError()
    with open(filepath, 'rb') as f:
        data = f.read()
    return data, filepath.suffix


def save_file(name: str, file: bytes):
    filepath = PATH / name
    if not file or filepath.suffix not in FILETYPES:
        raise ValueError
    size = filepath.write_bytes(file)
    return {'file': filepath, 'bytes': size}
