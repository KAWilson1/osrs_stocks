#TODO: make item_name the foreign key of the Item class

class Transaction():
	def __init__(self, item_name, unit_price, unit_intended_sell_price, quantity, start_time, end_time=None, notes="", completed=False):
		self.item_name = item_name
		self.unit_price = unit_price
		self.unit_intended_sell_price = unit_intended_sell_price
		self.quantity = quantity
		self.start_time = start_time


class Item():
	def __init__(self, internal_id, name):
		#TODO: Fill in

class ItemStats():
	def __init__(self, item):
		self.item = item

	def calc_average_price(): #TODO: define
		pass


