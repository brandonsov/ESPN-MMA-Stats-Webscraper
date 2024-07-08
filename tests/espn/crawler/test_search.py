import os
from unittest.mock import patch

from src.espn.crawler.search import query_players


@patch("src.espn.crawler.search.get_data_cache")
def test_query_players_cached(get_data_cache_mock):
    get_data_cache_mock.return_value = f"{os.getcwd()}/tests/fixtures"
    response = query_players("alex pereira")

    assert response
