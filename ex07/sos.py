"""
Program to encode text to Morse code.
Supports alphanumeric characters and spaces.
"""

import sys


def get_morse_dict():
    """
    Returns the Morse code dictionary.

    Returns:
        dict: Morse code mappings
    """
    return {
        ' ': '/',
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }


def encode_to_morse(text: str) -> str:
    """
    Encode text to Morse code.

    Args:
        text (str): Text to encode

    Returns:
        str: Morse code representation
    """
    morse_dict = get_morse_dict()
    try:
        return ' '.join(morse_dict[c.upper()] for c in text)
    except KeyError:
        raise AssertionError("the arguments are bad")


def main():
    """Main program entry point with error handling."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        result = encode_to_morse(sys.argv[1])
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
