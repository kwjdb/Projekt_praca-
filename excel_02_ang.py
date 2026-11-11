from openpyxl import load_workbook, Workbook

def make_workbook(file_path = 'rates.xlsx', headers = ["Date", "Currency", "NBP Rate"], title = "sheet"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = title
    sheet.column_dimensions['A'].width = 15
    sheet.column_dimensions['B'].width = 15
    sheet.column_dimensions['C'].width = 15
    sheet.append(headers)
    workbook.save(file_path)

def append_row_to_object(sheet, data):
    sheet.append(data)

def append_data_load(file_path = "rates.xlsx", data = 'null'):
    workbook = load_workbook(file_path)
    sheet = workbook.active
    sheet.append(data)
    workbook.save(file_path)

def finish_and_save(workbook, file_path):
    workbook.save(file_path)
    workbook.close()


def create_and_append(file_path = 'rates.xlsx', headers = ["Date", "Currency", "NBP Rate"], title = "sheet", data = "null"):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = title
    sheet.append(headers)
    sheet.append(data)