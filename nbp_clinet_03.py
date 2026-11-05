import requests
from datetime import datetime,timedelta,date


class Waluta:
    def __init__(self,waluta,koszt,data):
        self.waluta = waluta
        self.koszt = koszt
        self.data = data
    def przelicz_na_pln(self,kwota):
        return kwota * self.koszt
    def __repr__(self):
        return f"Kurs {self.waluta} to {self.koszt} PLN z dnia {self.data}"




class Nbp_Client:
    def __init__(self):
        self.podstawa_adresu ="http://api.nbp.pl/api/exchangerates/rates/a/"
        self.koniec_adresu_json = "/?format=json"

    def pobierz_walute(self,kod,data=None):
        if data is None:


            adres_pelny = (f"{self.podstawa_adresu}{kod}{self.koniec_adresu_json}")

        else:
            try:
                data_obiekt = datetime.strptime(data, "%Y-%m-%d")
                dzien_tygodnia = data_obiekt.isoweekday()
                if dzien_tygodnia == 6:
                    data_obiekt = data_obiekt - timedelta(days=1)
                elif dzien_tygodnia == 7:
                    data_obiekt = data_obiekt - timedelta(days=2)
                data = data_obiekt.strftime("%Y-%m-%d")

                adres_pelny = (f"{self.podstawa_adresu}{kod}/{data}{self.koniec_adresu_json}")

            except ValueError:
                print("Błędny format daty lub data nie istnieje w kalendarzu!")
                raise ValueError(f"Błędny format daty lub data {data} nie istnieje w kalendarzu!")


        req = requests.get(adres_pelny)
        if req.status_code != 200:
            print("blad polaczenia")
            raise ValueError(f"Nie udało się pobrać danych dla waluty {kod}")
        json = req.json()
        kurs = json['rates'][0]['mid']
        if data is None:
            data = date.today().isoformat()
        return Waluta(kod,kurs,data)





if __name__ == '__main__':
    klient = Nbp_Client()
    usd = klient.pobierz_walute("usd")
    print(usd)
    usd_stare = klient.pobierz_walute("usd","2005-07-21")
    print(usd_stare)
    usd_niedziela = klient.pobierz_walute("usd", "2026-11-01")
    print(usd_niedziela)
