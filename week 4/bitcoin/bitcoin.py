import requests
import sys

api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
price_str = api["bpi"]["USD"]["rate"]
price_str = price_str.replace(',', '')
price = float(price_str)

amount = float(sys.argv[1])
try:
    float_amount = float(amount)
    total = amount*price
    print(f"${total:,.4f}")
except ValueError:
    sys.exit()
