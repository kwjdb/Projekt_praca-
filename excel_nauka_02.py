from openpyxl import Workbook


from nbp_clinet_03 import Nbp_Client

if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    ws.title = "Wejście"
    ws.append(["data","waluta","kwota"])
    kilent = Nbp_Client()
    us = kilent.pobierz_walute("usd")
    ws.append([us.data,us.waluta,us.koszt])
    wb.save("excel test.xlsx")