def divisorGenerator(n):
    divisors = []
    # print(round(n/2))
    num = round(n/2+1)
    # print(num)
    for i in range(1,num):
        if n%i == 0: 
            # print(i)
            divisors.append(i)
    print(divisors)
    addingDivisors = 0;
    for i in divisors: 
        addingDivisors += i
    # print(addingDivisors)
    if addingDivisors == n: 
        strOfDivisors = str(divisors).split(", ")
        print(strOfDivisors )
        first = strOfDivisors[0].split("[")
        print("first", first)
        strOfDivisors[0] = first[len(first)-1]
        print(strOfDivisors)
        
        
        
        
        last = strOfDivisors[len(strOfDivisors)-1].split("]")
        print("last",last)
        strOfDivisors[len(strOfDivisors)-1] = last[0]
        print(strOfDivisors, "line 29")
        
        divisorsAddingStr = ""
        for i in strOfDivisors:
            if i == strOfDivisors[len(strOfDivisors)-1]:
                divisorsAddingStr += i
            else:
                divisorsAddingStr+= i+ " + "
        strListdivisors = ""
        for i in strOfDivisors:
            if i == strOfDivisors[len(strOfDivisors)-1]:
                strListdivisors += i
            else:
                strListdivisors += i+ ", "
        print(divisorsAddingStr)
        
        
        print("________________________")
        
        print("Divisors of " + str(n)+ " : " + strListdivisors)
        print("Sum of " + divisorsAddingStr + " = " + str(addingDivisors))
        print("Sum = Original Number")
        print(str(n)+" is Perfect Number")
        
    else:
        print("): not a perfect number! Try again!")
    
divisorGenerator(28)