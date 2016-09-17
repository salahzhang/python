import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipeida.org/wiki/Comparison_of_text_editors")
bs0bj = BeautifulSoup(html,"html.parser")

table = bs0bj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("../files/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
	for cell in row.findAll(['td', 'th']):
		csvRow.append(cell.get_text())
	writer.writerrow(csvRow)
finally:
	csvFile.close()
	