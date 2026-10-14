# Session 1 · Part B: Git + GitHub in VS Code

**Goal:** open a project, see what changed, save small checkpoints, try ideas on a branch, get updates, and undo a bad edit, all from the VS Code **Source Control** panel.

**Time:** about 90 minutes. The practice file is `main.py` from Part A.

---

## 1. The idea

- **Git** = save points for your project folder. If something breaks, you go back.
- **GitHub** = a website that keeps a copy of the project online.

Your project lives in two places:

```
Your files now  ──Commit──►  History (saved checkpoints)  ──Sync──►  GitHub
(working tree)                                            ◄──Sync──
```

> A change you did **not** commit has **no save point**. Git cannot bring it back.

### Words you need

| Word | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | One saved checkpoint, with a short message |
| **Diff** | The exact lines that changed |
| **Branch** | A separate copy of your work, for trying ideas |
| **Clone** | Download a project from GitHub |
| **Pull** | Get new changes from GitHub |
| **Push** | Send your commits to GitHub |

---

## 2. One-time setup

1. Install **Git** and **VS Code**.
2. Tell Git your name. This is the only time you need the terminal. In VS Code: **Terminal → New Terminal**, then:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

3. Open the **Source Control** panel: click the branch icon in the left bar, or press `Ctrl+Shift+G` (Mac: `Cmd+Shift+G`).

### The Source Control panel

```
SOURCE CONTROL                        ...   ← more actions (Pull, Branch, Undo…)
 ┌───────────────────────────────┐
 │ Message                       │          ← write your commit message here
 └───────────────────────────────┘
 [        ✓ Commit             ]          ← save the checkpoint
 ▾ Changes                    1
     main.py               M              ← click = see diff | + = stage | ↶ = discard
 ▾ Graph                                  ← your commit history
```

Bottom-left of the window (the **status bar**):

```
 ⎇ main   ⟳ 0↓ 1↑
   │        └─ ↓ new commits on GitHub / ↑ your commits not sent yet
   └─ the branch you are on (click to switch)
```

---

## 3. Clone (download) the project

1. Press `Ctrl+Shift+P` and type **Git: Clone**.
2. Paste the link: `https://github.com/Yousefeslam214/python.git`
3. Choose a folder on your laptop.
4. Click **Open** when VS Code asks.

You now have the project and its full history.

---

## 4. The daily loop: Change → Look → Stage → Commit

### Step 1: Change

Open `main.py`, change `name = "Yousef"` to your name, and **save** (`Ctrl+S`).

> VS Code only sees **saved** changes. A ● dot on the file tab means it isn't saved yet.

### Step 2: Look (status)

Open **Source Control**. `main.py` is now under **Changes** with a letter next to it:

| Letter | Meaning |
|---|---|
| **M** | Modified: the file changed |
| **U** | Untracked: a new file Git hasn't saved before |
| **D** | Deleted |

### Step 3: Read the diff

**Click `main.py`** in the list. A side-by-side view opens:

- **Left** = the last commit. **Red** = removed.
- **Right** = your file now. **Green** = added.

> **Always read the diff before you commit.** This is also how you will check AI edits later.

### Step 4: Stage

Hover over `main.py` and click **+**. It moves to **Staged Changes**, the list of changes that will go into the next commit.

### Step 5: Commit

Write a message in the box, like `Change name to my name`, then click **✓ Commit** (or press `Ctrl+Enter`).

> If you forget to stage, VS Code asks *"Would you like to stage all your changes and commit them directly?"* Click **Yes**.

### Step 6: See the history

Look at the **Graph** section at the bottom of the panel. Your commit is at the top. Click any commit to see what it changed.

### Good habits

- **Small commits**: one idea per commit.
- **Clear messages**: `Fix tax calculation`, not `update`.
- **Commit before any risky change**, so you have a safe point to go back to.

---

## 5. Branches: try ideas safely

A branch lets you experiment while `main` stays safe.

1. Click the branch name (**⎇ main**) in the status bar.
2. Choose **+ Create new branch…**, type `try-discount`, and press Enter.
3. Change `quantity = 3` to `quantity = 5` in `main.py`, save, then commit it.
4. Click the branch name again and choose **main**. Your change is gone from the file.
5. Switch back to **try-discount**. Your change is back. It was safe on the branch.

**Happy with it?** Switch to **main**, then **… → Branch → Merge…** and pick `try-discount`.

---

## 6. Get updates and share (Pull / Push)

| You want to… | Click |
|---|---|
| **Get** new changes from GitHub | **… → Pull** (do this **before** you start working) |
| **Send** your commits to GitHub | **Sync Changes ↑1**, the button that appears after you commit |
| Send a **new branch** for the first time | **Publish Branch** |

The first time, VS Code asks you to **sign in to GitHub**. Click **Allow** and finish in the browser. You need permission to push to the project, so ask your teacher.

---

## 7. Safe recovery: "I broke something!"

| Problem | What to click |
|---|---|
| I changed a file and want it back as it was | Hover the file → **↶ Discard Changes** |
| I want to throw away **all** my changes | Hover **Changes** → **↶ Discard All Changes** |
| I staged a file by mistake | Hover it in **Staged Changes** → **−** (Unstage) |
| I committed by mistake (not sent to GitHub yet) | **… → Commit → Undo Last Commit**. Your changes come back to the list. |
| I'm on the wrong branch | Click the branch name → pick the right one |
| I already sent a bad commit to GitHub | **Ask your teacher.** It's fixed with `git revert`. |

> ⚠️ **Discard is forever.** Click the file and read the diff first, so you know what you are throwing away.

### Stop and ask first if you see…

- A warning with **IRREVERSIBLE** or **DELETE** in it.
- A **merge conflict** (files marked **!** or with `<<<<<<<` lines).
- Anything that says **Force**.

---

## 8. Checking AI edits with Git

Later you will let AI tools (like Claude Code) change your files. Git is your safety net:

1. **Commit first**, so you have a clean checkpoint.
2. Let the AI make its change.
3. In **Source Control**, **click every changed file** and read the diff.
4. **Run the code** and check that it works.
5. Good → **Commit**. Bad → **Discard All Changes**, and you are back at your checkpoint.

---

## 9. Keep secrets out

- **Never commit passwords, API keys, or customer data.**
- The **`.gitignore`** file lists files Git should ignore (for example `.env`, where secrets go). More on this in Session 4.

---

## 10. Good to know: the same actions as commands

AI coding tools and error messages use these words, so learn what they mean:

| In VS Code | Command |
|---|---|
| Git: Clone | `git clone <url>` |
| The Changes list | `git status` |
| Click a file to see the diff | `git diff` |
| **+** Stage | `git add main.py` |
| **✓** Commit | `git commit -m "message"` |
| Graph | `git log --oneline` |
| Create new branch | `git switch -c try-discount` |
| Pull / Sync | `git pull` / `git push` |
| Discard Changes | `git restore main.py` |

---

## 11. Practice (homework)

1. **Checkpoint:** change `price` and `quantity` in `main.py` (Lesson 1, section 5). Run it, read the diff, then commit with a clear message.
2. **Branch:** create a branch called `practice`, change the greeting, commit, then switch between `main` and `practice` and watch the file change.
3. **Break and fix:** delete 5 lines from `main.py` and save. Read the diff, then **Discard Changes** to bring them back.
4. **Undo:** make a small commit, then use **Undo Last Commit**. What happened to your change?
5. **Explain it:** what is the difference between *your files now* and the *history*?
