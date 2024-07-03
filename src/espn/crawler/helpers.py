import logging
import os

logging.basicConfig(level=logging.DEBUG)


def check_file_exists(file_name: str) -> bool:
    return os.path.isfile(file_name)


def write_file(
    content: str,
    file_name: str,
    overwrite_file: bool = False,
) -> bool:
    if not overwrite_file and check_file_exists(file_name):
        logging.warn(f"File `{file_name}` already exists")
        return False

    with open(file_name, "w") as html_file:
        logging.debug(f"Creating file {file_name}")
        html_file.write(content)
        logging.info(f"Finished creating file {file_name}")

    return True
