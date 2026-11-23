# Lesson 6/48 · Phase 1: Python Basics: Variables, Numbers, Text, Print

> **Why this matters:** Every AI program, from a tiny chart to ChatGPT's training code, is built from these same building blocks: storing values, doing maths on numbers, working with text and showing results. Learn them once and you'll use them in every lesson after this.

📄 **Code for this lesson:** [`lesson_06_python_basics.py`](lesson_06_python_basics.py). Paste each section into its own cell in Google Colab (Lesson 5) and run it.

## The core idea

| Building block | What it does | Example |
|---|---|---|
| `print()` | Shows something on the screen | `print("Hello")` |
| **Variable** | A **name** that stores a **value** | `age = 30` |
| **Numbers** | Whole numbers (`int`) and decimals (`float`) | `48`, `12.5` |
| **Text** (`str`) | Words and characters, inside quotes | `"Delhi"` |

### Everyday analogy: labelled jars 🫙

A variable is like a **jar with a label** in your kitchen.

- The **label** is the variable name: `sugar`.
- What's **inside** is the value: `500` (grams).
- You can **look inside** (`print(sugar)`), **use it** in a recipe (`sugar - 100`), or **refill it** with something new (`sugar = 1000`).

```
 ┌─────────┐   ┌─────────┐   ┌─────────┐
 │  name   │   │  city   │   │lessons  │   ← labels (variable names)
 │ "Sara"  │   │ "Delhi" │   │    6    │   ← values inside
 └─────────┘   └─────────┘   └─────────┘
```

## 1. `print()`: show something

```python
print("Hello, AI!")
print("Lesson", 6, "of", 48)
```

Output:

```
Hello, AI!
Lesson 6 of 48
```

Separate several things with commas and `print` puts a space between them.

## 2. Variables: store a value

```python
name = "Sara"
city = "Delhi"
lessons_done = 5

print(name)          # Sara
print(lessons_done)  # 5
```

The `=` sign means **"store the value on the right in the name on the left"**. It is *not* "equals" like in maths.

You can **update** a variable:

```python
lessons_done = lessons_done + 1
print(lessons_done)  # 6
```

Read it right to left: "take `lessons_done` (5), add 1, store the result back in `lessons_done`".

**Naming rules**

- ✅ Letters, numbers and `_`: `total_lessons`, `price2`
- ✅ Use clear names: `monthly_salary` beats `x`
- ❌ Can't start with a number: `2price`
- ❌ No spaces: `my name`
- ⚠️ Case matters: `Name` and `name` are two different variables

## 3. Numbers: `int` and `float`

- `int` = whole number: `48`, `-3`, `0`
- `float` = decimal number: `12.5`, `3.14`

```python
print(type(48))     # <class 'int'>
print(type(12.5))   # <class 'float'>
```

`type()` tells you what kind of value something is.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | add | `10 + 3` | `13` |
| `-` | subtract | `10 - 3` | `7` |
| `*` | multiply | `10 * 3` | `30` |
| `/` | divide | `10 / 3` | `3.3333333333333335` |
| `//` | whole-number divide | `10 // 3` | `3` |
| `%` | remainder | `10 % 3` | `1` |
| `**` | power | `2 ** 3` | `8` |

- `/` **always** gives a `float`, even `10 / 2` gives `5.0`.
- Use `round(value, 2)` to keep 2 decimal places: `round(10 / 3, 2)` → `3.33`.
- Maths order works like school (BODMAS): `2 + 3 * 4` is `14`, `(2 + 3) * 4` is `20`.

## 4. Text (strings)

Text goes inside quotes, `"double"` or `'single'`. Python calls text a **string** (`str`).

```python
name = "Sara"
greeting = "Hello"

print(greeting + ", " + name)  # Hello, Sara     (join with +)
print(name.upper())            # SARA
print(name.lower())            # sara
print(len(name))               # 4               (number of characters)
print("-" * 20)                # --------------------
```

## 5. f-strings: put variables inside text

The easiest way to mix text and variables. Put an `f` before the quotes and variables inside `{ }`:

```python
lessons_done = 6
total_lessons = 48
percent = lessons_done / total_lessons * 100

print(f"{name} from {city} has finished {lessons_done} of {total_lessons} lessons.")
print(f"Progress: {percent:.1f}%")
```

Output:

```
Sara from Delhi has finished 6 of 48 lessons.
Progress: 12.5%
```

`:.1f` means "show 1 decimal place". You'll use f-strings constantly.

## 6. Text vs numbers (a very common mistake!)

`"30"` (in quotes) is **text**. `30` is a **number**. They don't mix:

```python
age_text = "30"
print(age_text + 1)   # ❌ TypeError: can only concatenate str (not "int") to str
```

Convert first:

```python
age = int(age_text)      # text → int
print(age + 1)           # 31

print("Age: " + str(age))  # int → text, so it can be joined
```

| Function | Converts to | Example |
|---|---|---|
| `int()` | whole number | `int("30")` → `30` |
| `float()` | decimal | `float("2.5")` → `2.5` |
| `str()` | text | `str(30)` → `"30"` |

This matters in AI: data loaded from files often arrives as **text**, and you must convert it to numbers before doing maths (you'll see this with Pandas in Lesson 12).

## Worked example: AI course progress card

```python
name = "Sara"
lessons_done = 6
total_lessons = 48

percent = lessons_done / total_lessons * 100
weeks_left = (total_lessons - lessons_done) / 3   # 3 lessons per week

print("=" * 30)
print("   AI ROAD MAP PROGRESS")
print("=" * 30)
print(f"Learner     : {name}")
print(f"Done        : {lessons_done}/{total_lessons}")
print(f"Progress    : {percent:.1f}%")
print(f"Weeks left  : {weeks_left:.1f}")
print("=" * 30)
```

Output:

```
==============================
   AI ROAD MAP PROGRESS
==============================
Learner     : Sara
Done        : 6/48
Progress    : 12.5%
Weeks left  : 14.0
==============================
```

## Try it yourself (20 min)

In a new Colab notebook called `Lesson_06_Python_Basics`:

1. **About me:** create variables `name`, `city` and `age`. Print one sentence using an f-string: *"My name is …, I live in … and I am … years old."*
2. **Age maths:** print your age in months, and roughly in days (`age * 365`).
3. **Shopping bill:** a shirt costs `800`, it's `25` percent off, then `18` percent tax on the sale price (the problem from Lesson 4). Store each value in a variable and calculate the final price in Python. Do you get `708.0`?
4. **Text tricks:** print your name in UPPERCASE, and print how many letters it has.
5. **Fix the error:** run this, read the error, then fix it:

   ```python
   score = "45"
   print(score + 5)
   ```

6. **Bonus:** edit the progress card above with your own name and real number of lessons done.

### My answers

| Task | My code | Output |
|---|---|---|
| About me sentence | | |
| Age in months / days | | |
| Shopping bill | | |
| Name in uppercase + length | | |
| Fixed error | | |

## Go deeper (free)

**The official Python tutorial: "An Informal Introduction to Python"** covers numbers, text and variables with lots of short examples.
👉 https://docs.python.org/3/tutorial/introduction.html

## Quick check

1. What does `=` mean in Python?
2. What's the difference between an `int` and a `float`?
3. What is `10 // 3`, and what is `10 % 3`?
4. Which is a valid variable name: `2price`, `my price` or `my_price`?
5. Why does `"5" + 5` give an error, and how do you fix it?
6. What will `print(f"I have {3 * 2} apples")` show?

## Next time

**Lesson 7: Lists and dictionaries** (storing many values at once). This also starts **Phase 2: Python for AI**. 🎉

---

<details>
<summary><b>Answers</b> (click to reveal)</summary>

1. Store the value on the right in the variable name on the left (it's not "equals" like in maths).
2. An `int` is a whole number (`48`), a `float` has a decimal point (`12.5`).
3. `10 // 3` is `3` (whole-number division). `10 % 3` is `1` (the remainder).
4. `my_price`. Names can't start with a number or contain spaces.
5. `"5"` is text and `5` is a number, and Python won't add them. Use `int("5") + 5` (gives `10`) or `"5" + str(5)` (gives `"55"`).
6. `I have 6 apples`.

</details>
