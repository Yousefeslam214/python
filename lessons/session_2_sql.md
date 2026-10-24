# Session 2 · Part B: SQL & Databases

**Goal:** understand how business data is stored, and answer business questions with `SELECT`, `WHERE`, `JOIN` and `GROUP BY`.

**Time:** about 70 minutes, plus 15 for the quick topics (or do them at home) · **Tool:** DB Browser for SQLite (free)

---

## 1. The idea

A database stores data in **tables**. A table looks like an Excel sheet.

Every business system (Odoo, an online shop, a bank) keeps its data in tables like these. With SQL you can answer your own business questions in seconds, instead of waiting for someone to build a report.

| Word | Meaning |
|---|---|
| **Table** | A group of one kind of thing: `customers`, `orders` |
| **Row (record)** | One thing, like one customer |
| **Column** | One piece of information, like `name` or `city` |
| **id (primary key)** | A unique number for each row |
| **Foreign key** | A column that points to an `id` in another table |

Our practice database has **2 tables**. Each order says **which customer** it belongs to:

![orders.customer_id points to customers.id: order 2 belongs to Sara](images/sql/01-tables.png)

> **Link to Part A:** the `orders` list in `main.py` is a table. Each dictionary is one row.
> **Link to Odoo:** Odoo works the same way. Customers are in the `res_partner` table and sales orders are in `sale_order`.

---

## 2. Setup (only once)

1. Install **DB Browser for SQLite** from **sqlitebrowser.org**.
2. Click **New Database** ①, save it as `practice.db`, and close the "Edit table" window that opens.
3. Open the **Execute SQL** tab ②, paste the setup code below, and press **▶ Run** (or `Ctrl+Enter`).
4. Click **Write Changes** ③ (or `Ctrl+S`).
5. Open **Browse Data** ④ to see your tables.

![DB Browser for SQLite: 1 New Database, 2 Execute SQL, 3 Write Changes, 4 Browse Data](images/sql/00-db-browser.png)

**Setup code** (copy all of it):

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

> From now on, write every query in the **Execute SQL** tab ② and press **▶**.
> In the `paid` column, **1 = yes** and **0 = no**.

---

## 3. SELECT: get data

```sql
SELECT * FROM customers;                    -- * = all columns
SELECT name, city FROM customers;           -- only these columns
SELECT * FROM orders ORDER BY amount DESC;  -- sort, biggest first
SELECT * FROM orders LIMIT 3;               -- only 3 rows
```

**Rules:** put text in 'single quotes' · end every query with `;` · `--` starts a comment (like `#` in Python).

---

## 4. WHERE: keep only some rows

![WHERE paid = 0 keeps 3 of the 7 orders](images/sql/02-where.png)

| SQL | Meaning |
|---|---|
| `=` | equal (Python uses `==`) |
| `!=` | not equal |
| `>` `<` `>=` `<=` | bigger / smaller |
| `AND` | both conditions are true |
| `OR` | at least one condition is true |

```sql
SELECT * FROM customers WHERE city = 'Cairo';
SELECT * FROM orders WHERE amount > 500;
SELECT * FROM orders WHERE paid = 0 AND amount > 500;
```

---

## 5. JOIN: connect two tables

The `orders` table says `customer_id = 2`. **Who is that?** `JOIN` finds out:

![JOIN matches customer_id with id and adds the customer name to each order](images/sql/03-join.png)

```sql
SELECT orders.id, customers.name, orders.product, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```

- `ON …` = **how the tables are related**.
- `orders.amount` = the `amount` column **from the `orders` table**.

---

## 6. GROUP BY: totals per group

| Function | Meaning |
|---|---|
| `COUNT(*)` | how many rows |
| `SUM(amount)` | add up |
| `AVG(amount)` | average |
| `MIN(amount)` / `MAX(amount)` | smallest / biggest |

![GROUP BY product puts the orders into 4 groups, then COUNT and SUM each group](images/sql/04-group-by.png)

```sql
SELECT product, COUNT(*) AS times_sold, SUM(amount) AS revenue
FROM orders
GROUP BY product;
```

`AS` gives the result column a clear name.

---

## 7. From a business question to SQL

Managers don't ask for SQL. They ask questions like *"How much did we sell?"* or *"Who still owes us money?"* Your job is to turn the question into SQL, in 3 steps.

**Step 1. Answer 3 questions first:**

1. **What** data do I need?
2. **Where** is it? Which tables?
3. **How** are the tables related? Which ids?

> *"How much money do our Cairo customers still owe us?"*
> 1. **What:** amount, paid, city
> 2. **Where:** `orders` and `customers`
> 3. **How:** `orders.customer_id = customers.id`

**Step 2. Spot the pattern.** Most business questions sound like one of these:

| The question sounds like… | Use | Example |
|---|---|---|
| "How much…?" · "How many…?" | `SUM()` · `COUNT()` | Total sales |
| "…per city? per product? per customer?" | `GROUP BY` | Sales per city |
| "Only the unpaid ones" · "only Cairo" | `WHERE` | Unpaid orders |
| "Who is the top…?" · "the best 3…?" | `ORDER BY … DESC` + `LIMIT` | Biggest customer |
| "…with the customer's name?" | `JOIN` | Orders with names |
| "Who has never…?" | `LEFT JOIN` (section 8) | Customers with no orders |

**Step 3. Write the SQL**, with the parts in this order:
`SELECT` → `FROM` → `JOIN … ON` → `WHERE` → `GROUP BY` → `HAVING` → `ORDER BY` → `LIMIT`

```sql
SELECT SUM(orders.amount) AS cairo_unpaid
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.city = 'Cairo' AND orders.paid = 0;
```

Result: **1000** (Ahmed 300 + Mona 700)

### The weekly dashboard: 4 numbers every manager asks for

| Business word | Meaning | Our shop |
|---|---|---|
| **Revenue** | All the money from all orders | 4000 |
| **Orders** | How many orders | 7 |
| **Average order value** | Revenue ÷ orders | 571.43 |
| **Unpaid (receivables)** | Money customers still owe us | 2200 |

```sql
SELECT SUM(amount)           AS revenue,
       COUNT(*)              AS orders,
       ROUND(AVG(amount), 2) AS average_order_value
FROM orders;

SELECT SUM(amount) AS unpaid FROM orders WHERE paid = 0;
```

> **Link to Odoo:** **Sales → Reporting** in Odoo shows numbers like these. SQL lets you ask your own questions too.

---

## 8. Quick topics: 7 small tools for more business questions

Each tool answers one more kind of question. Teach them fast, or try them at home.

**1. `DISTINCT`: remove repeats.** *"Which cities are our customers in?"*

```sql
SELECT DISTINCT city FROM customers;
```

3 cities (Cairo, Alexandria, Giza), not 5 rows.

**2. `IN`: any value from a list.** *"Show the laptop and monitor orders."*

```sql
SELECT * FROM orders WHERE product IN ('Laptop', 'Monitor');
```

Orders 1, 2, 5 and 7. It's a short way to write `product = 'Laptop' OR product = 'Monitor'`.

**3. `BETWEEN`: a range, great for dates.** *"Which orders came in the first half of September?"*

```sql
SELECT * FROM orders WHERE order_date BETWEEN '2026-09-01' AND '2026-09-15';
```

Orders 1 to 6. `BETWEEN` includes both ends.

**4. `LIKE`: search inside text.** *"Which products start with M?"*

```sql
SELECT DISTINCT product FROM orders WHERE product LIKE 'M%';
```

Monitor and Mouse. `%` means "any letters": `'M%'` starts with M, and `'%top'` ends with "top" (Laptop).

**5. `HAVING`: filter the groups.** *"Which customers ordered more than once?"* (our repeat customers)

```sql
SELECT customers.name, COUNT(*) AS orders
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.name
HAVING COUNT(*) > 1;
```

Ahmed, Mona and Sara, with 2 orders each. `WHERE` filters rows **before** grouping. `HAVING` filters the groups **after**.

**6. `CASE`: your own labels.** *"Show Paid and Unpaid instead of 1 and 0."*

```sql
SELECT id, amount, CASE WHEN paid = 1 THEN 'Paid' ELSE 'Unpaid' END AS status
FROM orders;
```

Business bonus: *"What % of our sales is already paid?"* (the collection rate)

```sql
SELECT ROUND(SUM(CASE WHEN paid = 1 THEN amount ELSE 0 END) * 100.0 / SUM(amount), 1) AS paid_percent
FROM orders;
```

**45.0**: 1800 of the 4000 is paid. Write `100.0`, not `100`, to keep the decimals.

**7. `LEFT JOIN`: find what's missing.** *"Which customers have never ordered?"*

```sql
SELECT customers.name
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
WHERE orders.id IS NULL;
```

**Khaled.** `JOIN` keeps only the matches. `LEFT JOIN` keeps every customer and leaves the order empty (`NULL`) when there is none. Business use: a list of customers to call.

> **Big tables (like Odoo's): keep queries fast**
> - Ask only for the columns you need, not `*`.
> - Add `LIMIT 20` while you explore.
> - Filter with `WHERE`, so you get back only the rows you need.
> - Searching by `id` is fast: the primary key has an **index**, like the index at the back of a book.

---

## 9. Common errors

Read the error like a Python traceback, fix **one** thing, and run again.

| Error | Why | Fix |
|---|---|---|
| `no such table: orderz` | Typo in the table name | `orders` |
| `no such column: nmae` | Typo in the column name | `name` |
| `no such column: Cairo` | Text without quotes | `'Cairo'` |
| `ambiguous column name: id` | Both tables have `id` | `orders.id` or `customers.id` |
| `near "FROM": syntax error` | Extra or missing comma | `SELECT name, city FROM …` |

---

## 10. Safety

- `SELECT` only **reads** data. It is always safe.
- `UPDATE` and `DELETE` **change** data. `DELETE FROM orders;` deletes **every** order.
- With **real company data (Odoo)**: practice on a copy, use read-only access, and never change data without review and a backup.

---

## 11. SQL vs NoSQL

Not every database uses tables. There are two big families.

**SQL:** the data is split into tables and linked by ids, like our practice database.

| orders.id | customer_id | product | amount | paid |
|---|---|---|---|---|
| 2 | 2 | Monitor | 1200 | 0 |

`customer_id = 2` points to the `customers` table: Sara, Alexandria.

**NoSQL (documents):** everything about the order is saved together, as JSON.

```json
{
  "id": 2,
  "customer": {"name": "Sara", "city": "Alexandria"},
  "product": "Monitor",
  "amount": 1200,
  "paid": false
}
```

| | SQL | NoSQL |
|---|---|---|
| **Shape** | Tables with fixed columns | Flexible documents, like JSON or Python dictionaries |
| **Links** | `JOIN` on ids | Related data is often saved inside the document |
| **Examples** | SQLite, PostgreSQL, MySQL | MongoDB, Firebase, Redis |
| **Good for** | Money, orders, invoices, reports | Data that changes shape: chat messages, logs, app events |

> **Rule of thumb:** start with SQL (PostgreSQL) unless you have a clear reason not to. Odoo uses PostgreSQL.
>
> **Link to Part A:** the `orders` list in `main.py` and the JSON in `lesson_3_toolkit.py` (section 5) already look like NoSQL documents.

> **Coming in Session 3:** in Django you write `Post.objects.filter(id=2)`, and Django runs `SELECT … WHERE id = 2` for you.
>
> **Coming in Session 5:** a third kind, the **vector database**, finds text by meaning. AI uses it to search your documents.

---

## 12. Practice

Try each question first, then click **Answer** to check.

**1. Show all orders for `Mouse`.**

<details><summary>Answer</summary>

```sql
SELECT * FROM orders WHERE product = 'Mouse';
```
Orders 3 and 6.
</details>

**2. Show customers from Alexandria.**

<details><summary>Answer</summary>

```sql
SELECT * FROM customers WHERE city = 'Alexandria';
```
Sara and Khaled.
</details>

**3. Show paid orders under 500.**

<details><summary>Answer</summary>

```sql
SELECT * FROM orders WHERE paid = 1 AND amount < 500;
```
Orders 4 (150) and 6 (250). Order 1 is exactly 500, so it is not "under 500".
</details>

**4. Show every order with the customer's name and city.**

<details><summary>Answer</summary>

```sql
SELECT orders.id, customers.name, customers.city, orders.product, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.id;
```
</details>

**5. Total sales per city?**

<details><summary>Answer</summary>

```sql
SELECT customers.city, SUM(orders.amount) AS total
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.city;
```
Alexandria 1450, Cairo 2400, Giza 150.
</details>

**6. Who still owes us money, and how much?**

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

**7. Challenge: who is our biggest customer?**

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

**8. Business: which products bring in the most money? Biggest first.**

<details><summary>Answer</summary>

```sql
SELECT product, SUM(amount) AS revenue
FROM orders
GROUP BY product
ORDER BY revenue DESC;
```
Monitor 1900, Laptop 1400, Mouse 550, Keyboard 150.
</details>

**9. Business: what is the average order value in each city?**

<details><summary>Answer</summary>

```sql
SELECT customers.city, ROUND(AVG(orders.amount), 2) AS average_order_value
FROM orders
JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.city;
```
Alexandria 725, Cairo 600, Giza 150.
</details>

---

## 13. Mini-project: Order report

Use Part A (Python) and Part B (SQL) together. **Commit after each step.**

**Step 1. Make your own projects repo (only once)**

1. Make a new folder called `my-projects` and open it in VS Code (**File → Open Folder**).
2. In **Source Control**, click **Initialize Repository**.
3. After your first commit, click **Publish Branch** and choose **private**.

Every mini-project gets its own folder in this repo. Make the first one: `s2-order-report`.

**Step 2. Python: `report.py`**

1. Copy `output/orders.csv` (made by `lesson_3_toolkit.py`) into `s2-order-report`.
2. In `report.py`, read the CSV and write 2 functions that **return** their answer:
   - `total_sales(orders)`: the total of all amounts
   - `unpaid_by_customer(orders)`: a dictionary like `{"Sara": 1200, "Ahmed": 300}`
3. Save both answers in `report.json`.

> **Hints:** CSV gives back text, so use `int(row["amount"])`. `paid` is the text `"True"` or `"False"`, so compare with `row["paid"] == "False"`. Start with `result = {}`. If the customer is already in it, add to their amount. If not, set it.

**Step 3. SQL: `my_queries.sql`**

1. Write **3 business questions** of your own. Answer *what, where, how* for each (section 7), then write the SQL.
2. Make one SQL error on purpose. Explain the message in your own words in a `--` comment.

**Step 4. Use AI as a tutor**

Paste one error message into Claude and ask: *"Explain this error in simple words. Don't fix my code."* Then fix it yourself.

**Teacher checklist (next session):** ☐ `report.json` has the right totals ☐ both functions use `return` ☐ 3 SQL questions answered ☐ at least 3 small commits with clear messages

---

## 14. Quick check

Answer in your own words first, then click **Answer**.

**1. What is the difference between `print` and `return` in a function?**

<details><summary>Answer</summary>

`print` shows a value on the screen. `return` gives the value back to the code that called the function, so you can save it in a variable and use it again. A function without `return` gives back `None`.
</details>

**2. What does `from shop_tools import format_egp` do?**

<details><summary>Answer</summary>

It opens the module `shop_tools.py` and takes the function `format_egp` from it, so you can use it in your file.
</details>

**3. How do you get `"Alexandria"` from this data?**

```python
data = {"customer": {"name": "Sara", "city": "Alexandria"}}
```

<details><summary>Answer</summary>

`data["customer"]["city"]`: first the key `"customer"`, then the key `"city"`.
</details>

**4. What is the difference between a class and an object?**

<details><summary>Answer</summary>

A class is a template, like an empty form: `Order`. An object is one filled-in copy: `order_1 = Order("Ahmed", 500, True)`. In Django (Session 3), the class is the table and each object is one row.
</details>

**5. SQL: how much unpaid money is there in each city?**

<details><summary>Answer</summary>

```sql
SELECT customers.city, SUM(orders.amount) AS unpaid
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE orders.paid = 0
GROUP BY customers.city;
```
Alexandria 1200, Cairo 1000.
</details>

---

<sub>DB Browser for SQLite screenshot: [sqlitebrowser/sqlitebrowser](https://github.com/sqlitebrowser/sqlitebrowser) (MPL 2.0 / GPL 3), with numbered boxes added. The diagrams were made for this lesson from the practice data.</sub>
