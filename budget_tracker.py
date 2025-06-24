print("💸 Welcome to Budget Tracker!")

balance = 0
transactions = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        amount = float(input("Enter income amount: ₦"))
        balance += amount
        transactions.append(f"Income: +₦{amount}")
        print(f"✅ Added ₦{amount}")
    elif choice == "2":
        amount = float(input("Enter expense amount: ₦"))
        balance -= amount
        transactions.append(f"Expense: -₦{amount}")
        print(f"❌ Spent ₦{amount}")
    elif choice == "3":
        print("\n📊 Budget Summary:")
        for t in transactions:
            print("-", t)
        print(f"\n💰 Current Balance: ₦{balance}")
    elif choice == "4":
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
