from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

def main():
    filename = 'user_data.csv'
    
    while True:
        print("Welcome to the Malaysian Tax Input Program")
        print("1. Register")
        print("2. Login")
        print("3. View Tax Records")
        print("4. Exit")
        
        choice = input("Please choose an option: ")
        
        if choice == '1':
            user_id = input("Enter your ID: ")
            ic_number = input("Enter your IC number (12 digits): ")
            password = ic_number[-4:]
            if verify_user(ic_number, password):
                print("Registration successful!")
                print("Please login to continue.")
            else:
                print("Invalid IC number. Registration failed.")
                
        elif choice == '2':
            user_id = input("Enter your ID: ")
            ic_number = input("Enter your IC number (12 digits): ")
            password = input("Enter the last 4 digits of your IC as password: ")
            if verify_user(ic_number, password):
                print("Login successful!")
                income = float(input("Enter your annual income: RM "))
                tax_relief = float(input("Enter your total tax relief amount: RM "))
                tax_payable = calculate_tax(income, tax_relief)
                print(f"Your calculated tax payable is: RM {tax_payable}")
                data = {
                    'User ID': user_id,
                    'IC Number': ic_number,
                    'Password': password,
                    'Income': income,
                    'Tax Relief': tax_relief,
                    'Tax Payable': tax_payable
                }
                save_to_csv(data, filename)
            else:
                print("Invalid credentials. Login failed.")
                
        elif choice == '3':
            df = read_from_csv(filename)
            if df is not None:
                print(df)
            else:
                print("No tax records found.")
                
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
