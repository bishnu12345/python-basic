sentence = input('Enter a sentence: ')
length = len(sentence)
vowel = 0
for i in range(0,length):
    letter = sentence[i]
    if(letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u'):
        vowel+=1
print('The number of vowels is {}'.format(vowel))