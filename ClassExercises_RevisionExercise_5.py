# William Craddock
# 18-09-14
# Class Exercises - Revision Exercise - 5

print("Enter the dimensions of the fridge in cm")
print()
fridge_height = int(input("Enter the fridge's height: "))
fridge_width = int(input("Enter the fridge's width: "))
fridge_depth = int(input("Enter the fridge's depth: "))
print()
print("Enter the dimensions inside the lift in cm")
print()
lift_height = int(input("Enter the lift's height: "))
lift_width = int(input("Enter the lift's width: "))
lift_depth = int(input("Enter the lift's depth: "))
print()      
answerl = lift_height * lift_width * lift_depth
answerf = fridge_height * fridge_width * fridge_depth
answer = answerl - answerf
print()
print("There will be {0} cm squared left in the lift".format(answer))
