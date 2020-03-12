from happyNumber import HappyNumber
def main():
	number = HappyNumber()
	for i in range(1,10):
		print(str(i)+" is a "+number.checkNumber(i))
		
if __name__ == '__main__':
	main()