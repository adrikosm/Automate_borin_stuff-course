
myname = input("What is your name ")
print("nice to meet you," + myname)

print("size of your name: " + str(len(myname)))

while True:
    try:
        myage = int(input("What is your age "))
        break
    except ValueError:
        print("Give a number ")
        pass

print('you will be ' + str(int(myage) + 1) + ' in a year')
