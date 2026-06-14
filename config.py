import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class UserCredentials:
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')

class PageElements:
    EMAIL_FIELD = '[name="email"]'