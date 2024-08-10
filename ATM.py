# Initial balance
Balance = 10000

# Prompt user to insert card
print("Insert Your CARD")

# Predefined password
Pass = "tanaya"

# Prompt user to enter PIN
PIN = input("Enter PIN: ")

# Check if the entered PIN matches the predefined password
if PIN == Pass:
    # Loop until the user chooses to exit
    while True:
        # Display menu options
        print("\n1 == Balance\n2 == Withdraw\n3 == Deposit\n4 == Exit")

        # Try to get the user's option choice
        try:
            option = int(input("Enter the option: "))
        except ValueError:
            # Handle non-integer input
            print("Enter Valid Option")
            continue

        # Display balance
        if option == 1:
            print(f"Your balance is: {Balance}")

        # Withdraw amount
        elif option == 2:
            withdraw_amount = int(input("Enter withdraw amount: "))
            # Check if there are sufficient funds
            if withdraw_amount > Balance:
                print("Insufficient funds")
            else:
                Balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your balance is {Balance}")

        # Deposit amount
        elif option == 3:
            deposit_amount = int(input("Enter deposit amount: "))
            Balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your balance is {Balance}")

        # Exit the loop and end the program
        elif option == 4:
            print("Thank you for using the ATM")
            break

        # Handle invalid option input
        else:
            print("Enter a valid option")
# Handle incorrect PIN input
else:
    print("Wrong PIN")
