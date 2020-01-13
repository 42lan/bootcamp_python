import sys

def usage():
	print ("Usage: python operations.py")
	print ("Example:")
	print ("\tpython operations.py 10 3")

def elementary_math(a = None, b = None):
	"""
	This program that prints the results of the four elementary mathematical
	operations of arithmetic (addition, subtraction,)multiplication, division)
	and the modulo operation.
	"""
	if (a == None and b == None):
		print (usage())
		exit()
	print ("Sum:\t\t", a + b)
	print ("Difference:\t", a - b)
	print ("Product:\t", a * b)
	if (b == 0):
		print ("ERROR (dib by zero)")
	else:
		print ("Quotient:\t", a / b)
	if (b == 0):
		print ("ERROR (modulo by zero)")
	else:
		print ("Remainder:\t", a % b)

print (elementary_math())
