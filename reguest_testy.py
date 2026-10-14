import requests
adress = "http://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json"

odp = requests.get(adress)
print(odp.status_code)

print("--------")
print(odp.text)


dane = odp.json()
print(dane)


print(dane["rates"][0]["mid"])
