def main():
    Expression = input('Expressions: ').strip().lower()

    x_str, y, z_str = Expression.split()
    x = float(x_str)
    z = float(z_str)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        print(x / z)
    elif y == "%":
        print(x % z)
    elif y == "**":
        print(x ** z)
    else:
        print(x // z)

main()