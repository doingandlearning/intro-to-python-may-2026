# Python Environment & Dependencies (VS Code Workflow)

## 1. Open Your Project

* `File → Open Folder`
* Ensure the **Python extension (Microsoft)** is installed

---

## 2. Create a Virtual Environment (VS Code Way)

Open Command Palette:

```text
Cmd/Ctrl + Shift + P
```

Run:

```text
Python: Create Environment
```

Then:

1. Choose **Venv**
2. Choose your Python version (e.g. Python 3.11)
3. Select location → project root
4. Name it:

```text
.venv
```

5. If prompted, select **requirements.txt** (if it exists)

**What VS Code does:**

* Creates `.venv/`
* Selects the interpreter automatically
* Optionally installs dependencies

---

## 3. Confirm the Interpreter

Check the bottom status bar:

```text
Python 3.x (.venv)
```

If not set:

```text
Cmd/Ctrl + Shift + P → Python: Select Interpreter
```

Choose the `.venv` interpreter.

---

## 4. Open the Terminal (and Check It’s Activated)

```text
Terminal → New Terminal
```

### What you should see

When activated, your prompt will include:

```bash
(.venv) your-name@machine project-folder %
```

or on Windows:

```bash
(.venv) PS C:\path\to\project>
```

The **`(.venv)`** prefix confirms you’re inside the environment.

---

### If you don’t see `(.venv)`

Activate manually:

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\Activate.ps1
```

---

### Quick check (optional but useful)

```bash
which python
```

Expected:

```bash
.../project/.venv/bin/python
```

---

## 5. Install Dependencies

```bash
pip install requests
```

Packages are installed **inside `.venv` only**.

---

## 6. Save Dependencies

```bash
pip freeze > requirements.txt
```

Example:

```text
requests==2.31.0
```

---

## 7. Recreate Environment (New Machine / Teammate)

Open project in VS Code, then:

```text
Cmd/Ctrl + Shift + P → Python: Create Environment
```

* Choose **Venv**
* Select Python version
* Select `requirements.txt`

VS Code will:

* create `.venv`
* install dependencies
* configure interpreter

---

## 8. Run Your Code

Options:

* ▶️ Run button
* Right-click → “Run Python File in Terminal”
* Terminal:

```bash
python app.py
```

---

## 9. Add New Dependencies Later

```bash
pip install numpy
pip freeze > requirements.txt
```

---

## 10. Deactivate

```bash
deactivate
```

---

# Mental Model

* **`.venv`** → your isolated project environment
* **Interpreter selection** → what VS Code uses
* **Terminal activation (`(.venv)`)** → where packages install
* **`requirements.txt`** → reproducible blueprint

---

# Common Pitfalls

### Wrong interpreter selected

* Fix: `Python: Select Interpreter`

---

### No `(.venv)` in terminal

* You’re installing globally
* Fix: activate manually

---

### requirements.txt not updated

* Others can’t reproduce your setup
* Fix:

```bash
pip freeze > requirements.txt
```

---

### Multiple terminals open

* Each can have different state
* If unsure → open a new terminal

---

# One-Line Summary

> Create `.venv` with VS Code → check for `(.venv)` → install with pip → freeze to requirements.txt
