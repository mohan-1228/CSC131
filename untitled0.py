import random

class Card(object):
   def __init__(self,value):
       self._face = 0
       self._value = value

   def __str__(self):
       if self._face == True:
           output = str(self._value)
       else:
           output = "*"
       return output

   def __eq__(self,other):
       if type(self)!=type(other):
           output = False
       elif self._value == other._value:
           output = True
       else:
           output = False
       return output


class Deck(object):
   def __init__(self, pairs):
       self._pairs = pairs
       self._cards = []
       for cards in range(self._pairs):
           self._cards.append(Card(cards))
           self._cards.append(Card(cards))

   def shuffle(self):
       random.shuffle(self._cards)

   def deal(self,index):
       return self._cards[index]

   def cardsleft(self):
       return len(self._cards)

class Game(object):
   def __init__(self,rows,columns):
       self._rows = rows
       self._columns = columns
       self._cards = (rows*columns)//2
       self._deck = Deck(self._cards)
       self._quit = False
       self._turns = 0

   #deals the cards into a 2D list
   def populateBoard(self):
       k = 0
       self._board = []
       self._deck.shuffle()
       for i in range(self._rows):
           self._board.append([])
           for j in range(self._columns):
               self._board[i].append(self._deck.deal(k))
               k+=1

   #shows the cards on the board
   def displayBoard(self):
       output = ""
       for i in range(self._rows):
           for j in range(self._columns):
               output += (str(self._board[i][j]) + " ")
           output += "\n"
       print(output)

   #iterates through the cards to see if any are face down. if all pairs have been found, gameover
   def isGameOver(self):
       victory = True
       for i in range(self._rows):
           for j in range(self._columns):
               if self._board[i][j]._face == False:
                   victory = False
                   break
       if victory == True:
           print("You Win.")
       return victory

