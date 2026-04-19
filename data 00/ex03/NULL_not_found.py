def NULL_not_found(object: any)-> int:
	typ = type(object)
	name = ["Nothing", "Cheese", "Zero", "Empty", "Fake"]
	types = [type(None), float, int, str, bool] 
	for i in range(len(name)):
		if (typ == types[i]):
			if (object != "Brian"):
				print(f'{name[i]}: {object} {typ}')
				return 0
			else:
				print ("Type not found")
				return 1
	