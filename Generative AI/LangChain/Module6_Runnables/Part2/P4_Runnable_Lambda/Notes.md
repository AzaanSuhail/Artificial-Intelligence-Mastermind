# 🧠 What is `RunnableLambda`?

`RunnableLambda` is a **wrapper that turns any Python function (lambda or normal function)** into a LangChain **Runnable** — making it compatible with LCEL pipelines like `RunnableSequence`, `RunnableParallel`, etc.

In simple terms:

> It allows you to inject custom Python logic into a LangChain pipeline.

---

## ⚙️ Conceptual Overview

* A **Runnable** in LangChain is any object that implements `.invoke()`, `.batch()`, and `.stream()`.
* `RunnableLambda` lets you quickly **wrap a function** that transforms data without writing a new Runnable class.

You can think of it like this:

```python
RunnableLambda(fn)(input) → fn(input)

```

---

## 🧩 Basic Example

```python
from langchain_core.runnables import RunnableLambda

# Define a simple lambda function
reverse_text = RunnableLambda(lambda x: x[::-1])

# Run it
output = reverse_text.invoke("LangChain")
print(output)

```

🟢 **Output:**

```python
niahCgnaL

```

✅ The input `"LangChain"` was reversed — the lambda function runs inside LangChain’s runnable framework.

---

## 🧱 Why It’s Important

`RunnableLambda` is extremely useful for:

* Adding **custom transformations** (formatting, parsing, pre/post-processing)
* **Debugging** pipelines (print/log data mid-pipeline)
* Performing **conditional routing**
* **Bridging** between LangChain and your own Python logic

---

## 🧩 Example — Custom Transformation in a Sequence

Let’s say you want to process text, summarize it, and then uppercase the result.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableSequence

# Define runnables
prompt = PromptTemplate.from_template("Summarize this text:\\n{text}")
llm = ChatOpenAI(model="gpt-4o-mini")

# Custom lambda to uppercase result
uppercase = RunnableLambda(lambda x: x.upper())

# Build the chain
chain = RunnableSequence(first=prompt | llm, last=uppercase)

output = chain.invoke({"text": "LangChain enables composable AI pipelines."})
print(output)

```

🟩 **Output Example:**

```
LANGCHAIN IS A TOOL FOR BUILDING AI WORKFLOWS.

```

---

## 🧩 Example — Conditional Logic

You can also use Python logic to branch behavior dynamically:

```python
def conditional_logic(x):
    if "error" in x.lower():
        return "⚠️ Error detected!"
    return f"✅ Processed: {x}"

logic_runnable = RunnableLambda(conditional_logic)

print(logic_runnable.invoke("System running fine"))
print(logic_runnable.invoke("Error: API limit reached"))

```

🟢 **Output:**

```
✅ Processed: System running fine
⚠️ Error detected!

```

---

## 🧠 How It Fits in the LCEL Ecosystem

| Runnable                | Purpose                                              |
| ----------------------- | ---------------------------------------------------- |
| `RunnableSequence`    | Connects runnables in a sequential flow              |
| `RunnableParallel`    | Runs multiple runnables simultaneously               |
| `RunnablePassthrough` | Passes data unchanged                                |
| ✅`RunnableLambda`    | Executes a Python function or lambda within the flow |

Thus, `RunnableLambda` is the **bridge** between LangChain’s declarative pipelines and your  **custom Python logic** .

---

## 🧩 Example — In a Complex Pipeline

```python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

split_words = RunnableLambda(lambda x: x["text"].split())
count_words = RunnableLambda(lambda words: len(words))

chain = RunnableParallel({
    "original": RunnablePassthrough(),
    "word_count": split_words | count_words
})

result = chain.invoke({"text": "LangChain makes LLM orchestration easy"})
print(result)

```

🟢 **Output:**

```python
{
  "original": {"text": "LangChain makes LLM orchestration easy"},
  "word_count": 5
}

```

---

# 🧭 Summary Table

| Feature             | Description                      | Example Use                   |
| ------------------- | -------------------------------- | ----------------------------- |
| Type                | Utility Runnable                 | Wraps Python functions        |
| Input/Output        | Any type                         | Dict, str, list, etc.         |
| Usage               | Pre/post-processing              | Cleaning, formatting, routing |
| Chain Compatibility | ✅ Works with all LCEL pipelines | Sequence, Parallel, Map       |

---

# 📚 Authoritative Learning & Reading Resources

Here are **high-quality, official, and expert-level sources** you should follow for deeper understanding:

1. **RunnableLambda API Reference (Official LangChain Docs)**
   🔗 [https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html)
2. **LangChain Expression Language (LCEL) Concepts**
   🔗 [](https://python.langchain.com/docs/concepts/lcel?utm_source=chatgpt.com)[https://python.langchain.com/docs/concepts/lcel](https://python.langchain.com/docs/concepts/lcel)
3. **LangChain How-To: Sequence Composition**
   🔗 [](https://python.langchain.com/docs/how_to/sequence?utm_source=chatgpt.com)[https://python.langchain.com/docs/how_to/sequence](https://python.langchain.com/docs/how_to/sequence)
4. **Advanced Tutorial: Runnables & LCEL Patterns (Medium)**
   🔗 [https://medium.com/@mishra.sagar25/langchain-series-part-8-mastering-runnables-and-lcel-9e1273aeed7a](https://medium.com/@mishra.sagar25/langchain-series-part-8-mastering-runnables-and-lcel-9e1273aeed7a)
5. **Mirascope Blog – Understanding Runnables**
   🔗 [](https://mirascope.com/blog/langchain-runnables?utm_source=chatgpt.com)[https://mirascope.com/blog/langchain-runnables](https://mirascope.com/blog/langchain-runnables)
