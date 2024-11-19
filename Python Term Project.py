import json

class BudgetManager:
    def __init__(self):
        self.income = 0.0
        self.expenses = {}
    
    def add_income(self, source, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Income must be a positive number.")
            self.income += amount
            print(f"Income from {source} of ${amount:.2f} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def add_expense(self, category, description, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Expense amount must be a positive number.")
            if category not in self.expenses:
                self.expenses[category] = []
            self.expenses[category].append({"description": description, "amount": amount})
            print(f"Expense of ${amount:.2f} for {description} added to {category}.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def view_summary(self):
        print("\n---- Financial Summary ----")
        print(f"Total Income: ${self.income:.2f}")
        print("Total Expenses:")
        
        total_expenses = 0.0
        for category, items in self.expenses.items():
            category_total = sum(item['amount'] for item in items)
            total_expenses += category_total
            print(f"  - {category}: ${category_total:.2f}")
        
        balance = self.income - total_expenses
        print(f"Balance: ${balance:.2f}")
        
        if self.income > 0:
            print("\nSpending Breakdown:")
            for category, items in self.expenses.items():
                category_total = sum(item['amount'] for item in items)
                percentage = (category_total / total_expenses) * 100 if total_expenses > 0 else 0
                print(f"  - {category}: {percentage:.2f}%")
        print("---------------------------\n")
    
    def save_data(self, filename="budget_data.json"):
        try:
            data = {
                "income": self.income,
                "expenses": self.expenses
            }
            with open(filename, "w") as file:
                json.dump(data, file)
            print(f"Data saved to {filename}.")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            self.income = data.get("income", 0.0)
            self.expenses = data.get("expenses", {})
            print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except Exception as e:
            print(f"Error loading data: {e}")

def main():
    manager = BudgetManager()
    manager.load_data()

    while True:
        print("Welcome to the Budget Manager!")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            source = input("Enter the source of income: ")
            amount = input("Enter the amount: ")
            manager.add_income(source, amount)
        elif choice == "2":
            category = input("Enter the expense category: ")
            description = input("Enter the description of the expense: ")
            amount = input("Enter the amount: ")
            manager.add_expense(category, description, amount)
        elif choice == "3":
            manager.view_summary()
        elif choice == "4":
            manager.save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
