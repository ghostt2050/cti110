run_program = "yes"

while run_program.lower() == "yes":
    try:
        number = int(input("Enter an integer: "))
        if number < 0:
            print("This program does not handle negative numbers.")
        else:
            for i in range(1, 13):
                print(f"{number} * {i} = {number * i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    run_program = input("\nWould you like to run the program again? ")

print("\nExiting program...")
