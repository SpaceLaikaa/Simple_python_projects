import random

secret_number = random.randint(1, 100)
guess = int(input("Guess the number: "))

if guess == secret_number:
   print("WoW u just guessed the number in first try, you had 1/100 chance. What a luck dude.")
else:
   if guess > secret_number:
       print("⬇️ Your guess is higher than the secret number.")
   else:
       print("⬆️ Your guess is lower than the secret number.")    

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("🎉 Yeah, you finally got it!")
        break
    elif guess > secret_number:
        print("⬇️ Your guess is higher than the secret number.")
    else:
        print("⬆️ Your guess is lower than the secret number.")
