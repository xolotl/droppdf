import xlrd
import csv
from os import sys

def csv_from_excel(excel_file):
	workbook = xlrd.open_workbook(excel_file)

	worksheet_name = workbook.sheet_names()[0]

	#all_worksheets = workbook.sheet_names()
	#for worksheet_name in all_worksheets:
	worksheet = workbook.sheet_by_name(worksheet_name)
	your_csv_file = open(''.join([worksheet_name,'.csv']), 'wb')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

	for rownum in xrange(worksheet.nrows):
		wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
	your_csv_file.close()

if __name__ == "__main__":
    csv_from_excel("pp.xlsx")
