# Guessing Number Game in Python
> **Description**: A fun number guessing game with try counter by Python!  
> Guess a secret number between 1 and 100 with smart hints and a perfect try counter.  
> Made by @Kosarizarei from Azerbaijan (November 16, 2025).

## Features
- Random number (1-100)
- Smart hints: "way too low/high" or "close!"
- Try counter with correct grammar ("1 try" / "X tries")
- Clean and beginner-friendly code

## How to Play
1. Run the script.
2. Guess the number.
3. Get hints until you win!

## Example
```text
Guessing Game!
I'm thinking of a number between 1 and 100. You have to guess it. Don't worry I'll help you
Can you guess my number? let's see: 50
Your guess is way too high
That was a wrong guess try another one: 25
Your guess is low but close!
I can't believe it! You did it!
You got it in 3 tries!
```
## Full Code (guessing_game.py)
```python
print('Guessing Game!')
print("I'm thinking of a number between 1 and 100. You have to guess it. Don't worry I'll help you")

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

print("I can't believe it! you did it!")
print(f"You got it in {i} {'try' if i == 1 else 'tries'}!")

```
