
function Fizzbuzz (num){


return (num ? ( (num % 3 == 0 && num % 5 == 0) ?  "FizzBuzz" : 
              (num % 3 == 0 ) ? "Fizz" : 
              (num % 5 == 0 ) ? "Buzz" :
              num.toString())  : "I guess this is Fizzbuzz")

}

//Can I call FizzBuzz
var test_callingFizzbuzz = () => console.log(Fizzbuzz()) 
test_callingFizzbuzz() 


var test_passingNum = (num, expectedResult) => console.log(Fizzbuzz(num) === expectedResult ? expectedResult : "test Failed" )

//Get 1 when I pass in 1
test_passingNum(1, "1")
//Get 2 when I pass in 2
test_passingNum(2, "2")
//Get “Fizz” when I pass in 3
test_passingNum(3, "Fizz")
//Get “Buzz” when I pass in 5
test_passingNum(5, "Buzz")
//Get “Fizz” when I pass in 6 (a multiple of 3)
test_passingNum(6, "Fizz")
//Get “Buzz” wen I pass in 10 (a multiple of 5)
test_passingNum(10, "Buzz")
//Get “FizzBuzz” when I pass in 15 (a multiple of 3 and 5)
test_passingNum(15, "FizzBuzz")
    



