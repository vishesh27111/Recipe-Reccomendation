import sys
from BigBasket import add

def add_to_list():
	item = sys.argv[1:]
	print(item)
	for i in item:
		add(i)
	return

if __name__ == '__main__':
	add_to_list()