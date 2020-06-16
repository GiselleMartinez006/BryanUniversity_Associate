# The tuple.py file should includes list of numbers in it:
# (1,2,3,4,5,6,7); 

# In the tuple.py file, write a program according to following specifications
#       Tuple 1 includes list of information of Robert
# o   (name, surname, birth year, favorite movie and year, profession, birthplace) = Robert 

#       Tuple 2 includes list of numbers in it
#       We call the value for [0] in tuple and for tuple 2 we call the value between 1 and 4
#       Run the code- It gives name Robert for first tuple while for second tuple it gives number (2,3 and 4)


Robert =("Robert", "Summers", "1996", "Warrior's Way 1997", "Massage Therapist", "City, California") 
nums = (1,2,3,4,5,6,7)

print("first tuple: ", Robert[0])
print("second tuple: ", nums[1:4])

