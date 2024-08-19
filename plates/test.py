def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        # Check if there are digits and if the first digit is not '0'
        digits = [char for char in s if char.isdigit()]
        if digits and digits[0] == '0':
            return False
        
        # Ensure that no letters appear after the digits
        digits_started = False
        for char in s:
            if char.isdigit():
                digits_started = True
            elif digits_started and char.isalpha():
                return False
        
        return True
    else:
        return False


main()
