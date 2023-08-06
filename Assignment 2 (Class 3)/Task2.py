item = "laptop"
price = "40,000"
quantity = 2
total_cost = price * quantity
formatted_string = "I bought {2} {0}(s) at {1} each, for a total of ${3}.".format(
    item, price, quantity, total_cost)
print(formatted_string)
