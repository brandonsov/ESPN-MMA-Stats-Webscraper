import logging
from urllib.request import urlopen

from constants import DATA_CACHE_LOCATION
from helpers import write_file

logging.basicConfig(level=logging.DEBUG)


def get_page_html(url) -> str:
    page = urlopen(url)
    html_bytes = page.read()

    return html_bytes.decode("utf-8")


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
            logging.debug(f"Attempting to fetch cached file {self.file_name}")
            with open(self.file_name, "r") as cached_file:
                self.content = cached_file.read()
                logging.debug(f"Fetched cached file {self.file_name}")

        if not self.content:
            self.content = get_page_html(url)

            if cache_write and self.file_name:
                write_file(self.content, self.file_name, True)
