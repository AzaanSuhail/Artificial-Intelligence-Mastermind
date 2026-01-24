# 🧩 What Is `RunnableSequence`?

A **`RunnableSequence`** is a **chain of multiple runnables** connected **sequentially** — where

➡️ **the output of one step** becomes **the input to the next step.**

Think of it as a **pipeline** where data flows step-by-step.

It’s the **backbone** of how LCEL executes complex logic like:

**Prompt → LLM → Parser → Postprocessor**

---

## ⚙️ Internal Concept

Here’s how LangChain defines it conceptually:

```python
RunnableSequence([step1, step2, step3, ...])

```

or equivalently:

```python
step1 | step2 | step3

```

➡️ Each step must be a **Runnable** (e.g., a PromptTemplate, LLM, OutputParser, RunnableLambda, etc.).

---

## 🧠 Basic Example: Prompt → LLM → Parser

Let’s create a simple example using `RunnableSequence`:

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

# Step 1: Create components
prompt = PromptTemplate.from_template("Explain the concept of {topic} in one sentence.")
llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Step 2: Create a RunnableSequence
chain = RunnableSequence(steps=[prompt, llm, parser])

# Step 3: Run it
result = chain.invoke({"topic": "Neural Networks"})
print(result)

```

### 🧩 Output Flow:

1. Input: `{"topic": "Neural Networks"}`
2. `PromptTemplate` → formats → `"Explain the concept of Neural Networks in one sentence."`
3. `ChatOpenAI` → generates LLM response
4. `StrOutputParser` → converts it to a clean string output
5. Output: `"Neural networks are systems modeled after the human brain to recognize patterns."`

---

## ⚡️ Shorthand Syntax (Pipe Operator)

You can achieve the same result using the  **pipe (`|`) operator** :

```python
chain = prompt | llm | parser
result = chain.invoke({"topic": "Deep Learning"})

```

It’s cleaner and more readable — this is **LangChain Expression Language (LCEL)** syntax.

---

## 🔁 Multiple-Step Sequence Example

Let’s say you want:

* First step: **summarize text**
* Second step: **translate summary**
* Third step: **polish tone**

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

# Define prompts for each step
summarize = PromptTemplate.from_template("Summarize the following text:\\n{text}")
translate = PromptTemplate.from_template("Translate this into French:\\n{summary}")
polish = PromptTemplate.from_template("Polish this French text:\\n{french}")

# Create the runnable sequence
chain = (
    summarize
    | llm
    | StrOutputParser()
    | (lambda x: {"summary": x})
    | translate
    | llm
    | StrOutputParser()
    | (lambda x: {"french": x})
    | polish
    | llm
    | StrOutputParser()
)

result = chain.invoke({"text": "LangChain helps developers build LLM applications faster."})
print(result)

```

🧠 **Explanation:**

* The output from one prompt/LLM is piped into the next step.
* Each step transforms or refines the output.
* You can mix `PromptTemplate`, `LLM`, and even simple **lambda functions** (as runnables).

---

## 🧩 Advanced Example – Custom Runnables in a Sequence

You can add **custom logic** using `RunnableLambda`:

```python
from langchain.schema.runnable import RunnableLambda

reverse_text = RunnableLambda(lambda x: x[::-1])
uppercase_text = RunnableLambda(lambda x: x.upper())

chain = reverse_text | uppercase_text
result = chain.invoke("langchain")
print(result)  # Output: "NIAHCGNAL"

```

---

## 🧠 When to Use `RunnableSequence`

Use it when:

* You have multiple steps that depend on each other.
* You want to ensure **clean data flow** between prompt, LLM, and output parser.
* You need a pipeline that can  **invoke** ,  **batch** , or **stream** data.

---

## ⚡️ Key Features

| Feature       | Description                              |
| ------------- | ---------------------------------------- |
| `invoke()`  | Run once synchronously                   |
| `ainvoke()` | Run once asynchronously                  |
| `batch()`   | Run multiple inputs in parallel          |
| `stream()`  | Stream intermediate outputs in real time |

Example:

```python
for chunk in chain.stream({"topic": "AI"}):
    print(chunk)

```
