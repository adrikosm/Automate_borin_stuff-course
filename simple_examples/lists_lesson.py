spam_list = [['cat', 'bat', 'rat', 'elephant', 'dog'],
             [10, 20, 30, 40, 50]]

print(spam_list[0][4], end=" ")
print(spam_list[1][4])
print(spam_list[0][:2])  # slice
print(spam_list[1][:2])

spam_list[0].append("mouse")
print(spam_list[0])

spam_list[1].append(60)
print(spam_list[1])

animal = (list(spam_list[0][4]))
print(animal)

for i in range(len(spam_list[0])):
    spam_list[0][i] = spam_list[0][i].upper()

print(spam_list[0], "\n")

for i in range(len(spam_list[0])):
    print(f'index of {i} is: {spam_list[0][i]}', end=" ")
    print(spam_list[1][i])
