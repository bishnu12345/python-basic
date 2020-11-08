#WAP to display follow pattern
# ******
# ****
# **
# *

# length = int(input("Enter number of stars"))
# for i in range(0, length, 2):
#     for j in range(length, i, -1):
#         print("*", end="")
#     print()


#WAP to display follow pattern
# 1
# 121
# 12321
# 1234321
# 123454321

# big_number = int(input('Enter biggest number: '))
# for i in range(0,big_number+1):
#     for j in range(1,i+1):
#         print(j,end='')
#         for k in range(j,1,-1):
#             print(k-1,end='')
#
#     print()


#WAP to display follow pattern
                # KATHMANDU
                #  ATHMAND
                #   THMAN
                #    HMA
                #     M

str='KATHMANDU'
length= len(str)
for i in range(0,int(length/2)):
    for j in range(0,int(length/2)):
        for k in range(length-1,int(length/2)):
            print(i*' '+str[j:k])
print()

