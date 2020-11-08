 # fruits=['Apple','Banana','Mango']
# for fruit in fruits:
#     print(fruit)

# #Print name 10 times
# name='Apoorba'
# for i in range(1,11):
#     # print(name) #prints every name in new line
#     print(name,end=',') #prints horizontally
#     #print(name,end=' ')
#

#Sum and average of numbers fron 1 to 5
# total = 0
# average = 0
# llimit= int(input("Enter Lower Limit"))
# ulimit= int(input("Enter Upper Limit"))
# count= ulimit - llimit + 1
#
# for i in range(llimit,ulimit+1):
#     total+=i
#
# average=total/count
# print("The sum of the numbers is {}".format(total))
# print("The average of the numbers is {}".format(average))


#Print a Sequence 2,4,6,8,10
# sequence=2
# for i in range(0,5):
#     print(sequence,end=' ')
#     sequence+=2
#
# print('\n')
#
# for i in range(2,11,2):
#     print(i,end=',')

#Find factorial of integer
factorial = 1
number= int(input('Enter a number'))

for i in range(1,number+1):
    factorial = factorial * i;

print('The factorial of {} is {}'.format(number,factorial))

