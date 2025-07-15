from dotenv import load_dotenv
from os import getenv

load_dotenv()

APP_ENV = getenv("APP_ENV", "development")

LOG_LEVEL = getenv("LOG_LEVEL", "DEBUG")
