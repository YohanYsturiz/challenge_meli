import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    DEBUG = True
    API_MELI = os.environ.get("API_MELI")
    DATABASE = os.environ.get("CHALLANGE_DB")