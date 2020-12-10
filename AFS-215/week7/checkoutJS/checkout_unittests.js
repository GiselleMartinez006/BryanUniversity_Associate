const Checkout = require("./checkout")

// Can create an instance of the Checkout class
function test_checkoutCall(){
    var checkout = new Checkout()
    console.log( checkout.printCart())
    return checkout
}

test_checkoutCall()
// Can add an item
function test_addItem(item){
    // console.log(items, "items")
  var checkout = new Checkout()
  checkout.addItem(item.name)
  console.log("listItems updated: ", checkout.listItems)
  return checkout
 }
 
 test_addItem({name:"red hat"})
 

// Can add an item price

function test_addPrice(item){
    //    console.log(items, "items")
     var checkout = new Checkout()
     checkout.addItem(item.name, item.price)
     console.log("listItems updated: ", checkout.listItems)
     return checkout
    }
    
    test_addPrice({name:"red hat", price: 5})

// Can calculate the current total
function test_currentTotal(){
   var checkout = test_addPrice({name:"red hat", price: 5})
   checkout.calculateTotal()
  
}

test_currentTotal()

// Can add multiple items and get correct total
function test_addItemS(...items){
    // console.log(items, "items")
  var checkout = new Checkout()
  items.forEach(item => checkout.addItem(item.name))
  console.log("listItems updated: ", checkout.listItems)
  return checkout
 }
 
 test_addItemS({name:"red hat"},{name: "blue hat"})

 function test_addPriceS(...items){
    //    console.log(items, "items")
     var checkout = new Checkout()
     items.forEach(item => checkout.addItem(item.name, item.price))
     console.log("listItems updated: ", checkout.listItems)
     return checkout
    }
    
    test_addPriceS({name:"red hat", price: 5},{name: "blue hat", price: 6})


    // Can add discount rules
function test_addDiscount(...items){
    //    console.log(items, "items")
     var checkout = new Checkout()
     items.forEach(item => checkout.addItem(item.name, item.price, item.discount))
    //  console.log("listItems updated: ", checkout.listItems)
     return checkout
    }
    
test_addDiscount({name:"red hat", price: 5, discount: 0.15},{name: "blue hat", price: 6, discount: 0.25})

// Can apply discount rules to the total
function test_applyDiscounts(){
        
    var checkout = test_addDiscount({name:"red hat", price: 5, discount: 0.15},{name: "blue hat", price: 6, discount: 0.25})
    // console.log(checkout, "test")
    checkout.applyDiscounts()
    }
    test_applyDiscounts()
// Exception is thrown for item added without a price

function test_checkoutExceptions(){
    var checkout = test_addDiscount({name:"red hat", price: 5, discount: 0.15},{name: "blue hat", price: 6, discount: 0.25}, {name:"green rabbit"})
    // checkout.applyDiscounts()
    checkout.calculateTotal()
}
test_checkoutExceptions()




