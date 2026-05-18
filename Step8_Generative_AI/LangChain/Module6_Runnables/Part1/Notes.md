# 🧠 What Are Runnables in LangChain?

In LangChain, **Runnables** are the **core building blocks** used to execute **any operation in a pipeline** — whether that’s calling an LLM, transforming input, parsing output, or chaining multiple steps together.

They form the **foundation of LangChain Expression Language (LCEL)** — a simple, composable way to build and connect LLM applications.

---

## ⚙️ Intuition

Think of a `Runnable` as a  **function with superpowers** .

🧩 It can:

* Take an **input** (e.g., user prompt)
* Do **some work** (call an LLM, retrieve data, or transform text)
* Return an **output**
* Be **connected** to other runnables to form a chain
* Be executed  **synchronously** ,  **asynchronously** , or **streamed**

---

## 🏗️ Core Interface

All Runnables share a common interface:

```python
runnable.invoke(input)       # Run once synchronously
await runnable.ainvoke(input)  # Run once asynchronously
runnable.batch(inputs)       # Run on a list of inputs
runnable.stream(input)       # Stream partial outputs

```

This means no matter what kind of runnable it is (LLM, prompt, parser, chain), you can call it in the same way.

---

## 🧩 Common Runnables in LangChain

| Runnable Type                 | Description                                  | Example                                 |
| ----------------------------- | -------------------------------------------- | --------------------------------------- |
| **RunnableLambda**      | Custom Python function wrapped as a runnable | Transform or preprocess text            |
| **RunnableSequence**    | Chain multiple runnables sequentially        | Prompt → LLM → OutputParser           |
| **RunnableParallel**    | Run multiple runnables at the same time      | Query multiple LLMs or tools            |
| **RunnableMap**         | Map a runnable over dictionary fields        | Run different steps on different keys   |
| **RunnablePassthrough** | Pass input directly to next step             | Used when chaining without modification |

---

## 🧠 Example: Basic Runnable Chain

Let’s create a simple chain:

**User prompt → Format into template → Call LLM → Parse output**

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

# Step 1: Create components
prompt = PromptTemplate.from_template("Explain the concept of {topic} in simple terms.")
llm = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Step 2: Combine them into a chain (RunnableSequence)
chain = RunnableSequence(steps=[prompt, llm, parser])

# Step 3: Run it
result = chain.invoke({"topic": "quantum computing"})
print(result)

```

🧩 Behind the scenes:

1. Input `{"topic": "quantum computing"}` → passed into `PromptTemplate`
2. Prompt text → passed into `ChatOpenAI`
3. LLM response → passed into `StrOutputParser`
4. Parsed string → final output ✅

---

## ⚡️ Runnables Are Composable

You can combine runnables easily using the  **pipe (`|`) operator** :

```python
chain = prompt | llm | parser

```

This is **syntactic sugar** for a `RunnableSequence`.

---

## 🧩 Example: RunnableLambda (Custom Logic)

```python
from langchain.schema.runnable import RunnableLambda

# A custom Python function wrapped as a Runnable
reverse_text = RunnableLambda(lambda x: x[::-1])

result = reverse_text.invoke("LangChain")
print(result)  # "niahCgnaL"

```

You can mix this with LLMs or prompts in a pipeline:

```python
chain = reverse_text | llm | parser

```

---

## ⚙️ RunnableParallel (Run in Parallel)

Example:

```python
from langchain.schema.runnable import RunnableParallel

parallel = RunnableParallel({
    "explanation": llm,
    "summary": llm
})

result = parallel.invoke("What is LangChain?")
print(result)

```

This runs both sub-runnables **simultaneously** and returns a dictionary:

```python
{
  "explanation": "...full explanation...",
  "summary": "...short summary..."
}

```

---

## 🔥 Why Runnables Are Powerful

✅ **Unified interface** — Everything (LLMs, tools, retrievers, custom logic) uses the same `.invoke()` method.

✅ **Composability** — You can build reusable modular pipelines.

✅ **Streaming support** — Stream tokens as they’re generated.

✅ **Async support** — Ideal for web apps or chatbots.

✅ **Scalable** — You can parallelize or batch inputs easily.

---

## 📘 Official and Readable Resources

* [Runnable Interface – LangChain Documentation](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html?utm_source=chatgpt.com) — the API reference for the base Runnable class. [LangChain](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html?utm_source=chatgpt.com)
* [LangChain Expression Language (LCEL) – Official Guide](https://python.langchain.com/docs/concepts/lcel/?utm_source=chatgpt.com) — overview of LCEL, composition with Runnables. [LangChain](https://python.langchain.com/docs/concepts/lcel/?utm_source=chatgpt.com)
* [Runnable Interface – Concepts Guide](https://python.langchain.com/docs/concepts/runnables/?utm_source=chatgpt.com) — conceptual explanation of Runnables, batching, streaming, etc. [LangChain](https://python.langchain.com/docs/concepts/runnables/?utm_source=chatgpt.com)
* [LCEL Cheatsheet – How-To Guide](https://python.langchain.com/docs/how_to/lcel_cheatsheet/?utm_source=chatgpt.com) — quick reference for pipe (`|`), `RunnableSequence`, `RunnableParallel`. [LangChain](https://python.langchain.com/docs/how_to/lcel_cheatsheet/?utm_source=chatgpt.com)
* [“LangChain Expression Language Explained” – Pinecone Tutorial](https://www.pinecone.io/learn/series/langchain/langchain-expression-language/?utm_source=chatgpt.com) — community explainer with examples. [pinecone.io](https://www.pinecone.io/learn/series/langchain/langchain-expression-language/?utm_source=chatgpt.com)
* [“Understanding LangChain Runnables” – Mirascope Blog](https://mirascope.com/blog/langchain-runnables?utm_source=chatgpt.com) — another independent take on Runnables.
