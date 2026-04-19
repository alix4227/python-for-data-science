import sys

def main(args):
	try:
		if (len(args) == 1):
			return
		if not args[1].isdigit() :
			raise AssertionError("argument is not an integer")
		if len(args) > 2 :
			raise AssertionError("more than one argument is provided")
		nb = int(args[1])
		if (nb % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except AssertionError as e:
		print(f'Assertion error: {e}')

if __name__ == "__main__":
	main(sys.argv)