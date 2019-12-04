import xlsxwriter
import constants
from structs import Transaction

def write_to_database(path, transactions):
	wb = xlsxwriter.Workbook(path)
	ws = wb.add_worksheet()

	for j in range(len(constants.TRANSACTION_HEADERS)):
		ws.write(0, j, constants.TRANSACTION_HEADERS[j])

	for i in range(0, len(transactions)):
		ws.write(i+1, 0, int(transactions[i].transaction_id))
		ws.write(i+1, 1, transactions[i].item_name) 
		ws.write(i+1, 2, int(transactions[i].unit_price))
		ws.write(i+1, 3, int(transactions[i].unit_intended_sell_price))
		ws.write(i+1, 4, int(transactions[i].quantity))
		ws.write(i+1, 5, transactions[i].notes)
		ws.write(i+1, 6, transactions[i].start_year)
		ws.write(i+1, 7, transactions[i].start_month) 
		ws.write(i+1, 8, transactions[i].start_day) 
		ws.write(i+1, 9, transactions[i].start_hour) 
		ws.write(i+1, 10, transactions[i].start_minute) 
		ws.write(i+1, 11, transactions[i].end_year)  
		ws.write(i+1, 12, transactions[i].end_month)  
		ws.write(i+1, 13, transactions[i].end_day)  
		ws.write(i+1, 14, transactions[i].end_hour)  
		ws.write(i+1, 15, transactions[i].end_minute) 
		ws.write(i+1, 16, transactions[i].completed)  
	wb.close()

def write_sample_data(path): #Do not use in production, overwrites database entirely
	wb = xlsxwriter.Workbook(path)
	ws = wb.add_worksheet()

	for j in range(len(constants.TRANSACTION_HEADERS)):
		ws.write(0, j, constants.TRANSACTION_HEADERS[j])

	for i in range(10):
		ws.write(i+1, 0, i+1)
		ws.write(i+1, 1, "test" + str(i+1)) 
		ws.write(i+1, 2, 10 + i)
		ws.write(i+1, 3, 11 + i)
		ws.write(i+1, 4, 3)
		ws.write(i+1, 5, "Notes")
		ws.write(i+1, 6, 2019)
		ws.write(i+1, 7, 12) 
		ws.write(i+1, 8, 4) 
		ws.write(i+1, 9, 11) 
		ws.write(i+1, 10, 15) 
		if i < 5:
			ws.write(i+1, 11, "None")  
			ws.write(i+1, 12, "None")  
			ws.write(i+1, 13, "None")  
			ws.write(i+1, 14, "None")  
			ws.write(i+1, 15, "None") 
			ws.write(i+1, 16, "None")  
		else:
			ws.write(i+1, 11, 2019)  
			ws.write(i+1, 12, 13)  
			ws.write(i+1, 13, 5)  
			ws.write(i+1, 14, 12)  
			ws.write(i+1, 15, 16) 
			ws.write(i+1, 16, constants.COMPLETION_SPEEDS[1])  
	wb.close()

if __name__ == "__main__":
	write_sample_data(constants.PATH_TO_DATABASE)