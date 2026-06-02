from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client():
    client = Client(
        API_KEY,
        API_SECRET,
        testnet=True
    )

    server_time = client.get_server_time()

    client.timestamp_offset = (
        server_time["serverTime"]
        - int(time.time() * 1000)
    )

    return client