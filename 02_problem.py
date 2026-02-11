'''Write a program that:
Generates a random number between 1 and 100
Prints it
Repeats this 5 times using a loop'''
import random
print("5 Random number:")
for i in range (5):
    r=random.randint(1,100)
    print(r)