# Exercise 4
from math import pi

for i in range(2, 12):
    pi_number = "{:." + str(i) + "f}"
    print(pi_number.format(pi))

# Exercise 5
string = input()

max_word = ''
for word in string.split():
    if len(word) > len(max_word):
        max_word = word

print(max_word)
