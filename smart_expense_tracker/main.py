import sqlite3

# Connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    note TEXT
)
""")
conn.commit()

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    cursor.execute(
        "INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
        (date, category, amount, note)
    )
    conn.commit()
    print("✅ Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\n📌 All Expenses:")
    for row in rows:
        print(row)

def category_summary():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)
    rows = cursor.fetchall()

    print("\n📊 Category-wise Summary:")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")

def main():
    while True:
        print("\n====== Smart Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()