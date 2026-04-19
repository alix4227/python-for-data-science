#!/usr/bin/env python3.10
def all_thing_is_obj(object: any)-> int:
	typ = type(object)
	types = [list, tuple, set, dict, str]
	names = ["List", "Tuple", "Set", "Dict", "is in the kitchen"]
	for i in range(len(types)):
		if typ == types[i]:
			if i == len(types) - 1:
				print(f"{object} {names[i]}: {typ}")
			else:
				print(f"{names[i]}: {typ}")
			return 42
	print(f"Type not found")
	return 42