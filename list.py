fruits=['Apple','Banana','Grapes','Lemon','Mango']
print(fruits)
print(fruits[0:2])
print(fruits[-2])
print(fruits[2:])
print(fruits[::2])

new_fruits=fruits[:]
print(type(new_fruits))

new_fruits.append('Orange') #adds single element to the list
print(new_fruits)
print(new_fruits.count('Grapes'))
print(fruits.index('Lemon'))

new_fruits.remove('Banana') #removes multiple elements if the value is same
print(new_fruits)

del new_fruits[2] # deletes a particular element of the given index
print(new_fruits)

new_fruits.extend(['Pomegranate','Pear','Strawberry']) #add multiple elements to the list
print(new_fruits)

print(len(new_fruits))

print(sorted(new_fruits))

