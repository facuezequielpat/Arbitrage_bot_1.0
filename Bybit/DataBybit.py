from dotenv import load_dotenv
import os
import requests
import json
from bybit_p2p import P2P

load_dotenv()
class Data_Bybit:
    def __init__(self):
        self.api_key = os.getenv("apiKeybit")
        self.api_secret = os.getenv("secretKeybit")
        self.client = P2P(testnet=False, api_key=self.api_key, api_secret=self.api_secret)

    def search_ads(self,tokenId:str,currencyId:str,side:str,size:str="10"):
        '''Obtiene anuncios P2P en Bybit.'''
        anuncios_online = self.client.get_online_ads(
            tokenId=tokenId,
            currencyId=currencyId,
            side=side,
            size=size)["result"]["items"]
        return anuncios_online

Data_Bybit = Data_Bybit()
print(Data_Bybit.search_ads("USDT","ARS","1"))
