"""
Program to filter words from a string based on length criteria.
"""

import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words longer than specified length.
    Uses list comprehension and lambda function.
    """
    try:
        # Check argument count
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        # Get and validate arguments
        text = sys.argv[1]
        try:
            length = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Split string and filter words using list comprehension and lambda
        words = text.split()
        result = list(ft_filter(lambda x: len(x) > length, words))
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
