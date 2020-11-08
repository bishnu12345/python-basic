 # def displayMenu():
#     print('0.Quit')
#     print('1.Add two numbers')
#     print('2.Subtract two numbers')
#     print('3.Multiply two numbers')
#     print('4.Divide two numbers')


def calculate(num1,num2,operator):
    result = 0
    if operator=='+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    if operator == '/':
        result = num1 / num2
    return result

num1=int(input('Enter first number'))
num2= int(input('Enter second number'))
operator=input('Enter operator')
result = calculate(num1,num2,operator)
print(result)



# displayMenu()
# choice = int(input('Your Choice'))
# while choice!=0:
#     if choice==1:
#         num1 = int(input("Enter first number"))
#         num2 = int(input("Enter second number"))
#         sum = num1 + num2
#         print('The sum of {} and {} is {}'.format(num1,num2,sum))
#
#     elif choice==2:
#         num1 = int(input("Enter first number"))
#         num2 = int(input("Enter second number"))
#         subtract = num1 - num2
#         print('The difference of {} and {} is {}'.format(num1, num2, subtract))
#
#     elif choice==3:
#         num1 = int(input("Enter first number"))
#         num2 = int(input("Enter second number"))
#         product = num1*num2
#         print('The product of {} and {} is {}'.format(num1, num2, product))
#
#     elif choice==4:
#         num1 = int(input("Enter first number"))
#         num2 = int(input("Enter second number"))
#         division= num1/num2
#         print('{} divided by {} is {}'.format(num1, num2, division))
#
#     displayMenu()
#     choice = int(input('Your Choice'))

#print('Thank You')

