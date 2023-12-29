'''
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec
'''

#Errors corrected

animal = "Lion" #Name Error of "Lion" not being defined due to lack of quotation marks.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #The first Logical Error was due to the f string not being included so this string was printed exactly how it was written. The second Logical Error was the order of the variables. It should be animal_type and then number_of_teeth.

print (full_spec) #Syntax Error because of missing parentheses.
