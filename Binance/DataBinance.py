import json
import requests 

class Data_Binance:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.search_url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

    def search_ads(self, asset: str, fiat: str, rows: str, trade_type: str, page=1) -> dict:
        payload = {
            "asset": asset,
            "fiat": fiat,
            "tradeType": trade_type,
            "page": page,
            "rows": rows
            #"payTypes": pay_types
        }
        resp = requests.post(self.search_url, headers=self.headers, data=json.dumps(payload))
        data = resp.json()
        return data

Data_Binance = Data_Binance()    
print(Data_Binance.search_ads("USDT", "ARS", "10", "SELL"))