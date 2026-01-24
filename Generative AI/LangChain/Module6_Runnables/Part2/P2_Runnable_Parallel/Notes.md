# ⚙️ What is `RunnableParallel`?

In simple terms:

> RunnableParallel lets you run multiple runnables (chains, prompts, functions, LLMs, etc.) in parallel, and collects all their outputs in a dictionary.

It’s like executing multiple “mini-chains” at the same time.

Each sub-runnable runs  **independently** , and when they all finish, you get a  **combined result** .

---

## 🧩 Core Idea

Let’s say you have:

* One LLM generating a **summary**
* Another LLM generating **keywords**
* Another LLM translating the text into **French**

You can run all three in **parallel** rather than one-by-one sequentially.

---

## 🧠 Syntax

```python
from langchain.schema.runnable import RunnableParallel

parallel_chain = RunnableParallel({
    "summary": summarize_chain,
    "keywords": keyword_chain,
    "translation": translate_chain
})

```

Then call it like this:

```python
result = parallel_chain.invoke({"text": "Your input text here"})

```

Result will be:

```python
{
  "summary": "...summary result...",
  "keywords": "...keywords result...",
  "translation": "...translation result..."
}

```

---

# 🧱 RunnableParallel in Action

Let’s explore **practical examples** 👇

---

## ✅ Example 1: Run Multiple Prompts Simultaneously

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")

# Define prompts for different tasks
summary_prompt = PromptTemplate.from_template("Summarize this text: {text}")
keywords_prompt = PromptTemplate.from_template("Extract 5 keywords from this text: {text}")
sentiment_prompt = PromptTemplate.from_template("Classify sentiment of this text (Positive/Negative/Neutral): {text}")

# Define sub-chains
summary_chain = summary_prompt | llm | StrOutputParser()
keywords_chain = keywords_prompt | llm | StrOutputParser()
sentiment_chain = sentiment_prompt | llm | StrOutputParser()

# Combine using RunnableParallel
parallel = RunnableParallel({
    "summary": summary_chain,
    "keywords": keywords_chain,
    "sentiment": sentiment_chain
})

# Run
result = parallel.invoke({"text": "LangChain simplifies building apps powered by LLMs!"})
print(result)

```

---

### 🧩 Output:

```python
{
  "summary": "LangChain helps developers easily create LLM-powered applications.",
  "keywords": "LangChain, LLM, AI, applications, development",
  "sentiment": "Positive"
}

```

All 3 LLM calls happen **concurrently** — faster and more efficient ⚡

---

## ✅ Example 2: Combine LLM + Custom Logic + API Calls

You can mix  **LLMs** ,  **custom functions** , or even  **retrievers** :

```python
from langchain.schema.runnable import RunnableLambda, RunnableParallel

# Custom function (RunnableLambda)
word_count = RunnableLambda(lambda x: len(x["text"].split()))

parallel = RunnableParallel({
    "word_count": word_count,
    "reverse_text": RunnableLambda(lambda x: x["text"][::-1]),
    "upper_text": RunnableLambda(lambda x: x["text"].upper()),
})

result = parallel.invoke({"text": "LangChain is awesome!"})
print(result)

```

Output:

```python
{
  "word_count": 3,
  "reverse_text": "!emosewa si niahCgnaL",
  "upper_text": "LANGCHAIN IS AWESOME!"
}

```

✅ All operations run  **in parallel** , so total execution time ≈ longest single task.

---

## ✅ Example 3: Combine Sequential + Parallel

You can even **nest** `RunnableParallel` inside a `RunnableSequence`.

```python
from langchain.schema.runnable import RunnableSequence

# Sequence: Preprocess → Run parallel tasks → Combine
full_chain = RunnableSequence([
    RunnableLambda(lambda x: {"text": x["text"].strip()}),
    RunnableParallel({
        "summary": summary_chain,
        "keywords": keywords_chain
    })
])

result = full_chain.invoke({"text": "  LangChain provides a powerful framework for LLM apps. "})
print(result)

```

---

# ⚡️ Features & Advantages

| Feature                          | Description                                                        |
| -------------------------------- | ------------------------------------------------------------------ |
| **Parallel Execution**     | Executes multiple chains simultaneously                            |
| **Combined Output**        | Returns a dict mapping key → output                               |
| **Composable**             | Can be combined with `RunnableSequence`,`RunnableLambda`, etc. |
| **Supports Async & Batch** | Works with `.ainvoke()`and `.batch()`                          |
| **Streaming Support**      | Stream results as they’re ready                                   |

---

# 🔧 Common Methods

| Method              | Purpose                             |
| ------------------- | ----------------------------------- |
| `.invoke(input)`  | Run synchronously                   |
| `.ainvoke(input)` | Run asynchronously                  |
| `.batch(inputs)`  | Run multiple inputs concurrently    |
| `.stream(input)`  | Stream outputs as they’re produced |

---

# 💡 RunnableParallel vs RunnableSequence

| Feature                   | RunnableSequence                | RunnableParallel              |
| ------------------------- | ------------------------------- | ----------------------------- |
| **Execution Order** | Sequential (step-by-step)       | Concurrent (all at once)      |
| **Use Case**        | When steps depend on each other | When steps are independent    |
| **Output**          | Single final output             | Dictionary of all sub-outputs |
| **Speed**           | Slower (depends on all steps)   | Faster (runs simultaneously)  |

---

# 📘 Authoritative Learning Resources (Official + Expert)

Here are **high-quality and verified sources** to master `RunnableParallel`:

1. 🔗 **RunnableParallel – API Reference (Official)**
   [https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.parallel.RunnableParallel.html](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.parallel.RunnableParallel.html)
2. 🔗 **LangChain Expression Language (LCEL) — Official Concepts**
   [](https://python.langchain.com/docs/concepts/lcel/?utm_source=chatgpt.com)[https://python.langchain.com/docs/concepts/lcel/](https://python.langchain.com/docs/concepts/lcel/)
3. 🔗 **LangChain How-To: Parallel Chains**
   [](https://python.langchain.com/docs/how_to/parallel/?utm_source=chatgpt.com)[https://python.langchain.com/docs/how_to/parallel/](https://python.langchain.com/docs/how_to/parallel/)
4. 🔗 **Medium Deep Dive: Mastering Runnables & LCEL** (Sagar Mishra, 2024)
   [https://medium.com/@mishra.sagar25/langchain-series-part-8-mastering-runnables-and-lcel-9e1273aeed7a](https://medium.com/@mishra.sagar25/langchain-series-part-8-mastering-runnables-and-lcel-9e1273aeed7a)
5. 🔗 **LangChain Cookbook — RunnableParallel Examples**
   [https://github.com/langchain-ai/langchain-cookbook](https://github.com/langchain-ai/langchain-cookbook)
6. 🔗 **Pinecone Learning Series — LCEL Overview**
   [](https://www.pinecone.io/learn/series/langchain/langchain-expression-language/?utm_source=chatgpt.com)[https://www.pinecone.io/learn/series/langchain/langchain-expression-language/](https://www.pinecone.io/learn/series/langchain/langchain-expression-language/)
