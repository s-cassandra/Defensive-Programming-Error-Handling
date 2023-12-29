'''
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print "Welcome to the error program"
    print "\n"

    # Variables declaring the user's age, casting the str to an int, and printing the result
    age_Str == "24 years old" 
    age = int(age_Str) 
    print("I'm" + age + "years old.")

    # Variables declaring additional years and printing the total years of age
    years_from_now = "3"
    total_years = age + years_from_now

print "The total number of years:" + "answer_years"

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"
'''

#Errors corrected 
print ("Welcome to the error program") #This was a Syntax Error where the parentheses were missing.
print ("\n") #This was a Syntax Error and an Indentation Error because there were missing parentheses and no need for this element to be indented. Examples of where indentation is needed include, but are not limited to, if,elif, and else statement and loops (while and for).

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #age_Str was not defined due to == being used and not =, causing a Name Error.
age = int(age_Str) #there was a Value Error because the string assocaited with the variable age_Str consisted of both numbers and letters "24 years old". I fixed this by removing the "years old" part.
print(f"I'm {age} years old.") # Lines 9, 10, and 11 all had an Indentation Error because there were unnecessarily indented. Line 11 resulted in a Type Error because we cannot concatenate strings and integers. I fixed this by implementing an f string to include the age and removed the "+" symbols. 

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) #Lines 14 and 15 had Indentation Errors because they were unnecessarily indented. Line 15 had a Type Error because years_from_now did not have its data type changed to integer, resulting in Python attempting to concatenate a string and an integer.

print (f"The total number of years: {total_years}") #Syntax Error because of missing parentheses. Logical Error because even though this ran, it did not give the total number of years. This was fixed using an f string. Name Error because answer_years was not defined. I didn't understand why answer_years was used instead of total_years so I just changed it total_years.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12
total_months += 6
print (f"In 3 years and 6 months, I'll be {total_months} months old") #Syntax Error because of missing parentheses. Name Error because total was not defined. I replaced this with total_years. Type Error because you cannot concatenate strings and integers so I used an f string. Logical Error because total_months does not account for the additional 6 months so I updated total_months and added 6.
