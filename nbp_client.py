from requests import get

import requests
class NBPClient:
    def __init__(self):
        self.adres = "http://api.nbp.pl/api/exchangerates/rates/a/"
        self.waluta = None
        self.koszt = None
    def pobierz_kurs(self, waluta):

       pelen_adres = f"{self.adres}{waluta}/?format=json"
       odp = requests.get(pelen_adres)
       if not odp.status_code == 200:
           print("blad")
       else:
           tabela = odp.json()
           aktualny_kurs = tabela["rates"][0]["mid"]
           self.koszt = aktualny_kurs
           self.waluta = waluta


if __name__ == '__main__':
    nbp = NBPClient()
    nbp.pobierz_kurs("eur")
    print(nbp.waluta)
    print(nbp.koszt)






