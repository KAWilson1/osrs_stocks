#TODO: make item_name the foreign key of the Item class

class Transaction():
	def __init__(self, transaction_id, item_name, unit_price, unit_intended_sell_price, quantity, notes,
		start_year, start_month, start_day, start_hour, start_minute, 
		end_year="None", end_month="None", end_day="None", end_hour="None", end_minute="None",  
		completed="None"):
		self.transaction_id = transaction_id
		self.item_name = item_name
		self.unit_price = unit_price
		self.unit_intended_sell_price = unit_intended_sell_price
		self.quantity = quantity
		self.notes = notes

		self.start_year = start_year
		self.start_month = start_month
		self.start_day = start_day
		self.start_hour = start_hour
		self.start_minute = start_minute

		self.end_year = end_year
		self.end_month = end_month
		self.end_day = end_day
		self.end_hour = end_hour
		self.end_minute = end_minute

		self.completed = completed

class MarginCheck():
	def __init__(self, item_name, sell_margin, buy_margin, curr_year, curr_month, curr_day, curr_hour, curr_minute)
		self.margin_id = 1
		self.item_name = item_name
		self.sell_margin = sell_margin
		self.buy_margin = buy_margin
		self.curr_year = curr_year
		self.curr_month = curr_month
		self.curr_day = curr_day
		self.curr_hour = curr_hour
		self.curr_minute = curr_minute

class Item():
	def __init__(self, internal_id, name):
		#TODO: Fill in
		pass

class ItemStats():
	def __init__(self, item):
		self.item = item

	def calc_average_price(): #TODO: define
		pass


