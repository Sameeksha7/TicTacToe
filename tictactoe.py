import random
bo = {'t-L': ' ', 't-M': ' ', 't-R': ' ', 'm-L': ' ', 'm-M': ' ', 'm-R': ' ', 'b-L': ' ', 'b-M': ' ', 'b-R': ' '}
m=['t-M','t-L','t-R','m-L','m-M','m-R','b-L','b-M','b-R']
c=1
print("Welcome to tic tac toe!")
print("Do you want X or 0 ?")
user=input()
print("The computer will go first")
while(c==1):
  def printBoard(board):
    print(board['t-L'] + '|' + board['t-M'] + '|' + board['t-R'])
    print('-+-+-')
    print(board['m-L'] + '|' + board['m-M'] + '|' + board['m-R'])
    print('-+-+-')
    print(board['b-L'] + '|' + board['b-M'] + '|' + board['b-R'])

  if(user=='X'):
    chance = '0'
  else:
    chance='X'
  count=0
  for i in range(9):
     printBoard(bo)
     if(chance==user):    
       print('What is your next move?')
       move = input()
       bo[move] = chance
       m.remove(move)
     else:
       move=m[random.randint(0, len(m) - 1)]
       bo[move]=chance
       m.remove(move)
     if(chance=='X'):
         chance='0'
     else:
         chance='X'
     if(bo['t-L']==bo['t-M']==bo['t-R']=='X' or bo['m-L']==bo['m-M']==bo['m-R']=='X' or bo['b-L']==bo['b-M']==bo['b-R']=='X' or bo['t-L']==bo['m-L']==bo['b-L']=='X' or bo['t-M']==bo['m-M']==bo['b-M']=='X' or bo['t-R']==bo['m-R']==bo['b-R']=='X' or bo['t-L']==bo['m-M']==bo['b-R']=='X'or bo['t-R']==bo['m-M']==bo['b-L']=='X'):
       count=1
       break
     if(bo['t-L']==bo['t-M']==bo['t-R']=='0' or bo['m-L']==bo['m-M']==bo['m-R']=='0' or bo['b-L']==bo['b-M']==bo['b-R']=='0' or bo['t-L']==bo['m-L']==bo['b-L']=='0' or bo['t-M']==bo['m-M']==bo['b-M']=='0' or bo['t-R']==bo['m-R']==bo['b-R']=='0' or bo['t-L']==bo['m-M']==bo['b-R']=='0'or bo['t-R']==bo['m-M']==bo['b-L']=='0'):
       count=2
       break
  printBoard(bo)
  if(count==1 and user=='X'):
    print("You win")
  elif(count==1 and user=='0'):
    print("Computer has beaten you!you lose")
  elif(count==2 and user=='0'):
    print("You win")
  elif(count==2 and user=='X'):
    print("computer has beaten you!you lose")
  else:
    print("Draw")
  print("Do you want to play again")
  ans=input()
  if ans=='yes':
    c=1
    bo = {'t-L': ' ', 't-M': ' ', 't-R': ' ', 'm-L': ' ', 'm-M': ' ', 'm-R': ' ', 'b-L': ' ', 'b-M': ' ', 'b-R': ' '}
    
    
  else:
    c=0
    
