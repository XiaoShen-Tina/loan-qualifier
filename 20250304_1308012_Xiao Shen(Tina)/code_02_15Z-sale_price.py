# This program gets an item's original price and calculate its sale price, with a 20% discount.
# Set discount
discount = 0.2
# Get a original price of a product
price_ori = input("Please enter original price of the product you choice:")
# Calculate the amount of discount
amount_disc = price_ori * discount
# Calculate the discounted price
price_disc = price_ori - amount_disc
# Display amount of discount and discounted price with message. Number should, after 3 digits, and show 2 digits after dicimal points
print(f"What you selected is {price_ori:,.2f} amount_disc, price_disc)