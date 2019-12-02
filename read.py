import xlrd
import constants

def read_database(path):
	wb = xlrd.open_workbook(path)
	ws = wb.sheet_by_index(0)
	all_rows = []
	for i in range(1, ws.nrows):
		row = []
		for j in range(len(constants.TRANSACTION_HEADERS)):
			row.append(ws.cell_value(i, j))
		all_rows.append(row)
	return all_rows