# ⚡ Parallel Chains in LangChain

## 🧩 What Are Parallel Chains?

While **Sequential Chains** execute **one after another** (output of one → input of next),

**Parallel Chains** run **multiple sub-chains simultaneously** and then **combine their outputs** at the end.

> Analogy:
>
> Sequential = Cooking step-by-step 🍳
>
> Parallel = Cooking multiple dishes at once 🍕🍝🍰 and serving them together

They’re ideal when **multiple model calls can work independently** on the same or different inputs.

---

## 🧠 Why Use Parallel Chains?

Parallel chains are useful when you want to:

* Run **independent LLM tasks concurrently**
* Collect **multiple perspectives** or **information types** in one call
* **Speed up** multi-step pipelines by reducing sequential dependency

---

## 🧩 Key Class: `RunnableParallel`

LangChain provides a core utility for this pattern — the **`RunnableParallel`** class (part of LangChain Expression Language, LCEL).

It executes multiple runnables (LLM calls, prompt templates, or even subchains)  **at the same time** , returning a **dictionary** of results.

---

## ⚙️ Example: Run Two Chains in Parallel

Here’s a simple demo 👇

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough

llm = ChatOpenAI(model="gpt-4o-mini")

# Prompt 1: Summarize
summary_prompt = ChatPromptTemplate.from_template("Summarize this text:\\n{text}")
summary_chain = summary_prompt | llm

# Prompt 2: Extract keywords
keyword_prompt = ChatPromptTemplate.from_template("Extract 5 important keywords from this text:\\n{text}")
keyword_chain = keyword_prompt | llm

# Combine them in parallel
parallel_chain = RunnableParallel(
    summary=summary_chain,
    keywords=keyword_chain
)

result = parallel_chain.invoke({"text": "LangChain enables developers to build modular applications powered by large language models."})

print(result)

```

### 🧩 Output

```python
{
  "summary": "LangChain helps developers create modular LLM-powered applications.",
  "keywords": "LangChain, developers, modular, LLM, applications"
}

```

✅ Both sub-chains (`summary_chain` and `keyword_chain`) ran  **simultaneously** ,

and the results were combined into a single dictionary.

---

## 🧰 Advanced Example: Combining Parallel + Sequential Chains

You can **mix Sequential and Parallel** for more complex workflows.

Example:

1️⃣ Step 1 (Parallel): Get summary + keywords

2️⃣ Step 2 (Sequential): Use those results to create a headline

```python
from langchain.schema.runnable import RunnableSequence

# Step 1: Parallel work
parallel_chain = RunnableParallel(
    summary=summary_chain,
    keywords=keyword_chain
)

# Step 2: Create headline using both results
headline_prompt = ChatPromptTemplate.from_template(
    "Using this summary: {summary} and these keywords: {keywords}, "
    "generate a short headline."
)
headline_chain = headline_prompt | llm

# Full pipeline (Sequential)
final_chain = RunnableSequence(
    first=parallel_chain,
    last=headline_chain
)

output = final_chain.invoke({"text": "LangChain enables developers to build modular applications powered by LLMs."})
print(output)

```

🔹 Here, **parallel execution** is used for independent reasoning (summary + keywords),

and **sequential chaining** for dependent reasoning (generate headline).

---

## ⚡ Key Benefits

| Feature                       | Description                                                 |
| ----------------------------- | ----------------------------------------------------------- |
| 🧠**Concurrency**       | Multiple model calls at once                                |
| ⚙️**Efficiency**      | Reduces total latency                                       |
| 🔗**Composable**        | Can be merged with sequential logic                         |
| 🧩**Independent Tasks** | Each sub-chain runs on same or different input              |
| 🧰**Integration**       | Works with any Runnable (LLMChain, prompt, retriever, etc.) |

---

## 🧩 When to Use Which?

| Type                       | Use Case                                                        |
| -------------------------- | --------------------------------------------------------------- |
| **Sequential Chain** | When one step’s output is needed for the next                  |
| **Parallel Chain**   | When multiple steps can run independently and be combined later |

> Tip: In large workflows (like document processing or multi-agent reasoning), combine both to get the best of parallel efficiency and sequential logic.

---

## 📘 Expert-Readable Resources

Here are the **best official and community resources** to master Parallel Chains:

| Type              | Resource                                                                                    | Description                                                    |
| ----------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 📖 Official Docs  | RunnableParallel – LangChain Docs                                                          | Official explanation with syntax and examples                  |
| 📘 LCEL Overview  | LangChain Expression Language (LCEL)                                                        | Explains how Sequential + Parallel logic is unified under LCEL |
| 💡 Cookbook       | [LangChain Cookbook on GitHub](https://github.com/langchain-ai/langchain/tree/master/cookbook) | Contains runnable examples and patterns                        |
| 🧠 Deep Dive Blog | Building Concurrent AI Workflows with LangChain RunnableParallel                            | Explains concurrency and hybrid chains                         |
| 🎥 Video Tutorial | LangChain LCEL Explained — Sequential and Parallel Chains (YouTube)                        | Clear walkthrough with visual pipeline demo                    |

---

## 🧩 Summary

| Concept                    | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| **Parallel Chain**   | Runs multiple subchains simultaneously                          |
| **Key Class**        | `RunnableParallel`                                            |
| **Output**           | Dictionary with outputs from each subchain                      |
| **Best Use Case**    | Independent subtasks (e.g., summarize, sentiment, extract data) |
| **Can Combine With** | `RunnableSequence`or `SequentialChain`for hybrid workflows  |
