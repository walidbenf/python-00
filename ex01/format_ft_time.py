from datetime import datetime
import time


def format_time():
    seconds_since_epoch = time.time()

    formatted_seconds = f"{seconds_since_epoch:,.4f}"
    scientific_notation = f"{seconds_since_epoch:.2e}"

    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")

    print(
        f"Seconds since January 1, 1970: {formatted_seconds} "
        f"or {scientific_notation} in scientific notation"
    )
    print(formatted_date)


if __name__ == "__main__":
    format_time()
