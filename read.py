import xlrd
import constants
from structs import Transaction, MarginCheck

def transaction_database(path):
	wb = xlrd.open_workbook(path)
	ws = wb.sheet_by_index(0)
	all_transactions = []
	for i in range(1, ws.nrows):
		trans = Transaction(
			int(ws.cell_value(i,0)), #id
			ws.cell_value(i, 1), #item name
			int(ws.cell_value(i, 2)), #buy
			int(ws.cell_value(i, 3)), #sell
			float(ws.cell_value(i, 4)), #quantity
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

def margin_database(path):
	wb = xlrd.open_workbook(path)
	ws = wb.sheet_by_index(0)
	all_margins = []
	for i in range(1, ws.nrows):
		margin = MarginCheck(
			int(ws.cell_value(i, 0)), #id
			ws.cell_value(i, 1), #item name
			int(ws.cell_value(i, 2)), #sell margin
			int(ws.cell_value(i, 3)), #buy margin
			ws.cell_value(i, 4), #time
			ws.cell_value(i, 5), 
			ws.cell_value(i, 6), 
			ws.cell_value(i, 7), 
			ws.cell_value(i, 8), 
			)
		all_margins.append(margin)
	return all_margins