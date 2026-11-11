# Lesson 4/48 · Phase 1: Better Prompting: Roles, Examples, Step-by-Step, Checking Answers

> **Why this matters:** Lesson 3 gave you the basics (task, context, format, constraints). This lesson adds four techniques that professionals use every day to get answers that are more accurate, more consistent and easier to trust.

## The core idea

Four techniques, each fixing a common problem:

| Technique | Problem it fixes | One-line version |
|---|---|---|
| 🎭 **Give a role** | Answers are generic | "Act as a…" |
| 🧩 **Show examples** | Answers are in the wrong style or format | "Here's what I want it to look like…" |
| 🪜 **Ask for step-by-step** | Answers to tricky questions are wrong or rushed | "Work through it step by step…" |
| ✅ **Check the answer** | Answers might be made up (hallucinations) | "How sure are you? What could be wrong?" |

You can combine them in one prompt.

## 1. 🎭 Give the AI a role

Telling the AI **who to be** changes its vocabulary, depth and focus.

> ❌ "Explain what a neural network is."
>
> ✅ "**You are a patient school teacher** explaining to a 14-year-old. Explain what a neural network is, using one everyday analogy."

Other useful roles:

- "You are a strict interviewer for a junior data analyst job. Ask me one question at a time."
- "You are a friendly English tutor. Correct my grammar and explain each mistake."
- "You are a senior Python developer reviewing beginner code. Point out mistakes kindly."

**Why it works:** remember from Lesson 2 that a model learns patterns from examples. It has seen how teachers, interviewers and reviewers write, so a role points it towards that pattern.

## 2. 🧩 Show examples (few-shot prompting)

Instead of *describing* what you want, **show it**. Giving 1 to 3 examples is called **few-shot prompting** ("shots" = examples). Giving none is **zero-shot**.

**Example: sorting customer messages**

```
Sort each message as Complaint, Question or Praise.

Message: "My order arrived broken."          → Complaint
Message: "Do you deliver to Pune?"           → Question
Message: "Great service, thank you!"         → Praise

Message: "Why is my refund taking so long?"  →
```

The AI follows the pattern and answers **Complaint** (or Question), in exactly the same short format.

Notice: this is Lesson 2 again! Examples with labels → the model spots the pattern → it predicts the label for a new example. You're doing mini machine learning inside a prompt.

**Tips**

- Make examples **varied** (different kinds of messages), not three that look the same.
- Keep the **format identical** in every example, so the AI copies it.

## 3. 🪜 Ask for step-by-step thinking

For maths, logic, planning or anything with several parts, AI makes fewer mistakes when it **works through the problem in steps** instead of jumping to the answer. This is often called **chain-of-thought** prompting.

> ❌ "A shirt costs ₹800. It's 25% off, then there's 18% tax on the sale price. What do I pay?"
>
> ✅ "A shirt costs ₹800. It's 25% off, then there's 18% tax on the sale price. What do I pay? **Work it out step by step, then give the final answer on its own line.**"

Expected steps:

1. Discount: 25% of 800 = 200 → sale price = ₹600
2. Tax: 18% of 600 = 108
3. **Final: ₹708**

Showing the steps has a second benefit: **you can check each step yourself** and spot exactly where any mistake happened.

You can also break a big task into steps yourself:

> "First, list the main topics in this article. Then, for each topic, write one sentence summary. Finally, give me 3 quiz questions."

## 4. ✅ Check the answer

Lesson 3 warned that AI can be **confidently wrong**. Build checking into your habit:

**Ask the AI to check itself**

- "Double-check your answer. Is anything wrong or uncertain?"
- "How confident are you in each fact here? Mark any you're unsure about."
- "What's the strongest argument *against* your answer?"

**Check it yourself**

- **Facts, numbers, dates:** confirm with a trusted source (official website, textbook, Google search).
- **Links and references:** click them. AI sometimes invents links or book titles that don't exist.
- **Maths:** redo it with a calculator, using the steps it showed.
- **Code:** run it (you'll start doing this in Lesson 5!).
- **Ask a second tool:** paste the same question into a different AI and compare.

**Rule of thumb:** the more it matters (health, money, legal, school or work), the more you check.

## Worked example: all four together

> **You are an experienced travel planner** (🎭 role). I'm planning a 2-day trip to Jaipur on a ₹10,000 budget for 2 people, travelling by train from Delhi.
>
> Format each day like this example (🧩 example):
> **Day 1 – Morning:** Amber Fort (₹200/person entry) · **Afternoon:** … · **Evening:** …
>
> **First** estimate the costs for travel, food, stay and tickets, **then** build the plan so it fits the budget (🪜 step-by-step).
>
> At the end, list any prices or opening times I should double-check before I go (✅ checking).

## Try it yourself (20 min)

Use any free AI tool (ChatGPT, Claude or Gemini).

1. **Role:** Ask "What is overfitting in machine learning?" once with no role, then again starting with "You are a patient teacher explaining to a complete beginner…". Compare.
2. **Examples:** Write a few-shot prompt with 3 examples that turns a product name into a short, fun tagline. Then give it a new product.
3. **Step-by-step:** Ask a word problem (shopping discount, travel time, splitting a bill) with "work it out step by step". Check each step with a calculator.
4. **Checking:** Ask "Give me 3 facts about the history of AI, with the year for each." Then ask "How confident are you in each fact?" and verify one fact yourself on Google.

### My answers

| Technique | My prompt | What changed / what I noticed |
|---|---|---|
| 🎭 Role | | |
| 🧩 Examples | | |
| 🪜 Step-by-step | | |
| ✅ Checking | | |

## Go deeper (free)

**Learn Prompting** is a free, beginner-friendly course covering roles, few-shot and chain-of-thought prompting.
👉 https://learnprompting.org/docs/introduction

## Quick check

1. What does giving the AI a role change about its answer?
2. What is "few-shot" prompting?
3. Why does asking for step-by-step working help with maths and logic questions?
4. Name two ways to check an AI answer yourself.
5. How is few-shot prompting similar to what you learned in Lesson 2?

## Next time

**Lesson 5: Getting set up: Google Colab and running your first cell.**

---

<details>
<summary><b>Answers</b> (click to reveal)</summary>

1. Its style, vocabulary, depth and focus: it answers the way that kind of person would.
2. Giving the AI a few examples (usually 1 to 3) of what you want, so it copies the pattern and format.
3. The AI makes fewer mistakes when it works through the parts in order, and you can check each step to find any error.
4. Any two of: confirm facts with a trusted source, click the links, redo the maths, run the code, ask a second AI tool.
5. Both use labelled examples: the model sees examples with answers, spots the pattern, and predicts the answer for a new example.

</details>
