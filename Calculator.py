exitcode = "y"
while exitcode != "q":
    n1 = float(input("Enter the first number:"))
    n2 = float(input("Enter the second number:"))
    print(
        "0:Addition\n"
        "1:Subtraction\n"
        "2:Multiplication\n"
        "3:Division\n"
        "4:Integer Division\n"
        "5:Modulo division\n"
    )
    operation = int(input("Enter the operation you want to perform:(Note:Please enter integer)"))
    switch = {
        0: n1 + n2,
        1: n1 - n2,
        2: n1 * n2,
        3: n1 / n2,
        4: n1 // n2,
        5: n1 % n2,
    }
    print(switch.get(operation, "Invalid operator number."))
    exitcode = input("Do you want to continue?\n"
                     "If no press q\n"
                     "Yes then press other keys\n"
                     ":")
