import codecs
import csv
import json
import asyncio

from apps.items.models.item import Item
from settings.base import API_MELI
from settings.db_connection import save_all, save_one

from aiohttp import ClientSession
from apps.items.utils import validate_json


# def get_item(item):
#     api = ServiceMeli(
#         params={
#             "ids": item,
#             "attributes": "price,start_time,category_id,currency_id,seller_id",
#         },
#         path="items",
#     )

#     item_info = api.get()

#     return item_info


# def get_category(category_id):
#     api = ServiceMeli(params={"attributes": "name"}, path=f"categories/{category_id}")

#     category_info = api.get()

#     return category_info


# def get_currency(currency_id: str):
#     api = ServiceMeli(
#         params={"attributes": "description"}, path=f"currencies/{currency_id}"
#     )

#     currency_info = api.get()

#     return currency_info


# def get_user(user_id: int):
#     api = ServiceMeli(params={"attributes": "nickname"}, path=f"users/{user_id}")

#     user_info = api.get()

#     return user_info


# def save_item(item: list):
#     item_data = get_item("".join(item))
#     if item_data[0]["code"] == 200:

#         isValid = validate_json(item_data[0]["body"])

#         if isValid:
#             category_data = get_category(item_data[0]["body"]["category_id"])
#             currency_data = get_currency(item_data[0]["body"]["currency_id"])
#             user_data = get_user(item_data[0]["body"]["seller_id"])
            

#             try:
#                 obj = Item(
#                     site=item[0],
#                     item_code=item[1],
#                     price=item_data[0]["body"]["price"],
#                     start_time=item_data[0]["body"]["start_time"],
#                     name=category_data["name"],
#                     description=currency_data["description"],
#                     nickname=user_data["nickname"],
#                 )

#                 save_db(obj)
#             except Exception as err:
#                 raise err

def save_items(items):
    objs_items = []
    for item in items:
        if(bool(item)):
            obj = Item(
                site=item["site"],
                item_code=item["item_code"],
                price=item["price"],
                start_time=item["start_time"],
                name=item["name"],
                description=item["description"],
                nickname=item["nickname"],
            )
            objs_items.append(obj)

    save_all(objs_items)

    return True


async def get_item(session, url: str, row: list) -> str:
    item_code = "".join(row)
    params_item = {"ids": item_code, "attributes": "price,start_time,category_id,currency_id,seller_id"}
    params_category = {"attributes": "name"}
    item = {}

    async with session.get(f"{url}/items", params=params_item) as item_resp:
        item_data = await item_resp.json()

        if validate_json(item_data[0]["body"]):
            item = item_data[0]["body"]
            item["site"] = row[0]
            item["item_code"] = row[1]
            item["price"] = item_data[0]["body"]["price"]
            item["start_time"] = item_data[0]["body"]["start_time"]
            item["category_id"] = item_data[0]["body"]["category_id"]
            item["currency_id"] = item_data[0]["body"]["currency_id"]
            item["seller_id"] = item_data[0]["body"]["seller_id"]
        else:
            return {}

    async with session.get(f"{url}categories/{item['category_id']}", params=params_category) as category_resp:
        category_data = await category_resp.json()
        item["name"] = category_data["name"]
    
    async with session.get(f"{url}currencies/{item['currency_id']}", params={"attributes": "description"}) as currency_resp:
        currency_data = await currency_resp.json()
        item["description"] = currency_data["description"]
    
    async with session.get(f"{url}users/{item['seller_id']}", params={"attributes": "nickname"}) as user_resp:
        user_data = await user_resp.json()
        item["nickname"] = user_data["nickname"]

    return item


async def read_file(file, params):
    config_params = json.loads(params)
    stream = codecs.iterdecode(file.stream, config_params["encoding"])

    async with ClientSession() as session:
        tasks = []
        for index, row in enumerate(
            csv.reader(stream, delimiter=config_params["separator"])
        ):
            if row and index >= 1:
                url = f"{API_MELI}"
                tasks.append(asyncio.create_task(get_item(session, url=url, row=row)))
            
            response = await asyncio.gather(*tasks)

    save_items(response)

    return 1


# async def main(stream, config_params):
#     async with ClientSession() as session:
#         tasks = []
#         for index, row in enumerate(
#             csv.reader(stream, delimiter=config_params["separator"])
#         ):
#             if row and index >= 1:
#                 item_code = "".join(row)
#                 url = f"{API_MELI}items?ids={item_code}&attributes=price,start_time,category_id,currency_id,seller_id"
#                 tasks.append(asyncio.create_task(get_item(session, url=url)))
            
#             response = await asyncio.gather(*tasks)
#             print(response)
