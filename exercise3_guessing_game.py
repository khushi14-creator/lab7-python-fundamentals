# Exercise 3 - Guessing Game (1 to 1000)
"""
Think of a number between 1 and 1000.
The computer will try to guess it using a binary search strategy.
You reply:
  'h' or 'higher'  -> your number is higher than the guess
  'l' or 'lower'   -> your number is lower than the guess
  'c' or 'correct' -> guess is correct
"""

LOW = 1
HIGH = 1000

print("Think of a number between 1 and 1000 (inclusive). I will try to guess it.")
input("Press Enter when you're ready...")

low = LOW
high = HIGH
rounds = 0

while low <= high:
    rounds += 1
    guess = (low + high) // 2
    # Use .format() instead of f-string
    print("My guess #{}: {}".format(rounds, guess))
    reply = input("Is your number (h)igher, (l)ower, or (c)orrect? ").strip().lower()

    if reply in ('c', 'correct'):
        print("Yay! I guessed your number {} in {} rounds!".format(guess, rounds))
        break
    elif reply in ('h', 'higher'):
        low = guess + 1
    elif reply in ('l', 'lower'):
        high = guess - 1
    else:
        print("Please reply with 'h', 'l', or 'c'. Let's try again.")
        rounds -= 1
        continue

else:
    print("Hmm, something went wrong — maybe the answers were inconsistent.")