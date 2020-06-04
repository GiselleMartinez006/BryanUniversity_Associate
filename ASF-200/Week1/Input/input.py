# Step 2: Get user input
# In your Week 1 folder, create a folder called ‘Input.’ 
# Create an input.py file
# The message.py file should ask a user their “city” and “zip code”
# In the input.py file, write a code that displays user input message.
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(
    0, 'c:\\Users\\17865\\dev\\BryanUniversity_Associate\\ASF-200\\week1\\print')
# from week1.print.message import city, zipcode
from message import city, zipcode
print("userCity: "+city + " " + "userZipcode: " + zipcode)
