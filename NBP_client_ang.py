import requests
from datetime import datetime, timedelta, date


class Currency:
    def __init__(self, currency, cost, rate_date):
        self.currency = currency
        self.cost = cost
        self.date = rate_date

    def convert_to_pln(self, amount):
        return amount * self.cost

    def __repr__(self):
        return f"Rate for {self.currency} is {self.cost} PLN on {self.date}"




class NbpClient:
    def __init__(self):
        self.base_url = "http://api.nbp.pl/api/exchangerates/rates/a/"
        self.json_suffix = "/?format=json"

    def get_currency(self, code, rate_date=None):
        if rate_date is None:
            full_url = f"{self.base_url}{code}{self.json_suffix}"
        else:
            try:
                date_object = datetime.strptime(rate_date, "%Y-%m-%d")
                day_of_week = date_object.isoweekday()
                if day_of_week == 6:
                    date_object = date_object - timedelta(days=1)
                elif day_of_week == 7:
                    date_object = date_object - timedelta(days=2)
                rate_date = date_object.strftime("%Y-%m-%d")

                full_url = f"{self.base_url}{code}/{rate_date}{self.json_suffix}"

            except ValueError:
                print("Invalid date format or date does not exist in calendar!")
                raise ValueError(f"Invalid date format or date {rate_date} does not exist in calendar!")

        req = requests.get(full_url)
        if req.status_code != 200:
            print("connection error")
            raise ValueError(f"Failed to fetch data for currency {code}")
        response_json = req.json()
        rate = response_json['rates'][0]['mid']
        if rate_date is None:
            rate_date = date.today().isoformat()
        return Currency(code, rate, rate_date)





