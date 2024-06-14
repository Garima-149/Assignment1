# program to make simple calculator
def switch():
  a = int(input("Enter first value: "))
  b = int(input("Enter second value: "))
  print("Press 1 for Addittion \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
  option = int(input("Enter your option: "))
  if (option == 1):
     result = a+b
     print("Addition : ", result)
  elif(option == 2):
     result = a-b
     print("Subtraction : ",result)
  elif (option == 3):
     result = a*b
     print("Multiplication : ", result)
  elif(option == 4):
     result = a/b
     print("Division : ",result)
  else:
     print("Invalid Value")
  
switch()