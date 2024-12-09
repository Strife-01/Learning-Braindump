import re


COEFFICIENTS = [1, 2, 1]

"""
    Computes all the terms for the binomial theorem based on Pascal's Triangle
"""

def main():
    # Get the required formula and power
    (sign, power) = get_formula()
    
    # Create the coefficients
    coefficients = get_coefficients(sign, power)
    
    # Print formula
    print_formula(coefficients)
    

def get_formula():
    
    print("Formula of type (a sign b) power of number")
    sign = None
    power = None

    while True:
        sign = input("Choose between: - or +: ")
        if sign != "-" and sign != "+":
            continue
        else:
            break
    
    while True:
        power = input("Choose a power between: 2 - infinity: ")
        try:
            power = int(power)
        except:
            continue
        if power < 2:
            continue
        else:
            break
        
    print(f"(a {sign} b) ^ {power}")
    return (sign, power)


def get_coefficients(sign, power):
    global COEFFICIENTS
    if power == 2:
        return COEFFICIENTS if sign == '+' else [1, -2, 1]
    else:
        for _ in range(power - 2):
            prev_coef = COEFFICIENTS
            new_coef = [1]
            for i in range(len(prev_coef) - 1):
                new_coef.append(prev_coef[i] + prev_coef[i + 1])
            new_coef.append(1)
            COEFFICIENTS = new_coef
    
    if sign == '-':
        for i in range(len(COEFFICIENTS)):
            if (i % 2 == 1):
                COEFFICIENTS[i] *= -1

    return COEFFICIENTS


def print_formula(coefficients):
    main_power = coefficients[1] if coefficients[1] > 0 else -1 * coefficients[1]
    print(f"a^{main_power} + ", end="")
    for i in range(1, main_power):
        print(f"{coefficients[i]}*a^{main_power - i}b^{i} + ", end="")
    print(f"b^{main_power}")


if __name__ == "__main__":
    main()
