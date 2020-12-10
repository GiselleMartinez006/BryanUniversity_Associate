class Item {
    constructor(name, price, discount){
        this.name = name, 
        this.price = price ? price : null, 
        this.discount = discount ? discount : null
        }
}


class Checkout {
    constructor() {
        this.listItems = []
        this.currentTotal = 0
        
    }
    printCart = () => ("Checkout Cart: " + JSON.stringify(this.listItems) + ", Current Value: " + this.currentTotal)
    
    addItem = (name, price, discount) => { 
    this.listItems = [...this.listItems, new Item(name, price, discount)]
    return this.listItems
   }
   applyDiscounts = () => {

    // console.log(this.listItems)
        for (let i = 0; i < this.listItems.length ; i++){
            console.log("Item: ", this.listItems[i])
            if (this.listItems[i].discount){ 

                this.listItems[i].price = this.listItems[i].price - (this.listItems[i].price * this.listItems[i].discount)
                this.listItems[i].discount = null
            } 
        }
    console.log("Applied Discounts: ",this.listItems)
   }

   calculateTotal = () => {
       var totalCount = this.currentTotal
       
       for (let i = 0; i < this.listItems.length ; i++){
        // console.log("Item: ", this.listItems[i])
       
        if (this.listItems[i].price && !this.listItems[i].discount){ 
            totalCount += this.listItems[i].price
            this.currentTotal = totalCount
            // this.listItems.splice(i, 1)
            
            
        } else if (!this.listItems[i].price) {
            console.log("The item: '" + this.listItems[i].name + "' does not have a price and will not be counted on sum. Make sure to get its price next time!")
        } else if (this.listItems[i].discount){
            console.log("The item: '" + this.listItems[i].name + "' still has unapplied discounts. Items with unapplied discounts can not be counted in total... please wait a moment while we apply your discounts!")
            this.applyDiscounts()
            this.calculateTotal()
        } else {
            console.log("red", this.listItems[i])
        }
    }
    this.clearCart()
    console.log(this.printCart())



   }
   clearCart = () => {
        console.log("clearing your cart...")
        var list = []

        this.listItems.forEach((item, index) =>  (!item.price || item.discount? list.push(item):  console.log("")))
        
    
    this.listItems = list
}
}

/*function Checkout (){

function addItem(item):
        this.listItems.append(item)
        ######print("Updated list: ",Checkout.listItems)
        
        
        
    def addPrice(self, name, price):
        if name in Checkout.listItems:
            index = Checkout.listItems.index(name)
            # print(index)
            Checkout.listItems[index].append(price)
           ######## print("Updated list: ",Checkout.listItems)
        
    

return {listItems: [], currentValue: 0, }

}*/


// class Checkout:
//     listItems = []
//     print(listItems)
  
//     def __init__(self):
//         pass
    
//     def addItem(self, item):
//         Checkout.listItems.append(item)
//         ######print("Updated list: ",Checkout.listItems)
        
        
        
//     def addPrice(self, name, price):
//         if name in Checkout.listItems:
//             index = Checkout.listItems.index(name)
//             # print(index)
//             Checkout.listItems[index].append(price)
//            ######## print("Updated list: ",Checkout.listItems)
        
    
//     def currentTotalCounter(self):
//         # print(Checkout.listItems, "current list for total count super.py")
//         totalCount = 0;
        
//         for item in Checkout.listItems:
//             if len(item) == 2:
//                 num = item[1]
//                 totalCount += num
                
//             if len(item) < 2:
//                 print("The Item '" + item[0] + "' has NOT been given a price and will not be counted for value count.")
//             elif len(item) > 2 :
//                 print("Make sure to apply All discounts before trying to checkout! '"+ item[0]+ "' still has some discounts waiting for you!")
            
                
//         Checkout.currentValue = totalCount
//         # print("Current Value: " + str(Checkout.currentValue) + "blue")
        
//         # Checkout.clearList()
        
    
                
                
//     def clearList():
//         for item in Checkout.listItems:
//             if len(item) == 2:
//                 index = Checkout.listItems.index(item)
//                 # print(index)
//                 del Checkout.listItems[index]
                    
//             if len(item) < 2:
//                 print("ALERT: The Item '" + item[0] + "' has NOT been given a price and will not be counted for value count.")
//             elif len(item) > 2 :
//                 print("ALERT: Make sure to apply All discounts before trying to checkout!")
            
        
        
//     def addDiscounts(self,name, discount):
//         print(name)
//         print(discount)
//         if name in Checkout.listItems:
//             index = Checkout.listItems.index(name)
//             print(index)
//             Checkout.listItems[index].append(discount)
//         print("Updated list: ",Checkout.listItems)
        
//     def applyDiscounts(self):
//         for item in Checkout.listItems:
//             # print(len(item))
//             if len(item) > 2:
//                 # print(item[2], item[2][0], item[2][1])
//                 # print(item[1] - ( item[1] * item[2][0]))
//                 item[1] = item[1] - ( item[1] * item[2][0])
//                 # print(item)
//                 del item[2]
//                 # print(item)
//         print("Updated list: ",Checkout.listItems)
// # self.cathegory = cathegory
//         # self.name = name
//         # self.shelf = shelf

module.exports = Checkout