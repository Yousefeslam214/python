# Session 1 · Part B: Git + GitHub Basics

**Goal:** By the end you can download a project, save your work in small checkpoints, try ideas safely on a branch, check every change, and undo mistakes.

**Time:** about 90 minutes. You will use `main.py` from Part A as the practice file.

---

## 1. Why Git?

- **Git** keeps **save points** for your project folder, like saves in a video game. If something breaks, you can go back.
- **GitHub** is a website that keeps a copy of your project online, so you can share it, back it up, and download it on another laptop.

Git runs on your laptop. GitHub is on the internet. Git works without GitHub, but GitHub needs Git.

---

## 2. Words you need

| Word | Simple meaning |
|---|---|
| **Repository (repo)** | A project folder that Git is tracking. |
| **Working tree** | The files you see and edit right now. |
| **Staging** | Choosing which changes go into the next save (`git add`). |
| **Commit** | A saved snapshot of your files, with a short message. |
| **History** | The list of all commits (`git log`). |
| **Branch** | A separate line of work. You can try things without touching `main`. |
| **Remote / origin** | The copy of the repo on GitHub. |
| **Clone** | Download a repo from GitHub for the first time. |
| **Pull** | Get the newest commits from GitHub. |
| **Push** | Send your commits to GitHub. |
| **Diff** | The exact lines that changed. |

### How changes move

```
Working tree --git add--> Staging --git commit--> History --git push--> GitHub
                                                  History <--git pull-- GitHub
```

**Important:** a change you have not committed has **no save point** yet. Git cannot bring it back if you lose it.

---

## 3. One-time setup

Open a terminal. In VS Code that's **Terminal → New Terminal**; on Windows you can also use **Git Bash**.

```bash
git --version
```

If you see a version number, Git is installed. Now tell Git who you are. This name is written on every commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 4. Clone a project

```bash
git clone https://github.com/Yousefeslam214/python.git
cd python
```

You now have the project folder on your laptop, with its full history. Open it in VS Code:

```bash
code .
```

---

## 5. The daily loop: status → diff → add → commit

You will repeat this loop every time you work.

### Step 1: Make a change

Open `main.py` and change this line to your own name:

```python
name = "Yousef"
```

### Step 2: `git status` (what changed?)

```bash
git status
```

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.py
```

`modified: main.py` means the file changed but is **not saved in Git yet**.

### Step 3: `git diff` (show me exactly what changed)

```bash
git diff
```

Shortened output:

```diff
-name = "Yousef"
+name = "Mona"
```

- Lines starting with `-` were **removed**.
- Lines starting with `+` were **added**.

Press `q` to exit if the screen doesn't return to normal.

> **Always read the diff before you commit.** This habit catches mistakes, and it is how you will check changes made by AI tools later.

### Step 4: `git add` (choose what to save)

```bash
git add main.py
git status
```

```
Changes to be committed:
	modified:   main.py
```

### Step 5: `git commit` (create the save point)

```bash
git commit -m "Change name to my name"
```

### Step 6: `git log` (see the history)

```bash
git log --oneline
```

```
37d11b6 Change name to my name
61e6a89 first commit
```

Each commit has an **ID** (like `37d11b6`). Your IDs will be different. You use this ID to look at or undo a commit.

### Good commit habits

- **Small commits.** One idea per commit.
- **Clear messages.** Say what changed: `Fix tax calculation`, not `update` or `stuff`.
- **Commit before risky changes**, so you always have a safe point to go back to.

---

## 6. Branches: try things safely

A branch is a copy of your work where you can experiment. `main` stays safe.

```bash
git branch                      # list branches (* = the one you are on)
git switch -c try-discount      # create a new branch and move to it
```

Now change something in `main.py`, for example `quantity = 3` → `quantity = 5`. Then commit:

```bash
git add main.py
git commit -m "Try bigger quantity"
```

Switch back and watch the file:

```bash
git switch main            # your change is gone from the file...
git switch try-discount    # ...and it's back. It was safe on the branch.
```

When you are happy with the branch, bring its changes into `main`:

```bash
git switch main
git merge try-discount
```

---

## 7. Pull and push (working with GitHub)

```bash
git pull     # get the newest changes from GitHub. Do this BEFORE you start working.
git push     # send your commits to GitHub.
```

The first time you push a **new branch**:

```bash
git push -u origin try-discount
```

The first push asks you to sign in to GitHub. You need permission to push to the repo, so ask your teacher.

---

## 8. Safe recovery: "I broke something!"

| Situation | Command | What it does |
|---|---|---|
| I changed a file and want to **throw away** my changes (not committed) | `git restore main.py` | Puts the file back to the last commit. |
| I want to throw away **all** uncommitted changes | `git restore .` | Same, for every file. |
| I ran `git add` by mistake | `git restore --staged main.py` | Takes it out of staging. Your edits stay. |
| I **committed** something bad | `git revert --no-edit <commit-id>` | Makes a **new** commit that undoes the bad one. History is kept. |
| I want to see an old commit | `git show <commit-id>` | Shows what that commit changed. |
| I'm on the wrong branch | `git switch main` | Moves you to `main`. |

> ⚠️ `git restore` deletes uncommitted changes **forever**. Run `git diff` first so you know what you are throwing away.

### Danger zone: do not use these without asking first

| Command | Why it's dangerous |
|---|---|
| `git reset --hard` | Deletes uncommitted work with no undo. |
| `git push --force` | Can delete other people's work on GitHub. |
| `git clean -fd` | Deletes untracked files permanently. |

---

## 9. Git + AI coding tools

Later in the program you will let AI tools (like Claude Code) edit your files. Git is your safety net:

1. **Commit first**, so you have a clean checkpoint.
2. Let the AI make its change.
3. Run **`git diff`** and read every changed line.
4. **Run the code** and check that it works.
5. Good → `git add` + `git commit`. Bad → `git restore .` and you're back to step 1.

---

## 10. Keep secrets out of Git

- **Never commit passwords, API keys, or customer data.**
- A file called **`.gitignore`** lists files that Git should ignore (for example `.env`, which is where secrets go).
- Once a secret is pushed to GitHub, treat it as **leaked**, even if you delete it later. It is still in the history.

We'll cover this more in Session 4.

---

## 11. Cheat sheet

| Command | Use it to… |
|---|---|
| `git clone <url>` | Download a repo for the first time |
| `git status` | See what changed |
| `git diff` | See exactly which lines changed |
| `git add <file>` | Choose a file for the next commit |
| `git commit -m "message"` | Save a checkpoint |
| `git log --oneline` | See the history |
| `git branch` | List branches |
| `git switch -c <name>` | Create a branch and move to it |
| `git switch <name>` | Move to a branch |
| `git merge <name>` | Bring a branch's changes into the current branch |
| `git pull` | Get the newest changes from GitHub |
| `git push` | Send your commits to GitHub |
| `git restore <file>` | Throw away uncommitted changes in a file |
| `git revert --no-edit <id>` | Undo a commit safely |

---

## 12. Practice (homework)

Do these on your own laptop, in the project folder.

1. **Checkpoint:** change `price` and `quantity` in `main.py` (Lesson 1, section 5). Run the file, then `status` → `diff` → `add` → `commit` with a clear message.
2. **Branch:** create a branch called `practice`, change the greeting in `main.py`, commit, then switch between `main` and `practice` and watch the file change.
3. **Break and restore:** delete 5 lines from `main.py` on purpose. Run `git diff` to see them, then `git restore main.py` to bring them back.
4. **Undo a commit:** make a small commit, then undo it with `git revert --no-edit <commit-id>`. Check `git log --oneline`. What do you see?
5. **Explain it:** in your own words, what is the difference between the *working tree* and the *commit history*?
