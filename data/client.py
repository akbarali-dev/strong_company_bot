import requests
import logging
from data.config import LINK


def get_data(sub_url, path_var=None):
    url = f"{LINK}/{sub_url}/"
    if path_var:
        url = f"{url}{path_var}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
