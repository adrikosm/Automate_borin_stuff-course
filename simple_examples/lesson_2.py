import pyperclip
import random

for i in range(0, 10):
    print(str(random.randint(1, 100)), end=" ")

print("\n")

pyperclip.copy("Hello world")
print(pyperclip.paste())
