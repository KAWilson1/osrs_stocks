import xlsxwriter
import constants

def write_to_database(path, data):
	wb = xlsxwriter.Workbook(path)
	ws = wb.add_worksheet()
	print(data)
	for i in range(len(data)):
	    for j in range(len(constants.TRANSACTION_HEADERS)):
	        ws.write(i, j, data[i][j])
	wb.close()