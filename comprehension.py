numbers= [1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
for i in numbers:
    if(i%2==0):
        even_numbers.append(i)
print(even_numbers)

#generate list from existing list using comprehension
odd_numbers= [j for j in numbers if j%2!=0]
print(odd_numbers)


#generate new list using comprehension
gen_numbers=[i for i in range(1,11)]
print(gen_numbers)

