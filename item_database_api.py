from osrsbox import items_api #https://www.osrsbox.com/projects/osrsbox-db/#the-item-database



def get_trade_limit(item_to_lookup):
	"""
	Looks items up by name

	Params:
		item_to_lookup <str>
			Name of the item you want to lookup, case insensitive
	Return:
		trade_limit <int> or False
			Returns False if the item cannot be found in the database
	"""
	trade_limit = False

	all_db_items = items_api.load()
	for item in all_db_items:
		if item_to_lookup.lower() == item.name.lower():
			trade_limit = item.buy_limit
			break
	
	return trade_limit

def show_all_item_trade_limits():
	all_db_items = items_api.load()
	for item in all_db_items:
		print(item.name + " : " + str(item.buy_limit))

if __name__ == "__main__":
	print(get_trade_limit("abyssal whipao"))