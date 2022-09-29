import asyncio
import codecs
import csv
import json

from aiohttp import ClientSession

from apps.items.models.item import Item
from apps.items.utils import validate_json
from settings.base import API_MELI
from settings.db_connection import save_all


def save_items(items):
    objs_items = []
    for item in items:
        if bool(item):
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
    params_item = {
        "ids": item_code,
        "attributes": "price,start_time,category_id,currency_id,seller_id",
    }
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

    async with session.get(
        f"{url}categories/{item['category_id']}", params=params_category
    ) as category_resp:
        category_data = await category_resp.json()
        item["name"] = category_data["name"]

    async with session.get(
        f"{url}currencies/{item['currency_id']}", params={"attributes": "description"}
    ) as currency_resp:
        currency_data = await currency_resp.json()
        item["description"] = currency_data["description"]

    async with session.get(
        f"{url}users/{item['seller_id']}", params={"attributes": "nickname"}
    ) as user_resp:
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

    return len(response)
