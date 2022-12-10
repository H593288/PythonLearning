
#Original pris og rabatt prosenten
original_price = float(input("Original price: "))
discount_percentage =float(input("Discount percentage: "))

# Regne ut prosenten
discount_amount = original_price * (discount_percentage/100)

# Regne ut prisen etter rabatt
total_price = original_price - discount_amount

#Print total prisen
print("Pris etter rabatten: " + str(total_price) + " NOK")