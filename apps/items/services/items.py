import codecs
import csv
import json
import logging

from apps.items.models.item import Item
from services.service_meli import ServiceMeli
from settings.db_connection import save as save_db
from concurrent.futures import ThreadPoolExecutor

from apps.items.utils import validate_json

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
executor = ThreadPoolExecutor(max_workers=6)

def get_item(item):
    api = ServiceMeli(
        params={
            "ids": item,
            "attributes": "price,start_time,category_id,currency_id,seller_id",
        },
        path="items",
    )

    item_info = api.get()

    return item_info


def get_category(category_id):
    api = ServiceMeli(params={"attributes": "name"}, path=f"categories/{category_id}")

    category_info = api.get()

    return category_info


def get_currency(currency_id: str):
    api = ServiceMeli(
        params={"attributes": "description"}, path=f"currencies/{currency_id}"
    )

    currency_info = api.get()

    return currency_info


def get_user(user_id: int):
    api = ServiceMeli(params={"attributes": "nickname"}, path=f"users/{user_id}")

    user_info = api.get()

    return user_info


def save_item(item: list):
    item_data = get_item("".join(item))
    if item_data[0]["code"] == 200:

        isValid = validate_json(item_data[0]["body"])

        if isValid:
            print("entraaaaa")
            category_data = get_category(item_data[0]["body"]["category_id"])
            currency_data = get_currency(item_data[0]["body"]["currency_id"])
            user_data = get_user(item_data[0]["body"]["seller_id"])
            

            try:
                obj = Item(
                    site=item[0],
                    item_code=item[1],
                    price=item_data[0]["body"]["price"],
                    start_time=item_data[0]["body"]["start_time"],
                    name=category_data["name"],
                    description=currency_data["description"],
                    nickname=user_data["nickname"],
                )

                save_db(obj)
            except Exception as err:
                raise err



def read_file(file, params):
    config_params = json.loads(params)
    stream = codecs.iterdecode(file.stream, config_params["encoding"])

    for index, row in enumerate(
        csv.reader(stream, delimiter=config_params["separator"])
    ):
        if row and index >= 1:
            executor.submit(save_item, row)

    return 1
