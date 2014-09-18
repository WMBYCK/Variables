# William Craddock
# 17-09-14
# Class Exercises - Revision Exercise - 3 & 4

print("Enter two integers the second will be divided by the first")
print()
input_number = int(input("Please enter the first number: "))
input_number1 = int(input("Please enter the second number: "))
answer = input_number // input_number1
remainder = input_number % input_number1
print()
print(" {0} / {1} = {2} remainder {3}".format(input_number,input_number1,answer,remainder))
