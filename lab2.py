import matplotlib.pyplot as plt
import random

# Constants
AVERAGE_PRICE = 600  # average price of a smartphone in BDT
DISCOUNT_THRESHOLD = 0.20  # 20% discount threshold
CRITICAL_STOCK_LEVEL = 10  # if stock is below this level, it's critical
ORDER_QUANTITY = 15  # default order quantity if conditions are met
MIN_ORDER_QUANTITY = 10  # minimum order quantity for critical stock

# Function to simulate agent decision
def trading_agent_decision(price, stock):
    """
    Determines the number of smartphones to order based on price and stock levels.
    """
    discount_price_threshold = AVERAGE_PRICE * (1 - DISCOUNT_THRESHOLD)
    tobuy = 0  # default order quantity is 0 (no order)

    # Decision logic based on given rules
    if price < discount_price_threshold and stock >= CRITICAL_STOCK_LEVEL:
        tobuy = ORDER_QUANTITY  # order more due to discount
    elif stock < CRITICAL_STOCK_LEVEL:
        tobuy = MIN_ORDER_QUANTITY  # order minimum due to low stock

    return tobuy

# Simulate prices and stock levels
prices = [random.randint(500, 700) for _ in range(30)]  # random price between 500 and 700
stocks = [random.randint(5, 25) for _ in range(30)]  # random stock level between 5 and 25
orders = []

# Generate orders based on agent decision
for price, stock in zip(prices, stocks):
    tobuy = trading_agent_decision(price, stock)
    orders.append(tobuy)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(prices, label="Price (BDT)", color="blue", marker="o")
plt.plot(stocks, label="Stock Level", color="green", marker="s")
plt.plot(orders, label="Order Quantity", color="red", marker="^")
plt.xlabel("Day")
plt.ylabel("Value")
plt.title("Trading Agent Decisions on Smartphone Inventory Management")
plt.legend()
plt.grid(True)
plt.show()
