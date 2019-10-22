import random
def askforanswer(c, a, b):
	inputstring = input( "question {}: please calculate {} times {} ".format( c, a, b ))
	try :
		answer = int(inputstring)
		return answer
	except ValueError:
		print("\nIt is not number\n")
		a = 111111;
		return a;

def main():
	count = 0
	q =111111
	while count != 5:
		a = random.randint(1,10)
		b = random.randint(1,10)
		c = a * b
		answer = askforanswer(count+1, a, b)
		if answer == c:
			count+= 1
			print("Correct")
		if answer != c and answer != q:
			count = 0
			print("Incorrect. Correct number is",c)
		if answer == q:
			count = 0
	print("You have passed the exam")