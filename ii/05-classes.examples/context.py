class Example:
    """Example class that demonstrate context management"""

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

if __name__ == '__main__':
    with Example() as e:
        print("Block")
