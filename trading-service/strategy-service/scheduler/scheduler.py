import schedule
import time
import datetime
import pytz
from strategies.strategy1 import execute_strategy as strategy1
from strategies.strategy2 import execute_strategy as strategy2

MARKET_TIMEZONE = pytz.timezone("US/Eastern")
MARKET_OPEN = "09:30"

def run_strategies():
    print(f"Running strategies at {datetime.datetime.now()}")
    market_data = get_market_data()
    
    strategy1(market_data)
    strategy2(market_data)
    print("All strategies executed!")

def convert_to_server_time(market_time):
    market_datetime = datetime.datetime.strptime(market_time, "%H:%M").time()
    market_now = datetime.datetime.combine(datetime.date.today(), market_datetime)
    market_now = MARKET_TIMEZONE.localize(market_now)

    server_timezone = pytz.timezone("UTC")
    return market_now.astimezone(server_timezone).strftime("%H:%M")

def start_scheduler():
    server_time = convert_to_server_time(MARKET_OPEN)
    print(f"Scheduler set to run at {server_time} (server time)")
    schedule.every().day.at(server_time).do(run_strategies)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    start_scheduler()
