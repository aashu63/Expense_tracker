import tkinter as tk
from tkinter import messagebox
import json
import os

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        
        self.expenses = {}
        self.load_expenses()

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        tk.Label(self.root, text="Expense Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Generate Report", command=self.generate_report).grid(row=3, column=0, columnspan=2)

        # Report Area
        self.report_area = tk.Text(self.root, height=15, width=50)
        self.report_area.grid(row=4, column=0, columnspan=2)

    def load_expenses(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)

    def save_expenses(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if amount and category:
            if category in self.expenses:
                self.expenses[category] += float(amount)
            else:
                self.expenses[category] = float(amount)
            self.save_expenses()
            messagebox.showinfo("Success", "Expense added successfully!")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both amount and category.")

    def generate_report(self):
        self.report_area.delete(1.0, tk.END)  # Clear previous report
        total = sum(self.expenses.values())
        self.report_area.insert(tk.END, "Summary Report\n")
        self.report_area.insert(tk.END, "=====================\n")
        for category, amount in self.expenses.items():
            self.report_area.insert(tk.END, f"{category}: ${amount:.2f}\n")
        self.report_area.insert(tk.END, f"Total Expenses: ${total:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
