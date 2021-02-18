import requests
import json

_config = {
    "publicKey": "oBeeALiv5vyEuVv06nW4gBU5I4Ek6Il9A2pLI3UFPrL6inYIHvw4dCMHU5pTP2GA",
    "privateKey": "m6tJ4C0faniubHBQEbFUPvfzbsYHzbhMNRaL0BJJm3oaycHaS8oLt67OVBZbZTMx"
}

api = "https://api1.binance.com"

def req(url):
    r = requests.get(url)
    return json.loads(r.content)

def candles():
    url = api+f"/api/v3/klines?symbol=XRPBTC&interval=1w&limit=1000"
    return req(url)

cndls = candles()
closed = []
total = 0
for c in cndls:
    total += float(c[4])
    closed.append(c[4])

print(min(closed), max(closed))
print(total/len(closed))