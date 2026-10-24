# =========================================================
#  shop_tools.py - a small module for Lesson 3
#  A module is just a .py file with code you want to reuse.
#  lesson_3_toolkit.py imports the two functions below.
# =========================================================


# Returns the price after adding tax.
def price_with_tax(price, tax_percent=14):
    return price + price * tax_percent / 100


# Returns the amount as text in Egyptian pounds, like "1,368.00 EGP".
# ,.2f means: a comma between thousands and 2 digits after the dot.
def format_egp(amount):
    return f"{amount:,.2f} EGP"
