'''Create a module string_utils.py:
Function to count vowels
Function to reverse a string
Import it in another program and test both functions.'''
def count_vowel():
    count=0
    vowel=('a','e','i','o','u')
    user=input("Enter the sentences: ")
    for char in user:
        if char.lower() in vowel:
            count+=1
    print("No of vowel: ",count)
def reverse_string():
    user_reverse=input("Enter the word to reverse:")
    reversed=user_reverse[::-1]
    print(reversed)

count_vowel()
reverse_string()