# Session 2 · Part B: SQL & Databases

**Goal:** By the end you understand how business data is stored (tables, records, IDs) and you can answer real business questions with `SELECT`, `WHERE`, `JOIN` and `GROUP BY`.

**Time:** about 90 minutes. All examples use one small practice database.

---

## 1. What is a database?

A database stores data in **tables**. A table looks like an Excel sheet.

| Word | Simple meaning | Example |
|---|---|---|
| **Table** | A group of the same kind of thing | `customers`, `orders` |
| **Row / record** | One thing | One customer |
| **Column** | One piece of information about each row | `name`, `city` |
| **ID (primary key)** | A unique number for each row. No two rows have the same ID. | `customers.id = 1` |
| **Foreign key** | A column that points to an ID in **another** table | `orders.customer_id` |

### Our practice tables

**`customers`**

| id | name | city |
|---|---|---|
| 1 | Ahmed | Cairo |
| 2 | Sara | Alexandria |
| 3 | Omar | Giza |
| 4 | Mona | Cairo |
| 5 | Khaled | Alexandria |

**`orders`** (`paid`: 1 = yes, 0 = no)

| id | customer_id | product | amount | paid | order_date |
|---|---|---|---|---|---|
| 1 | 1 | Laptop | 500 | 1 | 2026-09-01 |
| 2 | 2 | Monitor | 1200 | 0 | 2026-09-03 |
| 3 | 1 | Mouse | 300 | 0 | 2026-09-05 |
| 4 | 3 | Keyboard | 150 | 1 | 2026-09-10 |
| 5 | 4 | Laptop | 900 | 1 | 2026-09-12 |
| 6 | 2 | Mouse | 250 | 1 | 2026-09-15 |
| 7 | 4 | Monitor | 700 | 0 | 2026-09-20 |

### How the tables are related

```
orders.customer_id  ───►  customers.id
```

Order 2 has `customer_id = 2`, so it belongs to customer 2, **Sara**.

> **Link to Part A:** in Python, the `orders` list of dictionaries in `main.py` is a table. Each dictionary is one row, and each key is a column.
>
> **Link to Odoo:** Odoo stores its data the same way. For example, customers are in the `res_partner` table and sales orders are in the `sale_order` table.

---

## 2. Set up the practice database

### Option A: DB Browser for SQLite (easiest)

1. Download and install it from **sqlitebrowser.org**. It's free.
2. Click **New Database** and save it as `practice.db`. Close the "Edit table" window that opens.
3. Open the **Execute SQL** tab.
4. Paste the setup code below and press **▶ Run** (or `Ctrl+Enter`).
5. Click **Write Changes** (or `Ctrl+S`).

### Option B: Terminal

```bash
sqlite3 practice.db
```

Then paste the setup code. These two commands make the output easier to read:

```
.headers on
.mode column
```

Type `.quit` to exit.

### Setup code

```sql
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product     TEXT,
    amount      INTEGER,
    paid        INTEGER,
    order_date  TEXT
);

INSERT INTO customers (id, name, city) VALUES
    (1, 'Ahmed',  'Cairo'),
    (2, 'Sara',   'Alexandria'),
    (3, 'Omar',   'Giza'),
    (4, 'Mona',   'Cairo'),
    (5, 'Khaled', 'Alexandria');

INSERT INTO orders (id, customer_id, product, amount, paid, order_date) VALUES
    (1, 1, 'Laptop',   500,  1, '2026-09-01'),
    (2, 2, 'Monitor',  1200, 0, '2026-09-03'),
    (3, 1, 'Mouse',    300,  0, '2026-09-05'),
    (4, 3, 'Keyboard', 150,  1, '2026-09-10'),
    (5, 4, 'Laptop',   900,  1, '2026-09-12'),
    (6, 2, 'Mouse',    250,  1, '2026-09-15'),
    (7, 4, 'Monitor',  700,  0, '2026-09-20');
```

---

## 3. SELECT: get data

```sql
SELECT * FROM customers;
```

`*` means "all columns". This shows the whole `customers` table.

**Choose columns:**

```sql
SELECT name, city FROM customers;
```

**Sort the results** (`DESC` = biggest first, `ASC` = smallest first):

```sql
SELECT * FROM orders ORDER BY amount DESC;
```

**Only show a few rows.** Do this when you explore a big real table:

```sql
SELECT * FROM orders LIMIT 3;
```

### Basic rules

- Put **text** in single quotes: `'Cairo'`. Numbers don't need quotes: `500`.
- End each query with `;`.
- Writing keywords like `SELECT` and `FROM` in CAPITALS is a style habit, not a rule.

---

## 4. WHERE: filter rows

`WHERE` keeps only the rows that match a condition.

```sql
SELECT * FROM customers WHERE city = 'Cairo';
```

| id | name | city |
|---|---|---|
| 1 | Ahmed | Cairo |
| 4 | Mona | Cairo |

### Comparison operators

These are the same idea as in Python:

| SQL | Meaning |
|---|---|
| `=` | equal (Python uses `==`) |
| `!=` | not equal |
| `>` `<` | bigger / smaller |
| `>=` `<=` | bigger or equal / smaller or equal |

```sql
SELECT * FROM orders WHERE amount > 500;
SELECT * FROM orders WHERE paid = 0;
SELECT * FROM orders WHERE order_date >= '2026-09-10';
```

### AND / OR

```sql
-- unpaid AND big
SELECT * FROM orders WHERE paid = 0 AND amount > 500;
```

| id | customer_id | product | amount | paid | order_date |
|---|---|---|---|---|---|
| 2 | 2 | Monitor | 1200 | 0 | 2026-09-03 |
| 7 | 4 | Monitor | 700 | 0 | 2026-09-20 |

```sql
-- Laptop OR Mouse
SELECT * FROM orders WHERE product = 'Laptop' OR product = 'Mouse';
```

`--` starts a comment in SQL, like `#` in Python.

---

## 5. JOIN: combine two tables

**The problem:** the `orders` table says `customer_id = 2`, but who is customer 2?

**The fix:** `JOIN` connects the two tables using the ID.

```sql
SELECT orders.id, customers.name, orders.product, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

| id | name | product | amount |
|---|---|---|---|
| 1 | Ahmed | Laptop | 500 |
| 2 | Sara | Monitor | 1200 |
| 3 | Ahmed | Mouse | 300 |
| 4 | Omar | Keyboard | 150 |
| 5 | Mona | Laptop | 900 |
| 6 | Sara | Mouse | 250 |
| 7 | Mona | Monitor | 700 |

How to read it:

- `FROM orders JOIN customers`: use both tables.
- `ON orders.customer_id = customers.id`: this is **how they are related**.
- `orders.amount` means "the `amount` column from the `orders` table". Write the table name when both tables have a column with the same name, like `id`.

### JOIN + WHERE

Unpaid orders, with the customer's name:

```sql
SELECT customers.name, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE orders.paid = 0;
```

| name | amount |
|---|---|
| Sara | 1200 |
| Ahmed | 300 |
| Mona | 700 |

> **Notice:** Khaled never appears in JOIN results, because he has no orders. `JOIN` only keeps rows that match in **both** tables.

---

## 6. GROUP BY: totals per group

First, some functions that work on many rows at once:

| Function | Meaning |
|---|---|
| `COUNT(*)` | how many rows |
| `SUM(column)` | add up |
| `AVG(column)` | average |
| `MIN(column)` / `MAX(column)` | smallest / biggest |

```sql
SELECT COUNT(*) FROM orders;       -- 7
SELECT SUM(amount) FROM orders;    -- 4000
```

`GROUP BY` puts the rows into **groups** and then calculates **one result per group**.

**Sales per product:**

```sql
SELECT product, COUNT(*) AS times_sold, SUM(amount) AS revenue
FROM orders
GROUP BY product;
```

| product | times_sold | revenue |
|---|---|---|
| Keyboard | 1 | 150 |
| Laptop | 2 | 1400 |
| Monitor | 2 | 1900 |
| Mouse | 2 | 550 |

`AS` gives the result column a clear name.

**Total spent per customer, biggest first** (JOIN + GROUP BY + ORDER BY):

```sql
SELECT customers.name, COUNT(*) AS order_count, SUM(orders.amount) AS total_spent
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.name
ORDER BY total_spent DESC;
```

| name | order_count | total_spent |
|---|---|---|
| Mona | 2 | 1600 |
| Sara | 2 | 1450 |
| Ahmed | 2 | 800 |
| Omar | 1 | 150 |

> **Real-world tip:** two customers can have the same name. In a real system, group by `customers.id` so they don't get mixed together.

---

## 7. Thinking in SQL: from a business question to a query

Before you write any SQL, answer 3 questions:

1. **What data do I need?**
2. **Where is it?** Which tables?
3. **How is it related?** Which IDs connect the tables?

### Worked example

> *"How much money do our Cairo customers still owe us?"*

1. **What:** order amounts, whether they are paid, the customer's city.
2. **Where:** `orders` (amount, paid) and `customers` (city).
3. **How:** `orders.customer_id = customers.id`.

```sql
SELECT SUM(orders.amount) AS cairo_unpaid
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.city = 'Cairo' AND orders.paid = 0;
```

Result: **1000** (Ahmed 300 + Mona 700).

### The order of the parts

The parts of a query always come in this order:

```sql
SELECT   ...   -- which columns
FROM     ...   -- which table
JOIN     ...   -- add another table
  ON     ...   -- how the tables are related
WHERE    ...   -- filter rows
GROUP BY ...   -- make groups
ORDER BY ...   -- sort
LIMIT    ...;  -- how many rows
```

---

## 8. Common errors

Read errors the same way as Python tracebacks: read the message, find the problem, fix **one** thing, run again.

| Error | What it means | Example that causes it |
|---|---|---|
| `no such table: orderz` | Table name typo, or wrong database file open | `SELECT * FROM orderz;` |
| `no such column: nmae` | Column name typo | `SELECT nmae FROM customers;` |
| `no such column: Cairo` | You forgot the quotes around text | `WHERE city = Cairo` → `WHERE city = 'Cairo'` |
| `ambiguous column name: id` | Both tables have `id`, so SQL doesn't know which one | Write `orders.id` or `customers.id` |
| `near "FROM": syntax error` | A missing or extra comma, or a word in the wrong place | `SELECT name, city, FROM customers;` |

---

## 9. Safety: reading vs changing data

- `SELECT` only **reads**. It is always safe.
- `UPDATE` and `DELETE` **change** data. Be very careful:

```sql
DELETE FROM orders;                 -- ⚠️ deletes EVERY order
DELETE FROM orders WHERE id = 7;    -- deletes only order 7
```

**Rules for real company databases (like Odoo):**

- Practice on **sample data or a copy**, never on the live (production) database.
- Use a **read-only** account when you only need reports.
- Never run `UPDATE` or `DELETE` on real data unless someone has reviewed it and there is a **backup**.

---

## 10. Cheat sheet

```sql
SELECT * FROM table_name;                       -- all rows, all columns
SELECT col1, col2 FROM table_name;              -- some columns
SELECT * FROM t WHERE col = 'text';             -- filter
SELECT * FROM t WHERE a > 5 AND b = 0;          -- two conditions
SELECT * FROM t ORDER BY col DESC;              -- sort, biggest first
SELECT * FROM t LIMIT 10;                       -- first 10 rows

SELECT a.col, b.col
FROM a JOIN b ON a.b_id = b.id;                 -- combine tables

SELECT col, COUNT(*), SUM(amount)
FROM t GROUP BY col;                            -- totals per group
```

---

## 11. Practice

Try each one yourself first. Then open **Answer** to check.

**1. Show all orders for `Mouse`.**

<details><summary>Answer</summary>

```sql
SELECT * FROM orders WHERE product = 'Mouse';
```
2 rows: orders 3 and 6.
</details>

**2. Show all customers from Alexandria.**

<details><summary>Answer</summary>

```sql
SELECT * FROM customers WHERE city = 'Alexandria';
```
Sara and Khaled.
</details>

**3. Show paid orders with an amount less than 500.**

<details><summary>Answer</summary>

```sql
SELECT * FROM orders WHERE paid = 1 AND amount < 500;
```
Orders 4 (150) and 6 (250). Order 1 is exactly 500, so it is **not** less than 500.
</details>

**4. Show every order with the customer's name and city.**

<details><summary>Answer</summary>

```sql
SELECT orders.id, customers.name, customers.city, orders.product, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```
</details>

**5. How many orders are there for each product?**

<details><summary>Answer</summary>

```sql
SELECT product, COUNT(*) AS order_count
FROM orders
GROUP BY product;
```
Keyboard 1, Laptop 2, Monitor 2, Mouse 2.
</details>

**6. What are the total sales per city?**

<details><summary>Answer</summary>

```sql
SELECT customers.city, SUM(orders.amount) AS total
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.city;
```
Alexandria 1450, Cairo 2400, Giza 150.
</details>

**7. Who still owes us money, and how much?**

<details><summary>Answer</summary>

```sql
SELECT customers.name, SUM(orders.amount) AS unpaid
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE orders.paid = 0
GROUP BY customers.name;
```
Ahmed 300, Mona 700, Sara 1200.
</details>

**8. Challenge: who is our biggest customer?**

<details><summary>Answer</summary>

```sql
SELECT customers.name, SUM(orders.amount) AS total_spent
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.name
ORDER BY total_spent DESC
LIMIT 1;
```
Mona, with 1600.
</details>

### Homework

1. Write **3 business questions** of your own about this data. For each one, answer the 3 questions from section 7 (what, where, how related), then write the SQL.
2. Make one SQL error on purpose. Read the error message and explain it in your own words.
3. Commit your queries to Git (from Session 1) in a file called `my_queries.sql`.
