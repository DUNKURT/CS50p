def main():
    list = {}
    while True:
        try:
            grocery = input().upper().strip()
            key = f"{len(list) + 1}"
            list[key] = grocery

            print(list)
        except EOFError:
            break

main()