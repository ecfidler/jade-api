import glob
import os
from pathlib import Path

PATH = Path('.') / 'files'
FILETYPES = {'.stl', '.gcode'}
SUPPORTED_PRINTABLE_TYPES = {'.gcode'}


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


def rename_file(oldname: str, newname: str):
    path = Path(PATH) / oldname
    if not (path.exists() and path.is_file()):
        raise ValueError

    new_path = Path(PATH) / newname
    path.rename(new_path)
    return newname


def delete_file_from_name(filename: str):
    path = Path(PATH) / filename
    if not (path.exists() and path.is_file()):
        raise ValueError

    path.unlink()

    return True


def verify_file_is_printable(filename: str):
    path = Path(PATH) / filename
    if path.suffix in SUPPORTED_PRINTABLE_TYPES:
        return True

    return False
