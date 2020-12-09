
# The supermarketcheckout.py file should be able to achieve following tests
# Can create an instance of the Checkout class
# Can add an item
# Can add an item price
# Can calculate the current total
# Can add multiple items and get correct total
# Can add discount rules
# Can apply discount rules to the total
# Exception is Thrown for Item Added without a Price

from supermarket import Checkout

print("_______________________________________________________")
# =============================================================================
# 
# # "sports", "ball", "5"
# def test_CheckoutAndCanAddItemAndPrice():
#     co1 = Checkout("item5", 555)
#     co2 = Checkout("item10", 101010)
#     # co = Checkout()
#     
#     # print(Checkout())
#     
# # def test_CalculateCurrentTotal():
# #     co = Checkout()
# #     co.currentTotal()
#     
# 
# test_CheckoutAndCanAddItemAndPrice()
# # test_CalculateCurrentTotal()
# =============================================================================
             

# Can create an instance of the Checkout class

def test_createCheckoutInstance(): 
    co = Checkout()
    print(co.listItems)
    
# Can add an item

def test_addItem(itemToTest):
    co = Checkout()
    co.addItem(itemToTest)
    
test_addItem(["name"])

# Can add an item price

def test_addPrice(itemToTest, priceToTest):
    co = Checkout()
    co.addPrice(itemToTest, priceToTest)
    # print(co.listItems)
    
test_addPrice(["name"], 5)

# Can calculate the current total

def test_currentTotal():
    co = Checkout()
    # print(co.listItems, "current Total")
    co.currentTotalCounter()
    print("Current Value: ",co.currentValue)
# test_currentTotal()

print("division: -------------------")

# Can add multiple items and get correct total
def test_multipleItemsAndTotalAgain():
    test_addItem(["red hat"])
    test_addItem(["blue iron"])
      
    
    test_addPrice(["blue iron"], 10)
    test_addPrice(["red hat"], 15)
    
    test_currentTotal()

test_multipleItemsAndTotalAgain()

# Can add discount rules
def test_addDiscounts(itemToTest, discountToTest):
    co = Checkout()
    co.addDiscounts(itemToTest, discountToTest)
    # print(co.listItems)
test_addDiscounts(["blue iron", 10], [0.15, "Special Sale Monday"])


# Can apply discount rules to the total

def test_applyDiscounts():
    co = Checkout()
    co.applyDiscounts()
    
test_applyDiscounts()
# test_currentTotal()


# Exception is Thrown for Item Added without a Price
def test_noPrice():
    test_addDiscounts(["blue iron", 8.5], [0.15, "Special Sale Monday"])
    test_addItem(["green ball"])  
    test_currentTotal()
    Checkout.clearList()
    
    # //passing it
    test_applyDiscounts()
    test_addPrice(["green ball"], 20)
    test_currentTotal()
    Checkout.clearList()
    
    
test_noPrice()