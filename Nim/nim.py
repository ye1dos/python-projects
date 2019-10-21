
import random
import time

class CantMove( Exception ) :

   def __init__( self, reason ) : 
      self. __reason = reason

   def __repr__( self ) :
      return "unable to find a move: {}". format( self.__reason )


class Nim :
   def __init__( self, startstate ) :
      self. state = startstate


   # Goal is to be unambiguous : 
   def __repr__(self):

      rep = ''
      for i in range(len(self.state)):
         rep = rep + "{} : {}\n" .format(i + 1, '1 ' * self.state[i])
      return rep

   # Return sum of all rows:
   def sum(self):
      res = 0
      for i in self.state: res += i
      return res

   # Return nimber (xor of all rows): 

   def nimber(self):
      res = 0
      for i in self.state: result ^= i
      return res

   def randommove( self ) :
      possiblemove = []

      for i in range(len(self.state)):
         if self.state[i] >= 1:
            possiblemove.append(i)

      if len(possiblemove) == 0:
         raise CantMove("no sticks left ")

      range1 = random.randrange(0, len(possiblemove))
      a = self.state[possiblemove[range1]]
      range2 = random.randrange(0, a)
      self.state[possiblemove[range1]] = range2   


   def removelastmorethantwo(self):
      summ = 0
      numb = []
      
      for i in range(len(self.state)):
         if self.state[i] > 1:
            numb.append(i)

         if self.state[i] == 1: summ += 1

      if len(numb) != 1:
         raise CantMove("more than one row has more than one stick")

      if summ % 2 == 0:
         self.state[numb[0]] = 1
      else:
         self.state[numb[0]] = 0


   def makenimberzero(self):
      for i in range(len(self.state)):
         if (self.state[i]^self.nimber()) < self.state[i]:
            self.state[i] ^= self.nimber()
            return

   def optimalmove(self):
      try:
         self.makenimberzero() 
         return
      except:
         self.randommove()

      try:
         self.removelastmorethantwo() 
         return
      except:
         pass

   def usermove(self):
      crow = 0
      stick = -1
      while crow == 0:
         try:
            row = int(input("Input the index of row: "))
            if row <= 0 or row > len(self.state) or self.state[row - 1] == 0: raise 
            crow = row
         except:
            print("Row is wrong.\nTry Again!\n")

      while stick == -1:
         try:
            ch = int(input(("Input sticks that will be left in {} row: ".format(crow))))
            if ch >= self.state[row - 1] or ch < 0 : raise 
            stick = ch
         except:
            print("Stick number isn't correct.\nTry again!\n")
      self.state[crow - 1] = stick



######################

def play( ) :
   st = Nim( [ 1, 2, 3, 4, 5, 6 ] )
   turn = "user"
   while st. sum( ) > 1 :
      if turn == "user" :
         print( "\n" )
         print( st )
         print( "hello, user, please make a move" )
         st. usermove( )
         turn = "computer"
      else :
         print( "\n" )
         print( st )
         print( "now i will make a move\n" )
         print( "thinking" )
         for r in range( 15 ) :
            print( ".", end = "", flush = True )
            time. sleep( 0.1 )
         print( "\n" )
         st. optimalmove( )
         turn = "user"
   print( "\n" )
   if turn == "user" :
      print( "you lost\n" )
   else :
      print( "you won\n" )
play()