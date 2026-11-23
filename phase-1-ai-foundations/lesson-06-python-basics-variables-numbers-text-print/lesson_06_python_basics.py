# Lesson 6: Python basics - variables, numbers, text, print
# Run this in Google Colab (paste each section into its own cell)
# or on your computer with:  python lesson_06_python_basics.py

# --- 1. print: show something on the screen ---
print("Hello, AI!")
print("Lesson", 6, "of", 48)

# --- 2. Variables: a name that stores a value ---
name = "Sara"          # change to your name
city = "Delhi"          # change to your city
lessons_done = 5
print(name)
print(city)
print(lessons_done)

# A variable can be updated
lessons_done = lessons_done + 1
print("Lessons done now:", lessons_done)

# --- 3. Numbers: int (whole) and float (decimal) ---
total_lessons = 48          # int
progress = 6 / 48           # float
print(type(total_lessons))  # <class 'int'>
print(type(progress))       # <class 'float'>

print(10 + 3)    # 13   add
print(10 - 3)    # 7    subtract
print(10 * 3)    # 30   multiply
print(10 / 3)    # 3.333...  divide (always gives a float)
print(10 // 3)   # 3    whole-number division
print(10 % 3)    # 1    remainder
print(2 ** 3)    # 8    power (2 x 2 x 2)

print(round(10 / 3, 2))  # 3.33

# --- 4. Text (strings) ---
greeting = "Hello"
print(greeting + ", " + name)   # joining text with +
print(name.upper())             # SARA
print(name.lower())             # sara
print(len(name))                # number of characters
print("-" * 20)                 # repeat text

# --- 5. f-strings: put variables inside text ---
percent = lessons_done / total_lessons * 100
print(f"{name} from {city} has finished {lessons_done} of {total_lessons} lessons.")
print(f"Progress: {percent:.1f}%")

# --- 6. Converting between types ---
age_text = "30"            # this is text, not a number
age = int(age_text)        # convert text -> int
print(age + 1)             # 31
print("Age: " + str(age))  # convert int -> text before joining

# --- 7. Mini project: AI course progress card ---
weeks_left = (total_lessons - lessons_done) / 3   # 3 lessons per week
print("=" * 30)
print("   AI ROAD MAP PROGRESS")
print("=" * 30)
print(f"Learner     : {name}")
print(f"Done        : {lessons_done}/{total_lessons}")
print(f"Progress    : {percent:.1f}%")
print(f"Weeks left  : {weeks_left:.1f}")
print("=" * 30)
