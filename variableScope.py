fullmarks=100

def display_full_marks():
    #local variables
        fullmarks=75
        print(fullmarks)
        num1=5

display_full_marks() #Function Call
print("Outside", fullmarks)
print(num1) #error occured because num1 is a local variable inside the function only
