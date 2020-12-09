# In the supermarket.py file, 
# write a code that should achieve above tests through failing test,
# production test and the refractor test.

# , cathegory, name, shelf
class Checkout:
    listItems = []
    print(listItems)
  
    def __init__(self):
        pass
    
    def addItem(self, item):
        Checkout.listItems.append(item)
        ######print("Updated list: ",Checkout.listItems)
        
        
        
    def addPrice(self, name, price):
        if name in Checkout.listItems:
            index = Checkout.listItems.index(name)
            # print(index)
            Checkout.listItems[index].append(price)
           ######## print("Updated list: ",Checkout.listItems)
        
    
    def currentTotalCounter(self):
        # print(Checkout.listItems, "current list for total count super.py")
        totalCount = 0;
        
        for item in Checkout.listItems:
            if len(item) == 2:
                num = item[1]
                totalCount += num
                
            if len(item) < 2:
                print("The Item '" + item[0] + "' has NOT been given a price and will not be counted for value count.")
            elif len(item) > 2 :
                print("Make sure to apply All discounts before trying to checkout! '"+ item[0]+ "' still has some discounts waiting for you!")
            
                
        Checkout.currentValue = totalCount
        # print("Current Value: " + str(Checkout.currentValue) + "blue")
        
        # Checkout.clearList()
        
    
                
                
    def clearList():
        for item in Checkout.listItems:
            if len(item) == 2:
                index = Checkout.listItems.index(item)
                # print(index)
                del Checkout.listItems[index]
                    
            if len(item) < 2:
                print("ALERT: The Item '" + item[0] + "' has NOT been given a price and will not be counted for value count.")
            elif len(item) > 2 :
                print("ALERT: Make sure to apply All discounts before trying to checkout!")
            
        
        
    def addDiscounts(self,name, discount):
        print(name)
        print(discount)
        if name in Checkout.listItems:
            index = Checkout.listItems.index(name)
            print(index)
            Checkout.listItems[index].append(discount)
        print("Updated list: ",Checkout.listItems)
        
    def applyDiscounts(self):
        for item in Checkout.listItems:
            # print(len(item))
            if len(item) > 2:
                # print(item[2], item[2][0], item[2][1])
                # print(item[1] - ( item[1] * item[2][0]))
                item[1] = item[1] - ( item[1] * item[2][0])
                # print(item)
                del item[2]
                # print(item)
        print("Updated list: ",Checkout.listItems)
# self.cathegory = cathegory
        # self.name = name
        # self.shelf = shelf
