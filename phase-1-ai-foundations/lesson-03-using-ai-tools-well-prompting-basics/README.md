# Lesson 3/48 · Phase 1: Using AI Tools Well: Prompting Basics

> **Why this matters:** Tools like ChatGPT, Claude and Gemini are only as useful as what you ask them. The same tool can give a vague, useless answer or exactly what you need. The difference is usually the **prompt**.

## The core idea

A **prompt** is the message you give an AI tool: your question, instruction or request.

Remember Lesson 2: a model learns patterns from examples and then makes predictions. A chatbot is a generative AI model that **predicts a good reply to your words**. It can't read your mind. It only knows what you put in the prompt, so **the clearer your prompt, the better its prediction**.

Think of the AI as a **very smart new assistant on their first day**. They know a lot about the world, but nothing about *you*, your situation or what "good" looks like to you. You have to tell them.

### The 4 ingredients of a good prompt

| Ingredient | Question it answers | Example |
|---|---|---|
| 🎯 **Task** | What exactly do you want? | "Write a short email…" |
| 📋 **Context** | What background does it need? | "…to my manager. I'm sick today and will miss the 10am meeting…" |
| 📐 **Format** | What should the answer look like? | "…under 80 words, polite, with a subject line." |
| 🔍 **Constraints / audience** | Who is it for? Any limits? | "…don't over-explain my illness." |

You don't need all four every time, but the more a task matters, the more of them you should include.

```
Vague prompt  ──►  AI guesses what you mean  ──►  generic answer
Clear prompt  ──►  AI knows what you mean    ──►  useful answer
```

### Everyday analogy: ordering at a tea stall ☕

- "One tea, please." → You get *a* tea. Maybe too sweet, maybe with milk you didn't want.
- "One ginger tea, less sugar, no milk, in a takeaway cup." → You get exactly your tea.

The tea maker was just as skilled both times. The second order simply gave them the information they needed.

## Worked example: same tool, two prompts

**❌ Vague prompt**

> Explain machine learning.

You'll get a long, textbook-style answer. It might be too technical, too long, or skip what you actually wanted.

**✅ Clear prompt**

> I'm a complete beginner learning AI (I just learned that ML means computers learn rules from examples). Explain **features** and **labels** using one everyday example about weather. Keep it under 100 words and end with one quick question to test me.

| Ingredient | Where it is in the prompt |
|---|---|
| Task | "Explain features and labels" |
| Context | "complete beginner… I just learned that ML means…" |
| Format | "one everyday example… under 100 words… end with one quick question" |
| Audience | "complete beginner" |

The second prompt takes 20 seconds longer to write, and saves you several rounds of "no, simpler please".

## It's a conversation, not a one-shot

You don't have to get the prompt perfect the first time. **Follow up and refine:**

- "Make it shorter."
- "Explain that like I'm 12."
- "Give me 3 more examples."
- "I didn't understand the part about labels. Can you explain it another way?"
- "Put that in a table."

The AI remembers the earlier messages in the same chat, so each follow-up builds on the last answer.

## ⚠️ Important limits to know

1. **AI can be confidently wrong.** It predicts *likely-sounding* text, so sometimes it makes up facts, numbers, quotes or links. This is called a **hallucination**. Double-check anything important (health, money, legal, dates, facts for school or work).
2. **It may not know recent events.** Most models learned from data up to a certain date.
3. **Don't paste private information.** Avoid passwords, bank details, ID numbers, or other people's personal data.
4. **You're still in charge.** Treat the answer as a first draft from an assistant, not the final word.

(Lesson 4 covers more ways to get better answers and to check them.)

## Try it yourself (15 min)

1. Pick a real thing you need help with this week (an email, a study topic, a trip plan, a recipe with what's in your fridge…).
2. Write a **vague prompt** for it and send it to an AI tool (ChatGPT, Claude or Gemini, all free). Save the answer.
3. Rewrite it as a **clear prompt** using the 4 ingredients (task, context, format, constraints/audience). Send it in a **new chat**. Save the answer.
4. Send **one follow-up** to improve the second answer.
5. Compare: which answer was more useful, and why?

### My answers

| Question | My answer |
|---|---|
| What I needed help with | |
| My vague prompt | |
| My clear prompt | |
| Which ingredients I used | |
| My follow-up message | |
| Which answer was better, and why? | |

## Go deeper (free)

**Google's "Prompt design strategies"** guide explains how to write clear instructions, give context and ask for a format.
👉 https://ai.google.dev/gemini-api/docs/prompting-strategies

## Quick check

1. What is a prompt?
2. Name the 4 ingredients of a good prompt.
3. Why does adding context help the AI give a better answer?
4. What is a "hallucination", and what should you do about it?
5. The answer was too long and technical. Do you need to start over?

## Next time

**Lesson 4: Better prompting: roles, examples, step-by-step, checking answers.**

---

<details>
<summary><b>Answers</b> (click to reveal)</summary>

1. The message you give an AI tool: your question, instruction or request.
2. Task, context, format, and constraints/audience.
3. The AI only knows what's in your prompt. Context tells it your situation so it doesn't have to guess.
4. When the AI confidently makes up something false (a fact, number, quote or link). Double-check anything important against a trusted source.
5. No. Send a follow-up like "make it shorter and simpler" in the same chat.

</details>
