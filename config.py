import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# webhook
URL = os.environ.get('URL')
PORT = int(os.environ.get('PORT', '5000'))

# telegram
TOKEN = os.environ.get('TOKEN')

ENV = os.environ.get("ENV", "prod")
