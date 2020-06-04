import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(
    0, 'c:\\Users\\17865\\dev\\BryanUniversity_Associate\\ASF-200\\week1\\print')
# from week1.print.message import city, zipcode
from message import city, zipcode
print("userCity: "+city + " " + "userZipcode: " + zipcode)
