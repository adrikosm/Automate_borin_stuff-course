import shelve

shelveFile = shelve.open('mydata')
shelveFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']

print(shelveFile['cats'])

shelveFile.close()

hello_file = open('hello.txt', 'r+')

print(hello_file.read())

hello_file.close()
