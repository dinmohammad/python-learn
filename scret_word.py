scret_word = 'Gorib'
guess = ""
guess_count = 0
guess_limit= 3
out_of_guess = False

while guess != scret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Type Your Guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print('You Loss!')
else:
    print('You Win!')