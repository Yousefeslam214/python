# =========================================================
#  LESSON 1 - Python literacy
#  Execution flow, variables, data types, operators,
#  and reading a short script line by line.
# =========================================================


# ---------- 1. print and execution flow ----------
# Python runs the code from top to bottom, one line at a time.
print("\n===== LESSON 1 =====")
print("Hello, world!")
print("This line runs second.")
print("And this one runs third.")

# A line that starts with # is a comment. Python ignores it.
# Comments are notes for humans.

# One small mistake stops the whole file from running (SyntaxError).
# Try it: remove the # from the next line, run the file, then put it back.
# print("hello"


# ---------- 2. variables ----------
# A variable is a name that stores a value.
print("\n--- 2. Variables ---")
name = "Yousef"
age = 25
print(name)
print(age)

# You can change (reassign) the value later.
age = 26
print(age)

# Good names describe what they store.
# Python style is snake_case: lowercase words joined with _
total_price = 150      # good: you know what it is
x = 150                # works, but what is x?


# ---------- 3. data types ----------
print("\n--- 3. Data types ---")
whole_number = 10          # int
decimal_number = 10.5      # float
text = "hello"             # str (string = text)
is_paid = True             # bool (only True or False)

# type() tells you the type of a value.
print(type(whole_number))
print(type(decimal_number))
print(type(text))
print(type(is_paid))

# Changing a value from one type to another
print(int("5") + 1)    # text "5" -> number 5   -> 6
print(str(5) + "1")    # number 5 -> text "5"   -> "51"


# ---------- 4. operators ----------
print("\n--- 4. Operators ---")
a = 11
b = 5
print("a + b  =", a + b)    # 16   addition
print("a - b  =", a - b)    # 6    subtraction
print("a * b  =", a * b)    # 55   multiplication
print("a / b  =", a / b)    # 2.2  division (always gives a float)
print("a // b =", a // b)   # 2    whole-number division
print("a % b  =", a % b)    # 1    remainder (modulus)
print("a ** 2 =", a ** 2)   # 121  power

# Comparison operators give True or False.
print(a > b)     # True
print(a == b)    # False   (== compares, = assigns)
print(a != b)    # True

# + joins strings together.
greeting = "hello" + " " + "world"
print(greeting)

# f-string: put variables inside text with {}
print(f"{name} is {age} years old")


# ---------- 5. read a script line by line ----------
# Before you run it: read each line and guess the output.
print("\n--- 5. Read a script ---")
price = 200
quantity = 3
tax_percent = 14

subtotal = price * quantity
tax = subtotal * tax_percent / 100
total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {total}")

# PRACTICE: change price and quantity, guess the new total, then run.



# =========================================================
#  LESSON 2 - Logic and debugging
#  if/else, lists, loops, dictionaries,
#  reading errors (tracebacks) and try/except.
# =========================================================


# ---------- 1. if / elif / else ----------
# Run code only when a condition is True.
print("\n===== LESSON 2 =====")
print("\n--- 1. if / else ---")
order_total = 1200

if order_total >= 1000:
    print("Big order: 10% discount")
elif order_total >= 500:
    print("Medium order: 5% discount")
else:
    print("No discount")

# The indentation (4 spaces) shows which lines belong to the if.

# Nested if: an if inside another if
is_paid = False
if order_total >= 1000:
    if is_paid:
        print("Big order, already paid")
    else:
        print("Big order, waiting for payment")


# ---------- 2. lists ----------
# A list stores many values in order.
print("\n--- 2. Lists ---")
products = ["Laptop", "Mouse", "Keyboard"]

print(products)
print(products[0])       # first item (counting starts at 0)
print(products[-1])      # last item
print(len(products))     # number of items

products.append("Monitor")    # add an item to the end
print(products)


# ---------- 3. loops (for and while) ----------
# A for loop repeats the code once for each item.
print("\n--- 3. Loops ---")
for product in products:
    print("Product:", product)

# range(3) gives 0, 1, 2
for number in range(3):
    print("Number:", number)

# Add up numbers with a loop
prices = [100, 250, 75]
total = 0
for price in prices:
    total = total + price
print("Total:", total)

# A while loop repeats as long as the condition is True.
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter = counter + 1    # without this line the loop never stops!


# ---------- 4. dictionaries ----------
# A dictionary stores values by name (key: value).
print("\n--- 4. Dictionaries ---")
customer = {
    "id": 1,
    "name": "Ahmed",
    "city": "Cairo",
}

print(customer["name"])
customer["city"] = "Giza"            # change a value
customer["phone"] = "01001234567"    # add a new key
print(customer)

# A list of dictionaries looks like a table:
# each dictionary is one row (record). This connects to SQL in Part B.
orders = [
    {"id": 1, "customer": "Ahmed", "amount": 500, "paid": True},
    {"id": 2, "customer": "Sara", "amount": 1200, "paid": False},
    {"id": 3, "customer": "Ahmed", "amount": 300, "paid": False},
]

# loop + if = keep only the rows we want (like SQL WHERE)
unpaid_total = 0
for order in orders:
    if not order["paid"]:        # "not" flips True <-> False
        print(f"Order {order['id']} from {order['customer']} is not paid")
        unpaid_total = unpaid_total + order["amount"]
print("Unpaid total:", unpaid_total)

# PRACTICE: add a 4th order and check the unpaid total changes.


# ---------- 5. reading errors (tracebacks) ----------
# When Python hits an error it stops and prints a "traceback".
# How to read it:
#   1. Read the LAST line first: the error type and message.
#   2. Find the line number: where it happened.
#   3. Look at that line, make ONE change, run again.
#
# Try it: remove the # from ONE line at a time, run, read the error.
# print(discount)               # NameError: this variable was never created
# print("Total: " + 100)        # TypeError: can't join text and a number
# print(products[10])           # IndexError: there is no item at index 10
# print(customer["email"])      # KeyError: this key does not exist
# print(10 / 0)                 # ZeroDivisionError


# ---------- 6. try / except ----------
# try/except catches an error so the program does not crash.
print("\n--- 6. try / except ---")
user_input = "abc"

try:
    number = int(user_input)
    print("Number:", number)
except ValueError:
    print(f"'{user_input}' is not a number")

print("The program keeps running.")


# ---------- 7. debugging exercise ----------
# This code has 2 bugs.
# Select the 5 lines and press Ctrl+/ to remove the #, then run.
# Read the traceback, fix ONE bug, run again. Repeat.
#
# prices = [100, 250, 75]
# total = 0
# for price in prices
#     total = total + price
# print("Total: " + total)
