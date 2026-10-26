# Session 3 · Part A: Django overview

**Goal:** understand how a web app works, and find your way around a real Django project, so you can read it and guide AI to change it.

**Time:** about 80 minutes · **Project:** [`demo_django/`](../demo_django/), a small "posts manager"

---

## 1. The idea: why a framework?

A website needs many parts: URLs, pages, a database, logins, security, a back office.

- **Without a framework**, you build every part yourself. It's like building a car from metal.
- **With a framework**, the engine, the wheels and the seats are ready. You build *your* car.

**Django** is a Python framework with "batteries included": a database layer, an admin back office, users and logins, and security. Instagram was built with Django.

| Tool | What it is | Use it when |
|---|---|---|
| **Django** | A full kit: pages, database, admin, users | You build a product with data and a back office |
| **FastAPI** | Small and fast, for APIs only | You only need an API: no admin, no pages |
| **Odoo** | A ready business system (ERP), built on its own Python framework | You need sales, stock and invoices: you customize it, you don't build it |

> **You don't need to write Django from memory.** From Session 4, AI writes the code. Your job: know where things are, read them, and check that they work.

---

## 2. How the web works

```
            request:  GET /api/posts/
 Browser  ─────────────────────────────►  Server (Django)
          ◄─────────────────────────────
            response: 200 OK + the page or the JSON
```

Every click is a **request**. The server sends back a **response**.

| Word | Meaning | Example |
|---|---|---|
| **URL** | The address | `http://127.0.0.1:8000/api/posts/` |
| **GET** | "Give me" (read) | Opening a page |
| **POST** | "Take this" (send) | Pressing **Save** on a form |
| **Status code** | How it went | `200` OK · `302` go to another page · `404` not found · `500` server error |
| **HTML** | A page for people | The posts page |
| **JSON** | Data for programs | `/api/posts/` |

`127.0.0.1` means "this computer". `8000` is the door (the port) that Django listens on.

---

## 3. Setup: run the demo (only once)

Open the course folder in VS Code and **Pull** (Session 1). Then open a terminal (**Terminal → New Terminal**). You should see `(.venv)` from Session 2.

```bash
pip install -r demo_django/requirements.txt    # install Django
cd demo_django                                 # go into the project folder
python manage.py migrate                       # create the tables
python manage.py loaddata sample_posts         # add sample topics and posts
python manage.py createsuperuser               # make your admin login
python manage.py runserver                     # start the website
```

- `createsuperuser` asks for a username, an email (you can leave it empty) and a password. The password stays invisible while you type. That's normal. If Django says the password is too common, choose a longer one.
- `runserver` prints `Starting development server at http://127.0.0.1:8000/`. **Ctrl+click** the link.
- To stop the server, click in the terminal and press **Ctrl+C**.

> **Next time** you only need two commands: `cd demo_django` and `python manage.py runserver`.

---

## 4. The restaurant: how a request travels

Think of Django as a restaurant:

```
 Browser ──"GET /"──► urls.py ──► views.py ──► models.py ──► database
(customer)            (waiter)     (chef)      (storeroom)
                                     │
                                     ▼
                       template (the plate) ──► response: the page
```

| Restaurant | Django | File |
|---|---|---|
| The customer orders | The browser asks for a URL | — |
| The waiter takes the order to the right chef | The URL list | `config/urls.py`, `posts/urls.py` |
| The chef cooks | The view: a Python function | `posts/views.py` |
| The storeroom has the ingredients | The model: the database tables | `posts/models.py` |
| The plate makes it look good | The template: HTML | `posts/templates/posts/post_list.html` |
| A takeaway box | JSON: the same data, without the plate | `/api/posts/` |

**The demo has 3 pages, and each one adds one step:**

| Open this | What runs | Why it matters |
|---|---|---|
| [`/hello/`](http://127.0.0.1:8000/hello/) | urls → view → text | The simplest page |
| [`/`](http://127.0.0.1:8000/) | urls → view → **model** → **template** | A real page with data |
| [`/api/posts/`](http://127.0.0.1:8000/api/posts/) | urls → view → model → **JSON** | Data for other programs |

**Follow one order, file by file.** Open each file in VS Code:

1. `config/urls.py`: everything that isn't `admin/` goes to the posts app.
   ```python
   path("", include("posts.urls")),    # every other URL: look in posts/urls.py
   ```
2. `posts/urls.py`: the address `/` goes to the view `post_list`.
   ```python
   path("", views.post_list),
   ```
3. `posts/views.py`: the view asks the model for the posts, newest first, and hands them to the template.
   ```python
   def post_list(request):
       posts = Post.objects.order_by("-created_at")
       return render(request, "posts/post_list.html", {"posts": posts})
   ```
4. `posts/models.py`: `Post` is the table the posts come from.
5. `post_list.html`: shows each post. `{{ ... }}` shows a value. `{% ... %}` is logic, like a loop.
   ```html
   {% for post in posts %}
       <p>{{ post.text }}</p>
   {% endfor %}
   ```

> **Try it:** open [`/abc/`](http://127.0.0.1:8000/abc/). You get a **404** page that lists every URL pattern Django tried, in order. That list is `urls.py`.

---

## 5. Project, app, manage.py, settings.py

- **Project** (`config/`) = the whole restaurant: the settings and the main URL list.
- **App** (`posts/`) = one department, with its own models, views, URLs and templates. A project can have many apps (`posts`, `users`, `payments`). Odoo modules work the same way.

**`manage.py` is the remote control:**

| Command | What it does |
|---|---|
| `python manage.py runserver` | Start the website on your computer |
| `python manage.py makemigrations` | Write down a change to the tables |
| `python manage.py migrate` | Apply the changes to the database |
| `python manage.py createsuperuser` | Make an admin login |
| `python manage.py loaddata sample_posts` | Load sample rows |
| `python manage.py shell` | Open Python, connected to your database |

**`config/settings.py` has 5 settings to know:**

| Setting | Meaning |
|---|---|
| `SECRET_KEY` | A secret password for the site. In Session 4 it moves to a `.env` file. |
| `DEBUG = True` | Show detailed error pages. Only on your computer, never on a live site. |
| `INSTALLED_APPS` | The apps the project uses. Ours, `'posts'`, is at the end. |
| `DATABASES` | Where the data lives: the file `db.sqlite3` |
| `TIME_ZONE` | `'Africa/Cairo'`, so times show in Cairo time |

---

## 6. Models = tables (link to Session 2)

A model is a Python **class** (Lesson 3, section 6). Django turns it into a **table**:

```python
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

This is the SQL that Django wrote for it, shown by `python manage.py sqlmigrate posts 0001` (simplified):

```sql
CREATE TABLE posts_post (
    id         integer PRIMARY KEY,
    text       text,
    created_at datetime,
    topic_id   bigint REFERENCES posts_topic (id)
);
```

| Python (`models.py`) | Database (Session 2) |
|---|---|
| `class Post` | The table `posts_post` |
| `text = models.TextField()` | The column `text` |
| `topic = models.ForeignKey(Topic, ...)` | The column `topic_id`: a **foreign key** to `posts_topic` |
| `id` (Django adds it for you) | The **primary key** |
| One `Post` object | One row |

**The ORM: Python instead of SQL.** You write Python, and Django writes the SQL:

| Django (Python) | The SQL Django runs |
|---|---|
| `Post.objects.all()` | `SELECT * FROM posts_post;` |
| `Post.objects.count()` | `SELECT COUNT(*) FROM posts_post;` |
| `Post.objects.filter(id=2)` | `SELECT * FROM posts_post WHERE id = 2;` |
| `Post.objects.order_by("-created_at")` | `… ORDER BY created_at DESC;` |
| `Post.objects.filter(topic__name="AI tips")` | `… JOIN posts_topic … WHERE posts_topic.name = 'AI tips';` |

`topic__name` (two underscores) means: follow the foreign key to the `Topic` table, then use its `name`. That's a `JOIN`.

> **Try it:** stop the server (Ctrl+C) and run `python manage.py shell`. Type one line at a time:
> ```python
> from posts.models import Post, Topic
> Post.objects.count()                                      # 4
> Post.objects.filter(topic__name="AI tips")                # the 2 AI posts
> print(Post.objects.filter(topic__name="AI tips").query)   # the SQL, with INNER JOIN
> ```
> Type `exit()` to leave. Django's printout leaves out the quotes around `AI tips`.

**Migrations: the history of your tables.** The table structure has a history, like Git's history for your files:

| Command | What it does |
|---|---|
| `makemigrations` | Writes each change into a new file in `posts/migrations/`, like a commit |
| `migrate` | Applies the new files to the database, so the database matches the history |

We already made the first migration for you (`0001_initial.py`). That's why you only ran `migrate`. In Session 4, Claude Code adds a new migration when it adds columns.

---

## 7. The admin: a free back office

Open [`/admin/`](http://127.0.0.1:8000/admin/) and log in with your superuser.

1. Click **Topics → Add topic**. Type `Events` and press **Save**.
2. Click **Posts → Add post**. Choose a topic, write a text, and press **Save**.
3. Open [`/`](http://127.0.0.1:8000/) and [`/api/posts/`](http://127.0.0.1:8000/api/posts/). Your post is there.

You wrote **no** form and **no** list page. Django made them from the models, like the back office in Odoo.

`posts/admin.py` decides what the admin shows:

```python
class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "topic", "created_at"]    # the columns in the list
```

> In Session 4, Claude Code adds a filter here. Part B writes the spec for it.

---

## 8. Good to know (overview only)

| Topic | In one line | Where you saw it |
|---|---|---|
| **Forms** | How a user sends data to the server (a POST) | The **Add post** page in the admin |
| **Users and permissions** | Who can log in, and what each person may do | **Users** and **Groups** in the admin |
| **JSON API** | The takeaway box: the data without the HTML | `/api/posts/`. React reads it in Session 4, n8n in Session 6. |

---

## 9. Where to look: the project map

```
demo_django/
├── manage.py              the remote control
├── requirements.txt       the packages to install (Django)
├── db.sqlite3             the database file (made by migrate, not saved in Git)
├── config/                the PROJECT: settings for everything
│   ├── settings.py        house rules: apps, database, time zone
│   └── urls.py            the main URL list
└── posts/                 the APP: everything about posts
    ├── models.py          the tables (storeroom)
    ├── views.py           the code for each page (chef)
    ├── urls.py            the URLs of this app (waiter)
    ├── admin.py           what the admin shows (back office)
    ├── templates/posts/   the HTML pages (plates)
    ├── migrations/        the history of table changes
    └── fixtures/          the sample data
```

> **Before you change anything, ask: is it a URL, a page's logic, a table, or how it looks?** Then you know which file to open, and what to tell the AI.

---

## 10. Common errors

Read them like a Python traceback (Lesson 2): the last line first.

| Error | Why | Fix |
|---|---|---|
| `No module named 'django'` | Django isn't installed in the Python you're using | Check that you see `(.venv)`, then run `pip install -r requirements.txt` |
| `can't open file 'manage.py'` | You're in the wrong folder | `cd demo_django` |
| `no such table: posts_post` | The tables don't exist yet | `python manage.py migrate` |
| `That port is already in use` | Another server is still running | Stop it with Ctrl+C, or run `python manage.py runserver 8001` |
| `Page not found (404)` | That URL isn't in `urls.py` | Read the list on the 404 page |
| `TemplateDoesNotExist` | The template's name or folder is wrong | It must be `posts/templates/posts/post_list.html` |

---

<sub>The demo uses Django 5.2, a long-term support (LTS) version.</sub>
