print ("helo from snowball")
print ("a print from pycharm")



#import sys
#sys.stdin = open('in.txt','r')
#sys.stdout= open('out.txt','w')

turn = 1
stones = 7
running = True
while True:
    print("#stones:",stones,"     player",turn)
    choice = int(input("enter your choice: "))
    if choice==1:
        stones -=1
    if choice==2:
        stones -=2
    if stones<=0:
        print("player",turn,"win the game")
        running = False
    turn = 3- turn
