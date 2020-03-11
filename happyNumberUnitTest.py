import unittest
from happyNumber import HappyNumber

class unitTestHappyNumber(unittest.TestCase):

    def setUp(self):
        self.number = HappyNumber()

    def testIf1IsHappyNumber(self):
    	result = self.number.checkNumber(1)
    	self.assertEqual(result, 'Happy number')

    def testIf7IsHappyNumber(self):
    	result = self.number.checkNumber(7)
    	self.assertEqual(result, 'Happy number')

    def testIf130IsHappyNumber(self):
    	result = self.number.checkNumber(130)
    	self.assertEqual(result, 'Happy number')

    def testIf2IsSadNumber(self):
    	result = self.number.checkNumber(2)
    	self.assertEqual(result, 'Sad number')
    
    def testIf3IsSadNumber(self):
    	result = self.number.checkNumber(3)
    	self.assertEqual(result, 'Sad number')

if __name__ == '__main__':
	unittest.main()