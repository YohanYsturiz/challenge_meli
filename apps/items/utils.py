import jsonschema
from jsonschema import validate

item_json_schema = {
    "type": "object",
    "properties": {
        "seller_id": {"type": "number"},
        "price": {"type": "number"},
        "currency_id": {"type": "string"},
        "start_time": {"type": "string"},
        "category_id": {"type": "string"},
    },
    "required": ["seller_id", "price", "currency_id", "start_time", "category_id"],
}


def validate_json(jsonData):
    try:
        validate(instance=jsonData, schema=item_json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
