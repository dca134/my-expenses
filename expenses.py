import tkinter as tk
from tkinter import messagebox
import os

def load_expenses():
    """Uploading expenses from a file."""
    if not os.path.exists("expenses.txt"):
        return []
    with open("expenses.txt", "r") as file:
        return [line.strip().split(",") for line in file]

def save_expenses(expenses):
    """Saving expenses to a file."""
    with open("expenses.txt", "w") as file:
        for category, amount in expenses:
            file.write(f"{category},{amount}\n")

def add_expense():
    """Adding a new expense through the interface."""
    category = entry_category.get()
    amount = entry_amount.get()
    if not category or not amount:      #сhecking for eempty input
        messagebox.showerror("Error", "Enter the category and amount!")
        return
    try:
        amount = float(amount)      #checking that the sum is a number
        expenses.append([category, str(amount)])        #adding an expense to the list
        save_expenses(expenses)     #saving data to a file
        update_expense_list()       #updating the expense list
        entry_category.delete(0, tk.END)        #clearing the category input field
        entry_amount.delete(0, tk.END)      #clearing the amount entry field
        messagebox.showinfo("Success", "Expense added!")        #success message
    except ValueError:
        messagebox.showerror("Error", "The sum must be a number!")      #input error handling

#function to remove the expense
def delete_expense():
    """Deleting the selected expense."""
    selected = listbox_expenses.curselection()      #geetting the selected item
    if not selected:
        messagebox.showerror("Error", "Select the expense to delete!")
        return
    index = selected[0]     #index of the selected item
    del expenses[index]     #removing an item from the list
    save_expenses(expenses)     #saving changes to a file
    update_expense_list()       #updating the expence list
    messagebox.showinfo("Success", "The expense has been deleted!")     #success message

#Function for updating the expense list in the interface
def update_expense_list():
    """Updating the expense list in the interface."""
    listbox_expenses.delete(0, tk.END)      #Clearing the list in the interface
    for category, amount in expenses:
        listbox_expenses.insert(tk.END, f"{category}: {amount} €")      #adding new elements

#application interface
expenses = load_expenses()      #cost loading at program startup

root = tk.Tk()      #create the main window
root.title("My expenses")       #window title

#entering a category
label_category = tk.Label(root, text="Category:")
label_category.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_category = tk.Entry(root, width=20)
entry_category.grid(row=0, column=1, padx=10, pady=5)

#entering the amount
label_amount = tk.Label(root, text="The amount:")
label_amount.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_amount = tk.Entry(root, width=20)
entry_amount.grid(row=1, column=1, padx=10, pady=5)

#a button for adding expenses
btn_add = tk.Button(root, text="Add expense", command=add_expense)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

#list of expenses
label_list = tk.Label(root, text="List of expenses:")
label_list.grid(row=3, column=0, columnspan=2)
listbox_expenses = tk.Listbox(root, width=40, height=10)
listbox_expenses.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
update_expense_list()       #initil update of the list

#the button for deleting expenses
btn_delete = tk.Button(root, text="Delete the selected expense", command=delete_expense)
btn_delete.grid(row=5, column=0, columnspan=2, pady=10)

#launching the app
root.mainloop()