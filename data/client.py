import requests
import logging


def get_data(sub_url, path_var=None):
    url = f"http://localhost:8001/bot/{sub_url}/"
    if path_var:
        url = f"{url}{path_var}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # JSON formatida javobni qaytarish
    else:
        return None


def get_personal_data():
    response = requests.get(url + '/data/')
    if response.status_code == 200:
        return response.json()  # JSON formatida javobni qaytarish
    else:
        return None


def get_contact_data():
    response = requests.get(url + 'contact/')
    if response.status_code == 200:
        return response.json()  # JSON formatida javobni qaytarish
    else:
        return None


def get_file(f_type):
    response = requests.get(url + 'file/' + f_type)
    if response.status_code == 200:
        return response.json()  # JSON formatida javobni qaytarish
    else:
        return None


def get_portfolio(f_type):
    response = requests.get(url + 'portfolio/' + f_type)
    if response.status_code == 200:
        return response.json()  # JSON formatida javobni qaytarish
    else:
        return None
