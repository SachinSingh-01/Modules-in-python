'''Using __name__ Variable
Create a module that:
Prints "This is a module"
Uses if __name__ == "__main__": to print "Running directly"
Run it directly and then import it from another file to observe the difference.'''
print("This is a module")
if __name__ == "__main__":
    print("Running directly")
    