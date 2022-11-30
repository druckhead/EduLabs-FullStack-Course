# Implement a dictionary to store stocks data.
# Your dictionary should allow searching stocks by ticker.
# Data you should be able to store in your dictionary:

# Ticker
# Company name
# Employees number
# Address
# CEO name
# Stock prices data by date that includes: open price, close price, volume

# 	For example:
# company: Tesla
# ticker: TSLA
# employees num: 5000
# address: California
# CEO: Elon Musk
# stocks data (per date):
#  ...
#  14.11.2021: open price 1001.5, close price: 1020, volume: 50000000
#  15.11.2021: open price: 1067.7, close price: 1045.5, volume: 45000345

from pprint import pprint

stocks = {
    "AAPL": {
        "company_name": "Apple Inc",
        "num_employees": 0,
        "address": "",
        "CEO": "",
        "prices": {
            "14.11.21": {
                "open_price": 0.0,
                "close_price": 0.0,
                "volume": 0
            },
            "17.11.21": {
                "open_price": 0.0,
                "close_price": 0.0,
                "volume": 0
            },
        }
    },
    "TSLA": {
        "company_name": "Tesla",
        "num_employees": 0,
        "address": "",
        "CEO": "",
        "prices": {
            "14.11.21": {
                "open_price": 0.0,
                "close_price": 0.0,
                "volume": 0
            },
            "17.11.21": {
                "open_price": 0.0,
                "close_price": 0.0,
                "volume": 0
            },
        }
    },
}

abc = {
    1: "2",
    2: "3",
    2: "1"
}

pprint(stocks)

# pprint(stocks.get('AAPL').get('prices').get('14.11.21').get('close_price'))