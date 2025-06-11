from calculator_logic import (
    add, subtract, multiply, divide,
    square_root, power, log_natural, log_base10,
    sin_degrees, cos_degrees, tan_degrees
)

def get_float_input(prompt):
    """Gets a float input from the user, with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the calculator CLI."""
    operations = {
        "1": {"name": "Add", "func": add, "args": 2},
        "2": {"name": "Subtract", "func": subtract, "args": 2},
        "3": {"name": "Multiply", "func": multiply, "args": 2},
        "4": {"name": "Divide", "func": divide, "args": 2},
        "5": {"name": "Square Root", "func": square_root, "args": 1},
        "6": {"name": "Power", "func": power, "args": 2},
        "7": {"name": "Natural Log (ln)", "func": log_natural, "args": 1},
        "8": {"name": "Log Base 10 (log)", "func": log_base10, "args": 1},
        "9": {"name": "Sine (degrees)", "func": sin_degrees, "args": 1},
        "10": {"name": "Cosine (degrees)", "func": cos_degrees, "args": 1},
        "11": {"name": "Tangent (degrees)", "func": tan_degrees, "args": 1},
    }

    while True:
        print("\nSelect operation:")
        for key, op in operations.items():
            print(f"  {key}. {op['name']}")
        print("  0. Exit")

        choice = input("Enter choice (0-11): ")

        if choice == "0":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        selected_op = operations[choice]
        op_name = selected_op["name"]
        op_func = selected_op["func"]
        num_args = selected_op["args"]

        print(f"\n--- {op_name} ---")
        args = []
        if num_args == 1:
            args.append(get_float_input("Enter number: "))
        elif num_args == 2:
            args.append(get_float_input("Enter first number: "))
            args.append(get_float_input("Enter second number: "))

        try:
            result = op_func(*args)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
