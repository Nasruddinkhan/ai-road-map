# Lesson 5/48 · Phase 1: Getting Set Up: Google Colab and Running Your First Cell

> **Why this matters:** From now on you'll write real code. Google Colab lets you run Python in your browser for free, with nothing to install, and it's the same tool many AI researchers and students use to train models.

## The core idea

- **Python** is the most popular programming language for AI. Almost every AI library (NumPy, Pandas, scikit-learn, PyTorch) is written for Python.
- **Google Colab** ("Colaboratory") is a free website from Google where you write and run Python in a **notebook**. The code runs on Google's computers, not yours, so even an old laptop works. It can even give you a free **GPU** (a chip that makes deep learning much faster) later in the course.
- A **notebook** is a document made of **cells**:
  - **Code cells** hold Python code you can run.
  - **Text cells** hold notes, headings and explanations.

```
┌──────────────────────────────────────────┐
│ 📓 My_First_Notebook.ipynb                │
├──────────────────────────────────────────┤
│ [Text]  # My first notebook               │
├──────────────────────────────────────────┤
│ [▶ Code] print("Hello, AI!")              │
│          Hello, AI!          ← output     │
├──────────────────────────────────────────┤
│ [▶ Code] 2 + 3                            │
│          5                   ← output     │
└──────────────────────────────────────────┘
```

### Everyday analogy: a recipe notebook with a built-in kitchen 🍳

Imagine a recipe notebook where every recipe card has a **"Cook" button**. Press it and the dish appears right under the card. You can change the recipe, press again, and instantly see the new result. Text cells are your notes in the margin. That's a Colab notebook.

## Step by step: set up Colab

1. **Get a Google account.** Your Gmail account works.
2. **Open Colab:** go to 👉 https://colab.research.google.com
3. **Create a notebook:** click **New notebook** (or **File → New notebook in Drive**).
4. **Rename it:** click the title `Untitled0.ipynb` at the top-left and change it to `Lesson_05_First_Notebook`.
   - `.ipynb` is the file type for notebooks ("IPython notebook").
5. **Where is it saved?** Automatically in your Google Drive, in a folder called **Colab Notebooks**.

## Running your first cell

1. Click inside the empty code cell and type:

   ```python
   print("Hello, AI!")
   ```

2. Run it in either of these ways:
   - Click the **▶ play button** on the left of the cell, **or**
   - Press **Shift + Enter** (runs the cell and moves to the next one).
3. The first run takes a few seconds while Colab **connects** to a Google computer (look for "Connecting" / a green tick and "RAM / Disk" at the top-right).
4. You'll see the output under the cell:

   ```
   Hello, AI!
   ```

🎉 You just ran your first Python code.

### Try a few more cells

Click **+ Code** to add a new cell, then run each of these one at a time:

```python
2 + 3
```

```python
10 * 7
```

```python
print("I am learning AI")
```

```python
100 / 4
```

Notice: the **last line** of a cell shows its result automatically (`5`, `70`, `25.0`). `print(...)` is how you show text on purpose. You'll learn exactly how this works in Lesson 6.

### Add a text cell

Click **+ Text** and type:

```
# Lesson 5: My first notebook
Today I learned to run Python in Google Colab.
```

The `#` makes it a heading. Click outside the cell to see it formatted.

## Useful things to know

| Thing | What it means |
|---|---|
| **Shift + Enter** | Run the cell, go to the next one |
| **Ctrl + Enter** | Run the cell, stay on it |
| **+ Code / + Text** | Add a new code or text cell |
| **Runtime → Restart session** | Fresh start if things get stuck (your code stays, results are cleared) |
| **Runtime → Run all** | Run every cell from top to bottom |
| **Red error message** | Normal! Read the **last line** of it; it usually tells you what went wrong |
| **Disconnected after a while** | Colab stops idle sessions. Just run the cell again; your notebook is still saved |

### Your first error (on purpose)

Run this cell:

```python
print("Hello)
```

You'll get a `SyntaxError` because the closing `"` is missing. Fix it to `print("Hello")` and run again. Errors aren't failures; they're the computer telling you exactly what to fix. Every programmer sees dozens a day.

💡 **Tip from Lesson 4:** if you don't understand an error, paste the code and the error into an AI tool and ask "Explain this error to a beginner and show the fix." Then **run the fix** to check it.

## Try it yourself (15 min)

1. Create a notebook called `Lesson_05_First_Notebook`.
2. Add a **text cell** with a heading and one sentence about why you're learning AI.
3. Add **code cells** that:
   - print your name
   - print your city
   - calculate how many weeks the 48 lessons take at 3 lessons a week (`48 / 3`)
   - calculate your age in months (`your_age * 12`)
4. Make one error on purpose, read the last line of the message, and fix it.
5. **Bonus:** click **File → Save a copy in GitHub** (or download it via **File → Download → .ipynb**) and add it to this lesson's folder in this repo.

### My answers

| Task | My code | Output |
|---|---|---|
| Print my name | | |
| Print my city | | |
| Weeks for 48 lessons | | |
| My age in months | | |
| Error I made and how I fixed it | | |

## Go deeper (free)

**Google's official "Welcome to Colab"** notebook is a short, interactive tour of everything Colab can do.
👉 https://colab.research.google.com/notebooks/intro.ipynb

## Quick check

1. What is Google Colab, and why don't you need to install anything?
2. What are the two types of cells in a notebook?
3. What keyboard shortcut runs a cell?
4. You see a red error message. What's the first thing to look at?
5. Where are your Colab notebooks saved?

## Next time

**Lesson 6: Python basics: variables, numbers, text, print.**

---

<details>
<summary><b>Answers</b> (click to reveal)</summary>

1. A free website from Google for writing and running Python in a notebook. The code runs on Google's computers, so everything is already set up in the browser.
2. Code cells (run Python) and text cells (notes and headings).
3. Shift + Enter (or Ctrl + Enter to stay on the same cell).
4. The last line of the error. It usually names the type of error and what went wrong.
5. In your Google Drive, in the "Colab Notebooks" folder.

</details>
