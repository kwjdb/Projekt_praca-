from openpyxl import load_workbook, workbook
from nbp_clinet_03 import Nbp_Client

if __name__ == '__main__':
    wb = load_workbook("excel test.xlsx")
    ws = wb.active
    kilent = Nbp_Client()
    wb_out = workbook.Workbook()
    ws_out = wb_out.active
    ws_out.title = 'rozliczenie'
    ws_out.append(["Data", "Waluta", "Kwota Waluta", "Kurs NBP", "Kwota PLN"])
    kwota_ilosc = 100
    for row in ws.iter_rows(min_row=2 ,values_only=True):
        data, waluta, kwota = row
        obiekt = kilent.pobierz_walute(waluta,data)
        kwota_pln = obiekt.przelicz_na_pln(kwota_ilosc)
        print(kwota_pln)
        print(obiekt)
        ws_out.append([data,waluta,kwota_ilosc,kwota,kwota_pln])

    wb_out.save("faktury_rozliczone.xlsx")
    print("Gotowe! Zapisano plik faktury_rozliczone.xlsx")