#pip install requests
#Frankfurter API (free, no key)

import tkinter as tk
import requests

#live converion function

def convert():
    from_cur = from_currency.get().upper()
    to_cur = to_currency.get().upper()
    amount = float(amount_entry.get())
    
    url = f"https://api.frankfurter.app/latest?from={from_cur}&to={to_cur}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_cur]
    result = amount * rate    
    result_label.config(text=f"{amount} {from_cur} = {result:.2f} {to_cur}")
    
    
# GUI Window
root = tk.Tk()
root.title("Live Currency Converter")
root.geometry("400x300")

# Input fields
tk.Label(root, text = "From Currency (USD, EUR, GBP):").pack(pady=(20,5))
from_currency = tk.Entry(root)
from_currency.pack()

tk.Label(root, text="To Currency:").pack()
to_currency = tk.Entry(root)
to_currency.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# button
tk.Button(root, text="Convert Now 🤑", command=convert).pack(pady=10)

# finaly the result
result_label = tk.Label(root, text="Result will appear here", font=("Arial", 12))
result_label.pack(pady=20)

#run app
root.mainloop()