# Problem 1: Filter Prices
prices = [50, 120, 300, 85, 210]

def filter_prices(prices):
    filtered = []
    for price in prices:
        if price > 100:
            filtered.append(price)
    return filtered

print(filter_prices(prices))

# Problem 2: Check User Status
user = {"username": "Magdy320", "is_active": True}

def check_user(user):
    # اكتب شرط if هنا يفحص قيمة user["is_active"]
    if user["is_active"]:
        print("welcome, ", user["username"])
    else:
        print("Account is disabled")

check_user(user)