
print('Guessing Game!')
print("I'm thinking about a number and you should guess it. Don't worry I'll help you.")
print("Hint: The number is between 1 and 100")
import random
x = random.randint(1, 100)
num = int(input("Can you guess my number? let's see: "))
i = 1
while num != x:
    if num < x:
        if (x - num) > 10:
            print("Your guess is way too low")
        else:
            print("Your guess is low but close!")
    else:
        if (num - x) > 10:
            print("Your guess is way too high")
        else:
            print("Your guess is high but close!")
    num = int(input("That was a wrong guess try another one: "))
    i += 1

print("I can't believe it! you did it🎉🎉")
print(f"You got it in {i} {'try' if i == 1 else 'tries'}! ")