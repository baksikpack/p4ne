from openpyxl import load_workbook
from matplotlib import pyplot

wb = load_workbook('data_analysis_lab.xlsx') #загрузка таблицы
sheet = wb['Data'] #загрузка листа из таблицы
def getvalue(x):
    return x.value

years = list(map(getvalue, sheet['A'][1:]))
temprel = list(map(getvalue, sheet['C'][1:]))
sun = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temprel, label="температура")
pyplot.plot(years, sun, label="температура")

pyplot.show()
