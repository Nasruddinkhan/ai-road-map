# Lesson 2/48 · Phase 1: How Machines "Learn" from Data

> **Why this matters:** "The model learned it from data" is the one sentence behind almost every AI tool. Once you see what that actually means (examples in, patterns found, predictions out), AI stops feeling like magic.

## The core idea

Regular programming and machine learning work in **opposite directions**:

- **Regular programming:** a person writes the **rules**, the computer applies them to data and gives **answers**.
- **Machine learning:** a person gives the computer **data plus the right answers**, and the computer works out the **rules** itself.

```
Regular programming:   Rules + Data      ──►  Answers
Machine learning:      Data + Answers    ──►  Rules (a "model")
```

The "rules" an ML system discovers are called a **model**. Once you have a model, you can give it new data it has never seen and it will make a **prediction**.

### The three building blocks

1. **Examples (data).** Lots of past cases. Each example has **features** (the facts we know) and usually a **label** (the right answer).
   - Features of a house: size, number of bedrooms, location.
   - Label: the price it sold for.
2. **Patterns (training).** The computer looks through the examples and adjusts itself, little by little, until its guesses match the labels as closely as possible. This step is called **training**.
3. **Predictions (using the model).** Give the trained model a *new* house's features and it predicts a price, even though nobody told it that house's price.

### Everyday analogy: learning to judge ripe mangoes 🥭

Nobody gives you a rulebook for picking a ripe mango. Instead:

- You **see and touch many mangoes** (examples), and someone tells you "this one's ripe, this one isn't" (labels).
- Over time you **notice patterns**: soft when pressed, sweet smell, a bit of give near the stem (features that matter).
- Now at the market you can **pick a mango you've never seen** and guess correctly (prediction).

You never wrote down the rules. You learned them from examples. That's machine learning.

## Worked example: predicting if a student passes

Here is a tiny training dataset:

| Hours studied | Hours slept | Passed? (label) |
|---|---|---|
| 1 | 4 | ❌ No |
| 2 | 8 | ❌ No |
| 5 | 7 | ✅ Yes |
| 6 | 5 | ✅ Yes |
| 8 | 8 | ✅ Yes |
| 3 | 6 | ❌ No |

**What pattern would a model find?** Roughly: *"students who studied about 4+ hours passed."* Sleep doesn't seem to matter much in this small set.

**New student, never seen before:** studied 7 hours, slept 6. The model predicts ✅ **Yes**.

Two important things to notice:

- **More (and better) examples = better patterns.** With only 6 rows, the model could easily be fooled. Real systems learn from thousands or millions of examples.
- **Garbage in, garbage out.** If the labels are wrong, or the examples only include one type of student, the model learns the wrong pattern. The data matters as much as the algorithm.

## Two types of prediction you'll meet a lot

| Type | Predicts… | Example |
|---|---|---|
| **Classification** | a category | Spam or not spam? Cat or dog? Pass or fail? |
| **Regression** | a number | House price, tomorrow's temperature, delivery time |

## Try it yourself (15 min)

Pick **one** everyday prediction task (ideas: "will it rain today?", "which video will I click next?", "is this transaction fraud?", "how long will my commute take?"). Then write down:

1. **Features:** what facts would the computer need to know? List at least 3.
2. **Label:** what's the "right answer" it learns from?
3. **Examples:** where would the past data come from?
4. **Type:** is it classification (a category) or regression (a number)?
5. **What could go wrong?** One way bad or missing data could teach the wrong pattern.

### My answers

| Question | My answer |
|---|---|
| Task | |
| Features | |
| Label | |
| Where the examples come from | |
| Classification or regression? | |
| What could go wrong? | |

## Go deeper (free)

**Google's "Introduction to Machine Learning"** course covers what ML is, features, labels and models, in short readable sections.
👉 https://developers.google.com/machine-learning/intro-to-ml

## Quick check

1. In machine learning, what do we give the computer, and what does it figure out?
2. In a dataset of emails marked "spam" or "not spam", what is the label?
3. Predicting tomorrow's temperature in °C: classification or regression?
4. Why can a model trained on bad data give bad predictions even if the algorithm is good?

## Next time

**Lesson 3: Using AI tools well: prompting basics.**

---

<details>
<summary><b>Answers</b> (click to reveal)</summary>

1. We give it examples (data plus the right answers). It figures out the rules, which we call a model.
2. "Spam" or "not spam" for each email.
3. Regression, because it predicts a number.
4. The model can only learn patterns that are in the data. If the data is wrong, biased or incomplete, it learns the wrong patterns ("garbage in, garbage out").

</details>
