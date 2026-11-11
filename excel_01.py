from openpyxl import load_workbook, Workbook

def make_workbook(sciezka = 'kurs.xlsx',naglowki = ["Data", "Waluta","Kurs NBP"], tytul = "arkusz"):
    skoroszyt = Workbook()
    arkusz = skoroszyt.active
    arkusz.title = tytul
    arkusz.append(naglowki)
    skoroszyt.save(sciezka)

def dopisz_wiersz_na_obiekcie(arkusz,dane):
    arkusz.append(dane)

def dopisz_dane_load(sciezka = "kurs.xlsx",dane = 'null'):
    skoroszyt = load_workbook(sciezka)
    arkusz = skoroszyt.active
    arkusz.append(dane)
    skoroszyt.save(sciezka)

def zakoncz_i_zapisz(skoroszyt,scierzka):
    skoroszyt.save(scierzka)
    skoroszyt.close()


def utwurz_i_dopisz(sciezka = 'kurs.xlsx',naglowki = ["Data", "Waluta","Kurs NBP"], tytul = "arkusz",dane = "null"):
    skoroszyt = Workbook()
    arkusz = skoroszyt.active
    arkusz.title = tytul
    arkusz.append(naglowki)
    arkusz.append(dane)


