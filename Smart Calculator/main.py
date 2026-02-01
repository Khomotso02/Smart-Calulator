while True:
        print("Welcome to the Smart Calculator")
        print()

        print("Choose an operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print()

        try:
            choice = int(input("Enter your choice: "))
            if choice >=1 and choice <= 4:
                num_1 = float(input("Enter first number: "))
                num_2 = float(input("Enter second number: "))
                answer = 0

                if choice == 1 :
                        answer = num_1 + num_2

                elif choice == 2 :
                        answer = num_1 - num_2
                elif choice == 3 :
                        answer = num_1 * num_2
                elif choice == 4:
                        answer = num_1 / num_2
            else:
                print("Invalid choice. Try again")
                continue

            print(f"Result: {answer}")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

        except ValueError:
            print("Error: Please enter valid numbers")

        repeat = input("Do you want to try again? (yes/no): ").lower()
        if repeat != "yes":
            break
