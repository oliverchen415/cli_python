import click
import string

alpha_list = string.ascii_letters

# Numbers corresponding to the ASCII letters
upper_list = [number for number in range(65,91)]
lower_list = [number for number in range(97,123)]

def letter_shift(letter, shift):
    """Shifts a letter by a given number

    Args:
        letter (String): Letter to shift
        shift (Int): A value to shift a letter by

    Returns:
        String: A new letter shifted by a given number
    """
    if letter not in alpha_list:
        return letter
    shift_letter = ord(letter) + shift
    if (shift_letter in upper_list or shift_letter in lower_list):
        return chr(shift_letter)
    elif (shift_letter > max(upper_list) or shift_letter > max(lower_list)):
        return chr(shift_letter - 26)
    else:
        return chr(shift_letter + 26)

@click.command()
@click.option('--sentence', prompt='Something to encrypt', help='Message to encrypt')
@click.option('--shift', '-s', prompt='Shift letters by how much?', type=int, help='Number of characters to shift', show_default=True)

def caesar(sentence, shift):
    """Encrypts a message using a Caesar cipher

    Args:
        sentence (String): A message to be encrypted
        shift (Int): A value to shift all letters by
    """
    shift_sent = [letter_shift(letter, shift) for letter in sentence]
    click.echo(''.join(shift_sent))

    # alternative method using translations
    # shift_alpha = alpha_list[shift:] + alpha_list[:shift]
    # new_trans = str.maketrans(alpha_list, shift_alpha)
    # click.echo(sentence.translate(new_trans))

if __name__ == '__main__':
    caesar()