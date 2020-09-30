import gspread

gc = gspread.service_account(filename='./fallgraphs-1e6b222aade1.json')
sh = gc.open("Fall Guys")
sheet = sh.worksheet("Copy of Data")

def append_data(datalist):
    sheet.append_row(datalist)






