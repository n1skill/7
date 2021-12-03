# Exercise 1
s = input()
print(s.count("b"))

# Exercise 2
name = input("Имя: ")
if name[0].islower():
    print("Имя должно начинаться с большой буквы!")
for i in range(1, len(name)):
    if name[i].isupper():
        print("Имя должно начинаться с большой буквы, за которой маленькие!")
        break
for l in name:
    if l.isalpha():
        continue
    print("Имя может содержать только буквы!")

# Exercise 3
line = input()
sum = 0
for i in line:
    sum += ord(i)
print(sum)
