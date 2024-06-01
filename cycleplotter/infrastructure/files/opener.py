import zipfile
from io import StringIO
from typing import IO


def open_file(path: str, zip_entry_path: str) -> IO[str]:
    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as zip_ref:
            return StringIO(zip_ref.open(zip_entry_path, "r").read().decode("utf-8"))
    return open(path, "r")
