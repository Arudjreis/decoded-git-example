# Print out numbers 1 to 100
# For numbers evenly divisible by 3, print "Fizz" instead
# For numbers evenly divisible by 5, print "Buzz" instead
# For numbers evenly divisible by 15, print "FIzzBuzz" instead

for number in range(101):

    if (number % 15 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)

