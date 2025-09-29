# Ask the user what there name is and then say hello to them

name = input ("Hello! My names Py. What's your name? ").strip().title()
# Asks the user for their name, 
# removes an spaces from the begining or end of their input, 
# and capitalizes their name

# -.strip() and .title() are similar to functions but are called "methods" and are basically 
#  like extra features that can be implemented 
# -.strip() removes any spaces from the begining and end of a string
# -.title() formats the string like a title (ie., it capitalizes the first letter of each word)
# the above line of code can also be written like this:  name = input("What is yout name? ")
#                                                        name = name.strip().title() 


firstname, lastname = name.split(" ")
#splits the user's name into first name and last name 

# the method .split uses the space that the user typed in between their first and last name to split the
# sting into two smaller strings that were then assigned to two different variables in order


print(f"Hello {firstname}, nice to meet you!")
# Says hello to the user with only their first name

# the above line of code uses an "f" symbol at the begining of the function argument
# the "f" turns the string argument into a "format string or f-string" which tells python to format 
# elements of ths string in a special way. 
# the above line of code can also be written like print("Hello " + firstname + ", nice to meet you!")