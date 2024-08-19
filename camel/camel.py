import re

def main():
    camelCase = input("camelCase: ")
    split(camelCase)


def split(text):
    custom = "_"
    split = re.sub(r'([a-z])([A-Z])', r'\1' + custom + r'\2', text)
    print(split.lower())

main()