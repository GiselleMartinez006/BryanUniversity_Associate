
function Fizzbuzz (num){
console.log("I guess this is fizzbuzz")

return num ? num.toString() : num
}

//Can I call FizzBuzz
function callingFizzbuzz(){
Fizzbuzz() //should return no error 

}
callingFizzbuzz()

//Get �1� when I pass in 1
function test_passingNum(num){


console.log(Fizzbuzz(num))

}

test_passingNum(1)

//Get �2� when I pass in 2
test_passingNum(2)



