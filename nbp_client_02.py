import requests

class NBPwaluta():
    def __init__(self,waluta):
        self.adres = None
        self.waluta = waluta
        self.pobierz_kurs()

    def pobierz_kurs(self):
        self.adres = "http://api.nbp.pl/api/exchangerates/rates/a/"
        pelen_adres = f"{self.adres}{str(self.waluta)}/?format=json"
        self.polaczenie = requests.get(pelen_adres)
        if self.polaczenie.status_code != 200:
            print("blad polaczenia")
            raise ValueError(f"Nie udało się pobrać danych dla waluty {self.waluta}")
        json = self.polaczenie.json()
        self.koszt = json['rates'][0]['mid']
    def __repr__(self):
        return f"Kurs {self.waluta} to {self.koszt}"


    def przelicz_na_pln(self,ilosc_pieniedzy):
        ile_to_bedzie_waluty = ilosc_pieniedzy * self.koszt
        return ile_to_bedzie_waluty







if __name__ == '__main__':
    eur = NBPwaluta('eur')
    print(eur.koszt)
    usd = NBPwaluta('usd')
    print(usd.koszt)
    print(eur)
    print (eur.przelicz_na_pln(1000))