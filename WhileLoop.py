#print name 10 times
# count = 10
# while count>0:
#     print('Apoorba')
#     count-=1


WORD = 'DWIT'
count = 0
GUESS_ALLOWED: int = 10

while count<GUESS_ALLOWED:
    guess= input("Enter your guess: ")
    if(guess==WORD):
        print('Correct Answer')
        break
    else:
        count+=1
        print('Try Again')




