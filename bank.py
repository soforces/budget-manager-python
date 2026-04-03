import csv  # Library to handle CSV file operations (like Excel)
from datetime import datetime  # Library to capture the current date and time
import os  # Library to check if a file exists on the system

# Constant for the filename
DATA_FILE = 'expenses.csv'


def add_expense(category, amount, description):
    """Saves expense data provided by the user into the CSV file."""

    # Capture current date and time in a readable format
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Organize data into a list (row) to keep it structured
    new_entry = [timestamp, category, amount, description]

    # Check if the file already exists to decide if we need headers
    file_exists = os.path.isfile(DATA_FILE)

    # Open file in 'a' (append) mode to add data without deleting old records
    # encoding='utf-8' ensures special characters are saved correctly
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write headers only if the file is being created for the first time
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

        # Write the actual expense data row
        writer.writerow(new_entry)

    print(f"\n✅ Success: {amount} USD added to {category}.")


def view_report():
    """Reads all expenses from the file and calculates the total."""

    # Safety check: If file doesn't exist, notify the user
    if not os.path.isfile(DATA_FILE):
        print("\n⚠️ Error: No expense records found yet.")
        return

    total_sum = 0
    print("\n" + "=" * 40)
    print("      CURRENT EXPENSE REPORT")
    print("=" * 40)

    # Open file in 'r' (read) mode
    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        # DictReader maps the information to the header names
        reader = csv.DictReader(file)

        for row in reader:
            # Display each row in a clean format
            print(f"📅 {row['Date']} | 📂 {row['Category']}: {row['Amount']} | 📝 {row['Description']}")

            # Convert the string 'Amount' to a float for mathematical calculation
            total_sum += float(row['Amount'])

    print("=" * 40)
    # Print the total sum formatted to 2 decimal places
    print(f"TOTAL SPENT: {total_sum:.2f}")
    print("=" * 40 + "\n")


def main():
    """Main loop to handle the user interface and menu logic."""

    while True:
        print("--- PERSONAL FINANCE TRACKER ---")
        print("1. Add New Expense")
        print("2. View Expense Report")
        print("3. Exit System")

        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            category = input("Category (e.g., Food, Rent): ")
            amount_input = input("Amount (numbers only): ")
            description = input("Short Description: ")

            try:
                # Basic error handling: check if the input is a valid number
                amount_float = float(amount_input)
                add_expense(category, amount_float, description)
            except ValueError:
                # Triggers if the user enters letters instead of numbers
                print("\n❌ ERROR: Please enter a valid numeric value for the amount!")

        elif choice == '2':
            view_report()

        elif choice == '3':
            print("\nData saved. Exiting system...")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")


# Entry point of the script
if __name__ == "__main__":
    main()