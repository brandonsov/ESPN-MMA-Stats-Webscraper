import logging
import os.path
from urllib.request import urlopen

from constants import DATA_CACHE_LOCATION

logging.basicConfig(level=logging.DEBUG)


def get_page_html(url) -> str:
    page = urlopen(url)
    html_bytes = page.read()

    return html_bytes.decode("utf-8")


def write_file(content: str, file_name: str, overwrite_file: bool = False) -> bool:
    if not overwrite_file and os.path.isfile(file_name):
        logging.warn(f"File `{file_name}` already exists")
        return False

    with open(file_name, "w") as html_file:
        logging.debug(f"Creating file {file_name}")
        html_file.write(content)
        logging.info(f"Finished creating file {file_name}")

    return True


class Page:
    url: str = None
    content: str = None
    file_name: str = None

    def __init__(
        self,
        url: str,
        file_name: str = None,
        try_cache: bool = False,
        cache_write: bool = True,
    ):
        logging.debug(f"Creating Page object: {locals()}")
        self.url = url
        self.file_name = f"{DATA_CACHE_LOCATION}/{file_name}"

        if try_cache:
            logging.debug("Attempting to fetch cached file")
            with open(self.file_name, "r") as cached_file:
                self.content = cached_file.read()

        if not self.content:
            self.content = get_page_html(url)

            if cache_write and self.file_name:
                write_file(self.content, self.file_name, True)
