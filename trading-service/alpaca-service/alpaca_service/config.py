import os
import json
from dotenv import load_dotenv, dotenv_values

dotenv_path = "/app/alpaca-service/.env"
load_dotenv(dotenv_path=dotenv_path)

accounts_json = os.getenv("ALPACA_ACCOUNTS")
alpaca_accounts = json.loads(accounts_json)
