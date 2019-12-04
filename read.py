import xlrd
import constants
from structs import Transaction

def read_database(path):
	wb = xlrd.open_workbook(path)
	ws = wb.sheet_by_index(0)
	all_transactions = []
	for i in range(1, ws.nrows):
		trans = Transaction(
			int(ws.cell_value(i,0)), #id
			ws.cell_value(i, 1), #item name
			int(ws.cell_value(i, 2)), #buy
			int(ws.cell_value(i, 3)), #sell
			int(ws.cell_value(i, 4)), #quantity
			ws.cell_value(i, 5), #notes
			ws.cell_value(i, 6), #start time
			ws.cell_value(i, 7), 
			ws.cell_value(i, 8), 
			ws.cell_value(i, 9), 
			ws.cell_value(i, 10), 
			ws.cell_value(i, 11), #end time
			ws.cell_value(i, 12), 
			ws.cell_value(i, 13), 
			ws.cell_value(i, 14), 
			ws.cell_value(i, 15),
			ws.cell_value(i, 16) #completed 
			)
		all_transactions.append(trans)
		
	return all_transactions