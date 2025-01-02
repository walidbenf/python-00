"""
Module for analyzing text character composition.
Counts upper/lowercase letters, punctuation, spaces and digits in text.
"""

import sys
import string


def count_characters(text: str) -> dict:
    """
    Count different types of characters in given text.

    Args:
        text (str): Input text to analyze

    Returns:
        dict: Contains counts for total chars, upper/lower letters,
              punctuation, spaces and digits
    """
    counts = {
        'total': len(text),
        'upper': sum(1 for c in text if c.isupper()),
        'lower': sum(1 for c in text if c.islower()),
        'punct': sum(1 for c in text if c in string.punctuation),
        'space': sum(1 for c in text if c == ' '),
        'digit': sum(1 for c in text if c.isdigit())
    }
    return counts


def main():
    """Main program entry point with error handling."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = input()

        counts = count_characters(text)
        print(f"The text contains {counts['total']} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punct']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")

    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()

# Testing the docstrings
# print(count_characters.__doc__)
# print(main.__doc__)