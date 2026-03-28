import argparse

def get_greeting(name="World"):
    return f"Hello, {name}!"

def main():
    parser = argparse.ArgumentParser(description="A simple Hello World CLI.")
    parser.add_argument(
        "--name", 
        type=str, 
        default="GitHub World", 
        help="The name to greet (default: GitHub World)"
    )
    args = parser.parse_args()
    print(get_greeting(args.name))

if __name__ == "__main__":
    main()
