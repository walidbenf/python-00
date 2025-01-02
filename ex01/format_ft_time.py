from datetime import datetime
import time

def format_time():
    # Get current timestamp with decimals
    seconds_since_epoch = time.time()
    
    # Format timestamp with commas and scientific notation
    formatted_seconds = f"{seconds_since_epoch:,.4f}"
    scientific_notation = f"{seconds_since_epoch:.2e}"
    
    # Get current date and format it
    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")
    
    # Print results in exact format
    print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
    print(formatted_date)

if __name__ == "__main__":
    format_time()