import re

def main():
    text = input('Input: ')
    new = re.sub('[AaEeIiOoUu]',"",text)
    print(f"Output: {new}")


main()