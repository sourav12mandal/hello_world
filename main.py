import argparse
import sys
import time

def get_greeting(name="World"):
    return f"Hello, {name}!"

def animate_text(text, delay=0.05):
    """Prints text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Add a newline at the end

def main():
    parser = argparse.ArgumentParser(description="A simple Hello World CLI.")
    parser.add_argument(
        "--name", 
        type=str, 
        default="GitHub World", 
        help="The name to greet (default: GitHub World)"
    )
    args = parser.parse_args()
    
    greeting = get_greeting(args.name)
    animate_text(greeting)

if __name__ == "__main__":
    main()
