from openpyxl import Workbook


if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    ws.title = "arkusz huberta"
    ws.append(["KolumnaA", "KolumnaB", "KolumnaC"])
    ws.append(["wartość_string", "wartość_string", "wartosc liczbowa"])
    wb.save("excel testowy 1.xlsx")