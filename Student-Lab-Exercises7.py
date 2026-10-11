userInput= int(input("Enter a number: "))
if userInput % 3 == 0 and userInput % 5 == 0:
    print("FizzBuzz")
elif userInput %5 == 0:
    print("Buzz")
elif userInput % 3 == 0 :
    print("Fizz")
else:
    print(userInput)