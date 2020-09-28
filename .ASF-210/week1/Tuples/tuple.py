# The tuple.py file should be able to find the class wise roll number from a tuple-of-tuples.
# In the tuple.py file, write a code that displays the following output.
#  Expected Output:

# defaultdict(, {'VII': [1], 'V': [1, 2], 'VI': [1, 2, 3]})
#             ^ kind of guessed that "<class 'list'>" was expected before this comma. 
from collections import defaultdict
romanLetters = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

rollNumber = defaultdict(list)

for letter, num in romanLetters:
    print("letter", letter)
    print("num", num)
    rollNumber[letter].append(num)

print(rollNumber)