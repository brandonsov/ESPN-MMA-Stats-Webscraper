import json
import logging
import urllib.parse

import requests
from constants import (
    DATA_CACHE_LOCATION,
    ESPN_SEARCH_API_CALL,
    OUTPUT_SEARCH_API_CALL_JSON_FILE_SUFFIX,
)
from helpers import check_file_exists, write_file

logging.basicConfig(level=logging.DEBUG)


def query_players(name_query: str) -> str:
    logging.info(f"Querying player {name_query}")

    query_safe_name = urllib.parse.quote(name_query)
    search_query = f"{ESPN_SEARCH_API_CALL}{query_safe_name}"
    output_file_name = f"{DATA_CACHE_LOCATION}/{name_query.lower().replace(" ", "_")}{OUTPUT_SEARCH_API_CALL_JSON_FILE_SUFFIX}"
    if check_file_exists(output_file_name):
        logging.info(f"Using cached file {output_file_name}")
        with open(output_file_name, "r") as response_json:
            response = response_json.read()
    else:
        logging.info(f"Calling GET {search_query}")
        response = requests.get(search_query)
        write_file(json.dumps(response.json()), output_file_name, True)


query_players("Alex Pereira")
