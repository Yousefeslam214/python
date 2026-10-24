# =========================================================
#  LESSON 3 - The Python toolkit
#  Functions, modules and imports, files, CSV, JSON,
#  classes, and installing packages with pip.
# =========================================================
#
# How to use this file:
#   Read one section, guess what it will print, then run the file and check.
#   Each section ends with a LATER line: where you will use it again.
#
# This file makes an "output" folder with a few files inside.
# The code makes them, so you don't need to commit them.


# ---------- 1. functions ----------
# A function is a named block of code. Write it once, use it many times.
print("\n===== LESSON 3 =====")
print("\n--- 1. Functions ---")


def say_hello():
    print("Hello from a function!")


say_hello()    # calling the function runs the code inside it
say_hello()    # call it again: no need to write the code twice

# Defining a function (def) does NOT run it. Only calling it does.


# Parameters: the values a function needs.
def greet(name):              # name is a parameter
    print(f"Hello, {name}!")


greet("Sara")                 # "Sara" is the argument (the real value)
greet("Omar")


# A parameter can have a default value. You can skip it when you call.
def calculate_total(price, quantity, tax_percent=14):
    subtotal = price * quantity
    tax = subtotal * tax_percent / 100
    return subtotal + tax     # return sends the result back


total = calculate_total(200, 3)               # tax_percent uses the default: 14
print("Total:", total)                        # 684.0
print("No tax:", calculate_total(200, 3, 0))  # 600.0


# print vs return
# print shows a value on the screen. return gives the value back to your code.
def add_and_print(a, b):
    print(a + b)              # shows the answer, but gives nothing back


def add_and_return(a, b):
    return a + b              # gives the answer back


result = add_and_return(2, 3)
print(result * 10)            # 50: you can keep using a returned value

nothing = add_and_print(2, 3)  # shows 5
print(nothing)                 # None: a function without return gives back None


# Functions work with the lists and dictionaries from Lesson 2.
orders = [
    {"id": 1, "customer": "Ahmed", "amount": 500, "paid": True},
    {"id": 2, "customer": "Sara", "amount": 1200, "paid": False},
    {"id": 3, "customer": "Ahmed", "amount": 300, "paid": False},
]


def get_unpaid_total(orders):
    total = 0
    for order in orders:
        if not order["paid"]:
            total = total + order["amount"]
    return total


print("Unpaid total:", get_unpaid_total(orders))    # 1500


# GUESS FIRST: what does the last line print? Then run and check.
def double(number):
    return number * 2


def add_tax(amount):
    return amount + amount * 14 / 100


print(add_tax(double(100)))   # the inner function runs first

# PRACTICE: write count_orders(orders, customer_name) that RETURNS how many
# orders one customer has. count_orders(orders, "Ahmed") should give 2.

# LATER: every program you read from now on is made of functions.


# ---------- 2. modules and imports ----------
# A module is a .py file full of ready code. import lets you use it.
print("\n--- 2. Modules and imports ---")

import math                   # a module that comes with Python
from datetime import date     # take only one thing (date) from a module

print(math.ceil(4.2))         # 5: round up
print(math.sqrt(81))          # 9.0: square root
print("Today is", date.today())

# Your own file is a module too. shop_tools.py is next to this file.
from shop_tools import price_with_tax, format_egp

laptop_price = price_with_tax(1200)
print(format_egp(laptop_price))    # 1,368.00 EGP

# PRACTICE: open shop_tools.py and read the two functions.
# Then print format_egp(calculate_total(200, 3)). What do you get?

# LATER: a Django project (Session 3) is a folder of modules that import
# each other, with lines like: from .models import Post


# ---------- 3. files and paths ----------
# Programs save data in files, so it is still there after the program stops.
print("\n--- 3. Files and paths ---")

from pathlib import Path

print("Python is running in:", Path.cwd())    # paths start from this folder

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)            # make the folder (no error if it already exists)
notes_file = output_folder / "notes.txt"      # / joins a folder and a file name

# "w" = write. It creates the file, or replaces what was in it.
# encoding="utf-8" lets the file hold any language, Arabic too.
with open(notes_file, "w", encoding="utf-8") as file:
    file.write("Call Sara about order 2\n")   # \n = new line
    file.write("Send the invoice to Ahmed\n")

# "r" = read.
with open(notes_file, "r", encoding="utf-8") as file:
    print(file.read())

# with ... as file: Python closes the file for you when the block ends.
# Use "a" (append) to add to the end of a file instead of replacing it.

# PRACTICE: open output/notes.txt in VS Code. Then change "w" to "a",
# run the file twice, and look again. What changed?

# LATER: scripts write logs and reports to files, like the log of the
# auto-publisher in Session 6.


# ---------- 4. CSV files ----------
# CSV = a table saved as text: one row per line, commas between the values.
# Excel and Odoo can export and import CSV files.
print("\n--- 4. CSV ---")

import csv

csv_file = output_folder / "orders.csv"

# Write: one row for each dictionary.
# newline="" stops empty lines between the rows on Windows.
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "customer", "amount", "paid"])
    writer.writeheader()      # first row: the column names
    writer.writerows(orders)  # one row for each order

# Read: each row comes back as a dictionary.
total = 0
with open(csv_file, newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["customer"], row["amount"])
        total = total + int(row["amount"])    # int(): CSV gives back TEXT, not numbers

print("Total from the CSV:", total)           # 2000
print(type(row["amount"]))                    # <class 'str'>
# Careful: "paid" comes back as text too: "True" or "False".

# PRACTICE: open output/orders.csv in VS Code and find the header row.

# LATER: you will read exported CSV files (Odoo, Excel) and turn them into reports.


# ---------- 5. JSON ----------
# JSON is the most common way programs send data to each other.
# It looks almost the same as Python dictionaries and lists:
#   Python {} dictionary  ->  JSON {} object
#   Python [] list        ->  JSON [] array
#   True / False          ->  true / false
#   None                  ->  null
print("\n--- 5. JSON ---")

import json

report = {
    "shop": "Cairo Electronics",
    "total_orders": len(orders),
    "unpaid_total": get_unpaid_total(orders),
    "top_customer": {"name": "Sara", "city": "Alexandria"},    # a dictionary inside a dictionary
    "products": ["Laptop", "Mouse", "Keyboard"],                # a list inside a dictionary
}

# dumps = "dump to a string": dictionary -> JSON text. indent=2 makes it easy to read.
print(json.dumps(report, indent=2))

report_file = output_folder / "report.json"
with open(report_file, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=2)  # save the dictionary as a JSON file

with open(report_file, encoding="utf-8") as file:
    loaded = json.load(file)           # JSON file -> dictionary

print(loaded["top_customer"]["city"])  # Alexandria: first the key "top_customer", then "city"
print(loaded["products"][0])           # Laptop: first the key, then the position

# PRACTICE: add "city": "Cairo" to report, run, and open output/report.json.

# LATER: APIs answer in JSON (section 7), AI can answer in JSON (Session 5),
# and the Django backend sends JSON to the React screen (Session 4).


# ---------- 6. classes and objects ----------
# For now you only need to READ classes.
# A class is a template, like an empty order form.
# An object is one filled-in copy of the form.
print("\n--- 6. Classes and objects ---")


class Order:
    def __init__(self, customer, amount, paid):   # runs when you make a new object
        self.customer = customer   # attributes: the data inside each object
        self.amount = amount
        self.paid = paid

    def amount_with_tax(self, tax_percent=14):    # a method: a function inside a class
        return self.amount + self.amount * tax_percent / 100


order_1 = Order("Ahmed", 500, True)     # an object made from the Order class
order_2 = Order("Sara", 1200, False)    # another object, with its own data

print(order_1.customer)                 # Ahmed
print(order_2.amount)                   # 1200
print(order_2.amount_with_tax())        # 1368.0

# self means "this object". order_2.amount_with_tax() uses order_2's amount.

# LATER: in Django (Session 3) every table is a class like this:
#     class Post(models.Model):
#         text = models.TextField()
#         status = models.CharField(max_length=20)
# The class = the table. Each object = one row.


# ---------- 7. pip, virtual environments and requests ----------
# Python comes with many modules (math, csv, json ...). People share many
# more online as "packages". pip downloads and installs them.
# A virtual environment (.venv) is a private box of packages for ONE project,
# so one project can't break another.
#
# Do this once:
#   1. Press Ctrl+Shift+P, type "Python: Create Environment", choose Venv,
#      then choose your Python. VS Code makes a .venv folder, starts using it,
#      and tells Git to ignore it (so it never shows up in Source Control).
#   2. Open a NEW terminal (Terminal -> New Terminal). The line starts with (.venv).
#   3. Type:  pip install requests
#      Not working? Use the full path instead:
#        Windows:      .venv\Scripts\python -m pip install requests
#        Mac / Linux:  .venv/bin/python -m pip install requests
#   4. Select the lines below and press Ctrl+/ to remove the #, then run.
#
# requests asks a website for data. This free weather API needs no key
# and answers in JSON.
print("\n--- 7. pip and requests ---")

# import requests
#
# url = "https://api.open-meteo.com/v1/forecast"
# query = {
#     "latitude": 30.04,                # Cairo
#     "longitude": 31.24,
#     "daily": "temperature_2m_max",    # the highest temperature of each day
#     "timezone": "Africa/Cairo",
# }
# response = requests.get(url, params=query, timeout=10)    # wait 10 seconds at most
# print("Status code:", response.status_code)               # 200 = OK
#
# weather = response.json()                                 # JSON text -> dictionary
# days = weather["daily"]["time"]
# temperatures = weather["daily"]["temperature_2m_max"]
# print("First day:", days[0], temperatures[0], "C")
# print("Hottest:", max(temperatures), "C")
#
# with open(output_folder / "weather.json", "w", encoding="utf-8") as file:
#     json.dump(weather, file, indent=2)
# print("Saved output/weather.json")

# LATER: in Session 3 you will run "pip install django". In Sessions 5 and 6
# the same idea (send a request, get JSON back) talks to the Claude and LinkedIn APIs.


# ---------- 8. common errors ----------
# Remove the # from ONE line at a time, run, and read the LAST line of the error.
print("\n--- 8. Common errors ---")

# open("output/missing.txt")          # FileNotFoundError: no file with this name in this folder
# json.loads("{'name': 'Sara'}")      # JSONDecodeError: JSON needs "double quotes"
# import reqests                      # ModuleNotFoundError: a typo, or the package isn't installed
# calculate_total(200)                # TypeError: missing 1 required positional argument: 'quantity'
# print(order_1.city)                 # AttributeError: 'Order' object has no attribute 'city'

print("Done! Look inside the output folder.")
