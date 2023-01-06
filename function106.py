def addNumber(*number):
    sum = 0
    for num in number:
        sum = sum + num
    
    return sum
    
result = addNumber(10,20)
print("sum =",result)
result2 = addNumber(100,200,300,400,500)
print("sum2 =", result2)