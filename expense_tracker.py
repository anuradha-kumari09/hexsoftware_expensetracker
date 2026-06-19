print(" Expense Tracker")
expenses = []

while True:
    print("\n 1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4.Delete expense")
    print("5. Exit expense")
    
    choice = input("Choice: ").strip()
    
    if choice == '1':
        category = input("Category (Food/Travel/Shopping/Bills/Other):").strip().capitalize()
        name = input("Enter Expense Name: ").strip()
        amount = float(input("Enter Amount:"))
        
        expenses.append({"name": name,"category": category, "amount": amount})
        print(f"✅ Added: {name} —${amount:.2f} [{category}]")
        
    elif choice == '2':
        if not expenses:
            print("No expenses yet.")
        else:
            for i, e in enumerate(expenses,1):
                print(f"{i}. {e['name']} |{e['category']} | ${e['amount']:.2f}")
                
    elif choice == '3':
        total = sum(e['amount'] for e in expenses)
        print(f"Total: ${total:.2f} across {len(expenses)} expense(s)")
        
    elif choice == '4':
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['name']} —${e['amount']:.2f}")
            idx = int(input("Delete #: "))
        if 1 <= idx <= len(expenses):
            print(f" Deleted:{expenses.pop(idx-1)['name']}")
            
    elif choice == '5':
        print("Goodbye! ")
        break
    
    else:
        print("Invalid choice.")
    