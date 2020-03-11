from happyNumber import HappyNumber

number = HappyNumber()
for i in range(1,25):
	print(str(i)+" is a "+number.checkNumber(i))