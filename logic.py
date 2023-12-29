# Practical task: Write a program that displays a logical error

name = input("Please enter your name: ")
years_old = input("Please enter your age: ")
months_old = years_old * 12
print(f"Hello {years_old}! You are {name} years old. This is {months_old} in months.")

'''
Output:
The sentence will read incorrectly due to the following:
  1. years_old and name are in the wrong order in the print statement. Swap them and they will print correctly 
  2. months_old will print years_old 12 times because years_old is not recognised as an integer. Convert years_old to an integer 
     e.g. int(input("Please enter your age: ") and it will run correctly
'''
