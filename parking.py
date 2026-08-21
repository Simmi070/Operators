def calculate_change(paid, price):
    change = paid - price
    return change

parking_price = 10
print("===== Parking Ticket =====")
print(f"The parking costs {parking_price} $.")
print("Accepted coins: 1, 2, 5, 10\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 2, 5, 10\n)"))

    if coin != 1 and coin != 2 and coin != 5 and coin != 10:
        print("Invalid coin, try again!\n")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    if total_inserted >= parking_price:
        print("Enough money inserted!\n")
        break

change_due = calculate_change(total_inserted, parking_price)

print("Thank you!")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\n===== PURCHASE SUMMARY =====")
print("Parking Price: ", parking_price)
print("Coins Inserted: ", coins_inserted)
print("Total Paid: ", total_inserted)
print("Change Given: ", change_due)
print("==============================")
print("Thanks for your purchase!")