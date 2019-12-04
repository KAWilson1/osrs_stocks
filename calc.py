def margin(buy, sell):
	return sell - buy

def invested(buy, kiloquantity):
	return buy * kiloquantity * 1000

def profit(buy, sell, kiloquantity):
	return margin(buy, sell) * kiloquantity * 1000

def roi(buy, sell, kiloquantity):
	return round(profit(buy, sell, kiloquantity) / invested(buy, kiloquantity) * 100, 2)