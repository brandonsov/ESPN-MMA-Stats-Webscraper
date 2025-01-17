import logging
import os

from src.espn.crawler.constants import DATA_CACHE_LOCATION

logging.basicConfig(level=logging.DEBUG)


def get_data_cache() -> str:
    return DATA_CACHE_LOCATION


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
