import random

class TinyValueError(Exception):
    def __init__(self,guess):
        self.guess = guess

class EnormousValueError(Exception):
    def __init__(self,guess):
        self.guess = guess

def main():

    num = random.randint(1,100)
    print("I will select a number from 1-100, and you have to guess it.")

    while True:
        try:
            inputVal = int(input("Enter a guess: "))
            if inputVal < num:
                raise TinyValueError(inputVal)
            elif inputVal > num:
                raise EnormousValueError(inputVal)
            break
        except TinyValueError as err:
            print("Your guess of ",err.guess," was too small.")
        except EnormousValueError as err:
            print("Your guess of ",err.guess," was too big.")

    print("You guessed it!")

main()
