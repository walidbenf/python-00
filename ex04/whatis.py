import sys

try:
    # Check number of arguments
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    # Skip if no arguments provided
    if len(sys.argv) == 1:
        sys.exit(0)

    # Try to convert argument to integer
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Check if even or odd
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {str(e)}")
