# Usage of split method to accept multiple inputs from user
x1, x2 = input("Enter 2 programming languages").split()
print("First Programming language is: ", x1)
print("First Programming language is: ", x2)

y1, y2, y3 = input("Enter 3 cricketers name").split()
print("First cricketer is: ", y1)
print("Second cricketer is: ", y2)
print("Second cricketer is: ", y3)

# Python program showing
# how to take multiple input
# using List comprehension

# Taking 2 input values
x, y = [int(x) for x in input("Enter 2 values").split()]
print("First number is:", x)
print("Second number is:", y)

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)