import sys
import requests
import json

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif len(sys.argv) == 2 and sys.argv[1].isalpha() == True:
    print("Command-line argument is not a number")
    sys.exit(1)
elif len(sys.argv) != 2:
    print("Too many command-line arguments")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(response.json(), indent = 2))
    current_rate = response.json()["bpi"]["USD"]["rate_float"]
    #print(current_rate)
    bitcoins = float(sys.argv[1])
    bitcoin_value = current_rate * bitcoins
    print(f"${bitcoin_value:,.4f}")



except requests.RequestException:
    sys.exit(1)
except EOFError:
    sys.exit(1)
