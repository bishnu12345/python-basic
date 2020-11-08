#Hailstone numbers
#10,5,16,8,4,2,1,4,2,1
#if the number is even divide it by 2, if odd multiply by 3 and add 1

count = 0
first_num= 10
while count <10:
    print(first_num, end=',')
    if(first_num%2==0):
        first_num = int(first_num/2)
    else:
        first_num = (first_num * 3 ) + 1

    count+=1

print('\n')

#print 1,2,3,5,8,...upto 10th term
num1 = 1
num2 = 2
sum = 0
print('{},{}'.format(num1,num2),end=',')
for count in range(0,8):
    sum = num1 + num2
    print(sum,end=',')
    num1=num2
    num2=sum

print('\n')


#print 2,4,8,16,32,...upto 10th term

power=1
count = 10
while count > 0:
    number= 2**power
    print(number,end=',')
    power+=1
    count-=1

print('\n')


#print 2,8,18,32,...upto 10th term

for count in range(1,11):
    number = (count**2)*2
    print(number,end=',')

print('\n')


#print 2,2,4,6,10,...upto 10th term

count = 0
first_number = 2
second_number = 2
print('{},{}'.format(first_number,second_number),end=',')
while count < 8:
    sum = first_number + second_number
    print(sum,end=',')
    first_number = second_number
    second_number = sum
    count+=1

print('\n')

#print 1,4,9,...upto 10th term

for count in range(1,11):
    print(count**2,end=',')
    count+=1