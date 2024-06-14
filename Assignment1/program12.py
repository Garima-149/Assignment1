#program to calculate sum of sum of digits of given number
def getSum(n): 
    
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
   
n = 34
print(getSum(n))