from numbers import *
def gcd(n1, n2):
  if n2 == 0:
    if n1 == 0:
      raise ArithmeticError( "gcd(0,0) does not exist" )
    return n1
  else: 
    return gcd(n2, n1 % n2)


class Rational( Number ) :
	def __init__( self, num, denom = 1) :
		self. num = num
		self. denom = denom
		self. normalize()
	def normalize(self) :
		i = gcd(self. num, self. denom)
		if i != 1:
			self. num = self. num // i
			self. denom = self. denom // i
		if self. denom <= 0:
			raise ArithmeticError("denom is less than 0")
		return self. num // self. denom
  
	def __repr__( self ):
  		if self. denom == 1:
  			return '{}'. format(self. num)
  		return '{} / {}'. format(self. num, self. denom)
  
	def __neg__( self ) :
		return Rational(-self. num, self. denom)

	def __add__( self, other ) :
		if not isinstance(other, Rational):
			other = Rational(self.num*other.denom + self.denom*other.num,self.denom*other.denom)
		denom = self.denom * other.denom
		num = self.num * other.denom + self.denom * other.num
		return Rational(num, denom)


	def __sub__( self, other ) :
		if not isinstance(other, Rational):
			other = Rational(other , 1)
		denom = self.denom * other.denom
		num = self.num * other.denom - self.denom * other.num
		return Rational(num, denom)

	def __radd__( self, other ) :
  		answer = self+other
  		answer.normalize()
  		return answer


	def __rsub__( self, other ) :
  		if not isinstance(other, Rational):
  			other = Rational(other * self.denom - self.num, self.denom)
  		denom = self.denom * other.denom
  		num = self.num * other.num - self.num * other.denom
  		return Rational(num, denom)



	def __mul__( self, other ) :
		if not isinstance(other, Rational):
			other = Rational(other*self.num, self.denom)
		denom2 = self.denom
		num2 = self.num
		denom3 = other.denom
		num3 = other.num
		return Rational(num2*num3, denom2*denom3)

	def __truediv__( self, other ) :
		if isinstance(other,Rational):
			return Rational(self.num * other.denom , self.denom*other.num)
		return Rational(self.num , other*self.denom)

	def __rmul__( self, other ) :
		if isinstance(other,Rational):
			other = Rational(other , 1)
		else:
			return Rational(self.num * other , self.denom)

	def __rtruediv__( self, other ) :
		if not isinstance(other, Rational):
			other = Rational(other , 1)
		answer = Rational(other.num*self.denom , other.denom*self.num)
		answer.normalize()
		return answer

	def __eq__( self, other ) :
		if (other.num == self.num) and (other.denom == self.denom) :
			return True
		else:
			return False
		
	def __ne__( self, other ) :
		if (other.num == self.num) and (other.denom == self.denom):
			return False
		else:
			return True

	def __lt__( self, other ) :
		if (other.num * self.denom > self.num * other.denom):
			return True
		else:
			return False

	def __gt__( self, other ) :
		if (other.num * self.denom < self.num * other.denom):
			return True
		else:
			return False
	def __le__( self, other ) :
		if (other.num * self.denom >= self.num * other.denom):
			return True
		else:
			return False
	def __ge__( self, other ) :
		if (other.num * self.denom <= self.num * other.denom):
			return True
		else:
			return False
