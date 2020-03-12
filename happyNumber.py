# -*- coding: utf-8 -*-

# Desafio Dojo Puzzles: http://dojopuzzles.com/problemas/exibe/numeros-felizes/


class HappyNumber():
	# Verifica se o número 'a' é feliz ou triste
	#  Ou seja, verifica o número 'a' até encontrar 1 ou um loop infinito (um número repetido) 
	def checkNumber(self, a):
		currentNumber = a
		listOfNumbers = []

		try:
			assert isinstance(a, int)
			while True:
				if (currentNumber==1 or currentNumber==0):
					return 'Happy number'
				elif (currentNumber in listOfNumbers):
					return 'Sad number'
				else:
					listOfNumbers.append(currentNumber)
					currentNumber = self.findNext(currentNumber)
			
		except AssertionError:
			print('Invalid input')
			return -1
	
	# Retorna a soma do quadrado dos digitos do número 'a'
	def findNext(self, a):
		dividend = a
		divisor = 10
		sumOfDigits = 0

		while True:
			quotient = dividend//divisor
			if quotient==0:
				sumOfDigits += pow(dividend, 2)
				return sumOfDigits
			else:
				sumOfDigits += pow(dividend%divisor, 2)
				dividend = quotient