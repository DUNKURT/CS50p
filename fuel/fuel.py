def main():
    fuel = get_fuel("Fraction: ")
    print(f"{fuel}")
    

def get_fuel(prompt):
    while True:
        try:
            n = input(prompt)
            x, y = map(int, n.split("/"))
            if x >= 0 and y > 0 and x <= y:
                percent =  x / y * 100
                if percent >= 99:
                    return "F"
                elif percent <= 1:
                    return "E"
                else:
                    return f"{round(percent)}%"
        except (ValueError, ZeroDivisionError): 
            pass
        
main()