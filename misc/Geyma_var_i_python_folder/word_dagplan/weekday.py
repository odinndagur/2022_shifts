import datetime

# intDay = datetime.date(year=2000, month=12, day=1).weekday()

def get_weekday(year=None, month=None, day=None):
    days = ["Mánudagur", "Þriðjudagur", "Miðvikudagur", "Fimmtudagur", "Föstudagur", "Laugardagur", "Sunnudagur"]
    if not any([year,month,day]):
        raise ValueError('Need to input date')
    currentDate = datetime.datetime.today()
    if not year:
        if int(month) < currentDate.month and currentDate.month > 10:
            year = currentDate.year + 1
        else:
            year = currentDate.year
    inputDate = datetime.date(year=year,month=int(month),day=int(day))
    return days[inputDate.weekday()]