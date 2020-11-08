percentage = int(input("Enter your percentage: "))
if percentage>80:
    print("You have achieved Grade A")
else:
    print("You have failed")


#Ternary Operator
value="Distinction" if percentage>=80 else "Fail"
print(value)
