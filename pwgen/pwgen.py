# import random
import secrets

import click

# * ASCII lists
upperCaseList = [chr(value) for value in range(65, 91)]
lowerCaseList = [chr(value) for value in range(97, 123)]
numeralsList = [chr(value) for value in range(48, 58)]
symbolsList = [chr(value) for value in range(33, 44)]

alphaNum = upperCaseList + lowerCaseList + numeralsList + symbolsList
anNoSymbols = upperCaseList + lowerCaseList + numeralsList

def pwgen(max_len, symbols=True):
    if (max_len < 4 and symbols == True) or (max_len < 3 and symbols == False):
        raise ValueError('Invalid password length, enter a valid length.')
    if symbols == True:
        pwStart = [secrets.choice(upperCaseList), secrets.choice(lowerCaseList), secrets.choice(numeralsList), secrets.choice(symbolsList)]
    else:
        pwStart = [secrets.choice(upperCaseList), secrets.choice(lowerCaseList), secrets.choice(numeralsList)]
    charRemain = max_len - len(pwStart)
    newAlphaNum = 0
    while newAlphaNum < charRemain:
        if symbols == True:
            pwStart += secrets.choice(alphaNum)
        else:
            pwStart += secrets.choice(anNoSymbols)
        newAlphaNum += 1
    secrets.SystemRandom().shuffle(pwStart)
    pwStart = ''.join(pwStart)
    return pwStart

@click.command()
@click.option('--symbols', '-s', type=bool, default=True,
              prompt='Use symbols? True/False',
              help='add or remove symbols from passwords, default is True')
@click.option('--length', type=int, prompt='Length of password')
def main(length, symbols):
    click.echo(pwgen(length, symbols))

if  __name__ == "__main__":
    main()
