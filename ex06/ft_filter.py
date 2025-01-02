def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return iter([item for item in iterable if bool(item)])
    return iter([item for item in iterable if function(item)])


def main():
    """Test ft_filter function."""
    # Test with function
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(ft_filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")

    # Test with None
    mixed = [0, 1, False, True, '', 'hello']
    truthy = list(ft_filter(None, mixed))
    print(f"Truthy values: {truthy}")

    # Print docstring
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
