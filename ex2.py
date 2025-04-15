from datetime import datetime

def calc_data(date1, date2):
    date1 = datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.strptime(date2, "%d/%m/%Y")

    return abs((date2 - date1).days)
