"""
Module implementing a progress bar similar to tqdm.
"""

import sys
import shutil


def ft_tqdm(lst: range) -> None:
    """
    Create a progress bar for iterables.

    Args:
        lst (range): Range object to iterate over

    Yields:
        Current item in the range
    """
    total = len(lst)
    terminal_width = shutil.get_terminal_size().columns
    bar_length = min(50, terminal_width - 30)

    for i, item in enumerate(lst, 1):
        percentage = (i / total) * 100
        filled_length = int(bar_length * i // total)
        bar = ('=' * (filled_length - 1) + '>' +
               ' ' * (bar_length - filled_length))

        output = f"\r{percentage:3.0f}%|[{bar}]| {i}/{total}"
        sys.stdout.write(output)
        sys.stdout.flush()

        yield item


def main():
    """Test the progress bar implementation."""
    from time import sleep

    print("Testing ft_tqdm:")
    for elem in ft_tqdm(range(100)):
        sleep(0.1)
    print()


if __name__ == "__main__":
    main()
