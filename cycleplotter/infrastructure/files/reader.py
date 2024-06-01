import zipfile


def read_file(path: str, zip_entry_path: str) -> str:
    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as zip_ref:
            with zip_ref.open(zip_entry_path) as file:
                return file.read().decode("utf-8")
    with open(path) as file:
        return file.read()
