# enum class and display individual member and their names.

# Expected Output:

# Afghanistan = 93
# Albania = 355
# Algeria = 213
# Andorra = 376
# Angola = 244
# Antarctica = 672

from enum import Enum

class countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for country in countries: 
    print(country.name + " = " + str(country.value))
