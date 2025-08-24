import tkinter as tk
from tkinter import ttk

# Latest USD to INR exchange rate
USD_TO_INR = 87.33  # as of August 23, 2025

# Example global average expected stock market return (for illustration, set at 7%)
EXPECTED_RETURN_PERCENT = 7.0

def calculate():
    try:
        amount = float(amount_entry.get())
        currency = currency_var.get()

        # Convert and display
        if currency == "INR":
            amount_in_usd = amount / USD_TO_INR
            converted_label.config(text=f"USD: {amount_in_usd:.2f}")
            invested = amount
        else:
            amount_in_inr = amount * USD_TO_INR
            converted_label.config(text=f"INR: {amount_in_inr:.2f}")
            invested = amount_in_inr

        # Calculate estimated profit (one year, simple interest)
        profit = invested * EXPECTED_RETURN_PERCENT / 100
        total = invested + profit
        profit_label.config(text=f"Estimated Profit (1yr): {profit:.2f} INR")
        total_label.config(text=f"Total Value: {total:.2f} INR")
    except ValueError:
        converted_label.config(text="Invalid input")
        profit_label.config(text="")
        total_label.config(text="")

# Tkinter UI
root = tk.Tk()
root.title("Stock Market Calculator (INR/USD)")

ttk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

currency_var = tk.StringVar(value="INR")
ttk.Label(root, text="Currency:").grid(row=1, column=0, padx=10, pady=10)
currency_combo = ttk.Combobox(root, textvariable=currency_var, values=["INR", "USD"], state="readonly")
currency_combo.grid(row=1, column=1, padx=10, pady=10)

calc_button = ttk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

converted_label = ttk.Label(root, text="")
converted_label.grid(row=3, column=0, columnspan=2, pady=10)

profit_label = ttk.Label(root, text="")
profit_label.grid(row=4, column=0, columnspan=2, pady=10)

total_label = ttk.Label(root, text="")
total_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
