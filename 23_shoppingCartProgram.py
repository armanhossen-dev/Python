# PreventS 'Ctrl + C' / 'KeyboardInterrupt' ignoring interrupt THIS TWO LINES
import signal
signal.signal(signal.SIGINT,signal.SIG_IGN)

foods = []
prices = []
total = 0
totalpay = 0
print("\n---Welcome to Mayer Dua Shopping Mall----")
print("Enter a food you want to buy (q to quit)\n")
i = 0
d3 = 0

while  True:
    i+=1
    print(f'{i}. ', end="")
    food = input("Food Name: ")
    if food.lower() == 'q': # if user type 'Q'
        print()
        break
    else:
        foods.append(food)
        total += 1
        price = float(input("   Food price: $"))
        prices.append(price) 
        totalpay += price

max_price_width = len(f"{max(prices):.2f}")
max_food_width = max(len(food) for food in foods)

print("----------Your Cart----------")
print("Your shopping list: ")
for a in range(total):
    # print(f"{a+1}. Item Name: \t{foods[a]:<10} \tPrice: \t${prices[a]:>{max_width}.2f}")
    print(
        f"{a+1}. "
        f"Item Name: {foods[a]:<{max_food_width}}  "
        f"Price: ${prices[a]:>{max_price_width}.2f}" 
    )    
# print("-------------------------------------------------")
# print(f"You have to pay: \t\t\t${totalpay:.2f}\n")

line_width = max_food_width + max_price_width + 24
print("-" * line_width)
print(
    f"{'You have to pay:':<{line_width - max_price_width - 1}}"
    f"${totalpay:>{max_price_width}.2f}\n"
)