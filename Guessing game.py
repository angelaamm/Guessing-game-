num=23
guess=0
guess_limit=5

guess_number=1
guess=int(input(f"Guess a number 1-100: "))
while guess_number<guess_limit:
    if guess !=num:
        guess_number+=1
        if guess>num:
            guess=int(input(f"{guess} too high. Guess again 1-100: "))
        else:
            guess=int(input(f"{guess} too low. Guess again 1-100: "))
    if guess==num:
        print(f"You win! you guessed it: {num}")
if guess!=num:
    print(f"You lose Guess was: {num}")