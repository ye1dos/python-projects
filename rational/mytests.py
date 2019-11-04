from matrix import *
from vector import *
from rational import *

def tests():

	a = Matrix(Rational(1, 2), Rational(1, 5), Rational(1, 8), Rational(1, 16))
	b = Matrix(Rational(3, 2), Rational(1, 5), Rational(1, 5), Rational(1, 7))
	print("Matrix a is :")
	print(a)
	print("Matrix b is :")
	print(b)	
	c = a@b
	
	print("Multiplication\n")
	print(c)
	d = Matrix(Rational(1, 9), Rational(4, 9), Rational(7, 9), Rational(5, 2))
	
	print("\nCHECKING THE (m1 × m2) × m3 = m1 × (m2 × m3) \n")
	e = a@b
	f = c@d
	print("this is axb: ")
	print(e)
	print("this is bxc: ")
	print(f)
