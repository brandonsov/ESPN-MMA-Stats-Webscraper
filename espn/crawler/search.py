import json
import urllib.parse

import requests
from constants import (
    DATA_CACHE_LOCATION,
    ESPN_SEARCH_API_CALL,
    OUTPUT_SEARCH_API_CALL_JSON_FILE_SUFFIX,
)
from helpers import write_file


def query_players(name_query: str):
    query_safe_name = urllib.parse.quote(name_query)
    search_query = f"{ESPN_SEARCH_API_CALL}{query_safe_name}"

    response = requests.get(search_query)

    output_file_name = f"{DATA_CACHE_LOCATION}/{name_query.replace(" ", "_")}{OUTPUT_SEARCH_API_CALL_JSON_FILE_SUFFIX}"
    write_file(json.dumps(response.json()), output_file_name, True)
