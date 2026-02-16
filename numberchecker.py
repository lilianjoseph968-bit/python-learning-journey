#number checker game
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("even number detected")
else:
    print("odd number detected")

if num > 0:
    print("this is a positive number")
elif num < 0:
    print("this is a negative number")
else :
    print("this is a zero")


score = 0

print("Welcome to the Math Game!")
print("Type 'exit' to stop playing.\n")

while True:
    a = 5
    b = 3

    answer = input(f"What is {a} + {b}? ")

    if answer == "exit":
        break

    if int(answer) == a + b:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Game over!")
print("Your score:", score)

