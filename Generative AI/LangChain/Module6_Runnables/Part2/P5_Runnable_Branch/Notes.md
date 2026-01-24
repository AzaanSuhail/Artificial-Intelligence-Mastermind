## 🧠 What is `RunnableBranch`?

`RunnableBranch` is a **control-flow runnable** that allows **conditional routing** between multiple runnable paths.

Think of it like an **“if-elif-else”** for your LangChain pipelines.

It evaluates a set of **conditions (functions)** in order, and when one returns `True`, it executes the corresponding runnable (or chain).

If none match, it runs the  **default (else) branch** .

---

### 🧩 Real-world Analogy

Imagine a chatbot:

* If the user says “hi” → greet them.
* If they ask a question → answer it.
* Otherwise → say you don’t understand.

That’s exactly what `RunnableBranch` does inside a LangChain pipeline.

---

## ⚙️ Syntax

```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (condition_1, runnable_1),
    (condition_2, runnable_2),
    default_runnable
)

```

* Each `condition` is a **callable** (e.g., a lambda or function) returning a boolean.
* The first condition that returns `True` triggers its runnable.
* If none match → the `default_runnable` runs.

---

## 🧩 Basic Example

```python
from langchain_core.runnables import RunnableBranch, RunnableLambda

# Define branches
is_greeting = lambda x: "hello" in x.lower()
is_farewell = lambda x: "bye" in x.lower()

# Define what to do for each branch
greet = RunnableLambda(lambda _: "👋 Hey there! How can I help?")
farewell = RunnableLambda(lambda _: "👋 Goodbye, see you soon!")
default = RunnableLambda(lambda _: "🤖 I didn’t understand that.")

# Build branch
chat_router = RunnableBranch(
    (is_greeting, greet),
    (is_farewell, farewell),
    default
)

print(chat_router.invoke("Hello bot"))
print(chat_router.invoke("bye"))
print(chat_router.invoke("what’s your name?"))

```

🟢 **Output:**

```
👋 Hey there! How can I help?
👋 Goodbye, see you soon!
🤖 I didn’t understand that.

```

✅ The chain **chose a branch dynamically** based on the input.

---

## 🧠 How It Works Internally

1. Input passes through `RunnableBranch`.
2. Each `(condition, runnable)` pair is checked in sequence.
3. When the first condition returns `True`, its corresponding runnable is executed.
4. If none match, `default` is executed.

This enables **conditional pipelines** — like routing messages, handling user intents, or switching models.

---

## 🧩 Example — Routing to Different LLMs

Suppose you want:

* `GPT-4` for reasoning questions.
* `GPT-3.5` for casual chat.
* A default fallback otherwise.

```python
from langchain_core.runnables import RunnableBranch
from langchain_openai import ChatOpenAI

gpt4 = ChatOpenAI(model="gpt-4-turbo")
gpt35 = ChatOpenAI(model="gpt-3.5-turbo")
default = ChatOpenAI(model="gpt-4o-mini")

is_reasoning = lambda x: "why" in x.lower() or "how" in x.lower()
is_casual = lambda x: "hi" in x.lower() or "hello" in x.lower()

llm_router = RunnableBranch(
    (is_reasoning, gpt4),
    (is_casual, gpt35),
    default
)

print(llm_router.invoke("Why is the sky blue?")[:100])

```

🧩 **Output (truncated):**

```
The sky appears blue because molecules in the air scatter blue light more than other colors...

```

✅ Routed intelligently to the  **GPT-4 reasoning branch** .

---

## 🧩 Example — Combine with RunnableSequence

You can chain conditional logic into full pipelines:

```python
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableBranch

# Step 1: Preprocess
clean_text = RunnableLambda(lambda x: x.strip().lower())

# Step 2: Conditional routing
is_math = lambda x: any(ch.isdigit() for ch in x)
math_branch = RunnableLambda(lambda x: f"🧮 You entered a number: {x}")
text_branch = RunnableLambda(lambda x: f"✍️ You entered text: {x}")

branch = RunnableBranch(
    (is_math, math_branch),
    text_branch
)

# Step 3: Compose sequence
pipeline = RunnableSequence(first=clean_text, last=branch)

print(pipeline.invoke(" 12345 "))
print(pipeline.invoke("LangChain Rocks"))

```

🟢 **Output:**

```
🧮 You entered a number: 12345
✍️ You entered text: langchain rocks

```

---

## 🧩 Visualization

```
                ┌──────────────┐
Input ─────────▶│RunnableBranch│
                └──────┬───────┘
                       │
     ┌─────────────────┼────────────────┐
     ▼                 ▼                ▼
 [cond1=True]     [cond2=True]     [default]
Runnable_1        Runnable_2        Runnable_Default

```

---

## 🧱 Key Advantages

| Feature                     | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| 🧩**Dynamic Routing** | Choose which runnable to run at runtime                      |
| 🔁**Composable**      | Works with `RunnableSequence`,`RunnableParallel`, etc.   |
| 🧠**Custom Logic**    | You can write any Python function as a condition             |
| 🧰**Use Cases**       | Chat intent routing, model switching, conditional formatting |

---

## 🧭 Summary Table

| Parameter      | Type           | Description                       |
| -------------- | -------------- | --------------------------------- |
| `conditions` | list of tuples | `(condition_fn, runnable)`pairs |
| `default`    | Runnable       | executed if no condition matches  |
| `invoke()`   | method         | triggers evaluation + execution   |
