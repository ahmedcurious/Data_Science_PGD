product = 'laptop'
discount = 25
original_price = 20000
discounted_price = original_price - (original_price*(25/100))
formatted_string = "I bought a {} having original price of {}".format(
    product, original_price)+f" but I got a discount of {discount}%"+" and after discount I got it for %d" % (discounted_price)

print(formatted_string)

# **Assignment 5: Combining Formatting Methods**

# **Instructions:**

# 1. Create a variable `product` and assign a product name.
# 2. Create a variable `discount` and assign a discount percentage.
# 3. Create a variable `original_price` and assign an original price.
# 4. Calculate the discounted price using the formula: `discounted_price = original_price * (1 - discount / 100)`.
# 5. Using any combination of string formatting methods (`+`, `.format()`, `f''`, `%()`), create a descriptive string with the product name, original price, discount percentage, and discounted price.
# 6. Print the descriptive string.
