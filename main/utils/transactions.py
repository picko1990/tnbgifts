import requests


def get_transactions(recipient=""):
    bank_address = "http://54.183.16.194"
    response = requests.get(
        f"{bank_address}/bank_transactions?ordering=-block__created_date&recipient={recipient}&limit=100"
    ).json()
    txs = response["results"]
    if txs:
        while response["next"]:
            response = requests.get(response["next"]).json()
            txs.extend(response["results"])
    return txs
