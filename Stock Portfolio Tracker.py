# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200
}

portfolio = {}
total_value = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks the user wants to enter
n = int(input("How many different stocks do you want to add? "))

# Get stock names and quantities from the user
for i in range(n):
    stock_name = input(f"\nEnter stock name #{i + 1}: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found! Skipping this entry.")

# Calculate total investment value
print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(
        f"{stock}: {quantity} shares × ${price} = ${value}"
    )

print("\nTotal Investment Value = $", total_value)

# Optional: Save results to a text file
save = input("\nDo you want to save the portfolio to a text file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("========================\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(
                f"{stock}: {quantity} shares × ${price} = ${value}\n"
            )

        file.write(f"\nTotal Investment Value = ${total_value}")

    print("Portfolio saved successfully as 'portfolio_summary.txt'.")
else:
    print("Portfolio was not saved.")