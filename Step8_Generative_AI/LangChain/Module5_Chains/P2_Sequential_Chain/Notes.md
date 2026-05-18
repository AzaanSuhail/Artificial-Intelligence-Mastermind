## 🧩 What is a Sequential Chain?

In  **LangChain** , a **Sequential Chain** is a type of **Chain** that executes multiple sub-chains  **in sequence** , where the  **output of one step becomes the input to the next** .

Think of it like a **pipeline** of tasks — each model call or computation transforms the data a bit more before passing it forward.

> Analogy: Imagine making coffee ☕
>
> Step 1: Grind beans → Step 2: Boil water → Step 3: Brew → Step 4: Pour into cup
>
> Each step depends on the previous step’s output. That’s what a **Sequential Chain** does for LLM workflows.

---

## 🧠 Why Use Sequential Chains?

When your application logic needs  **multiple dependent reasoning steps** , you can:

* Break it down into modular subchains
* Reuse or debug each chain independently
* Maintain structured data flow (inputs → outputs)
* Combine LLMs, prompt templates, tools, or even custom functions together

---

## 🧩 Types of Sequential Chains

LangChain gives you **two main variants** of sequential chaining:

### 1. **SimpleSequentialChain**

* The simplest form.
* Each chain passes its output as the next chain’s input  **as a single string** .
* Ideal for **text transformations** (e.g., summarize → rephrase → expand).

```python
from langchain.chains import SimpleSequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Step 1: Summarize a text
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\\n{text}"
)
summary_chain = LLMChain(llm=OpenAI(), prompt=summary_prompt)

# Step 2: Create a title from summary
title_prompt = PromptTemplate(
    input_variables=["summary"],
    template="Create a catchy title for the following summary:\\n{summary}"
)
title_chain = LLMChain(llm=OpenAI(), prompt=title_prompt)

# Combine into a sequential chain
overall_chain = SimpleSequentialChain(chains=[summary_chain, title_chain])
result = overall_chain.run("LangChain is a framework for building LLM applications.")
print(result)

```

🔹 The output from the first LLM (`summary_chain`) becomes the input to the second (`title_chain`).

---

### 2. **SequentialChain**

* More **flexible and powerful** than `SimpleSequentialChain`.
* You can handle **multiple inputs and outputs** per step.
* Each sub-chain can receive **specific variable mappings** (not just a single string).

```python
from langchain.chains import SequentialChain, LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Step 1: Extract keywords
keyword_prompt = PromptTemplate(
    input_variables=["text"],
    template="Extract 3 key topics from this text:\\n{text}"
)
keyword_chain = LLMChain(llm=OpenAI(), prompt=keyword_prompt, output_key="keywords")

# Step 2: Generate summary based on those keywords
summary_prompt = PromptTemplate(
    input_variables=["text", "keywords"],
    template="Summarize the text focusing on these keywords: {keywords}\\n{text}"
)
summary_chain = LLMChain(llm=OpenAI(), prompt=summary_prompt, output_key="summary")

# Combine them
chain = SequentialChain(
    chains=[keyword_chain, summary_chain],
    input_variables=["text"],
    output_variables=["summary"],
    verbose=True
)

result = chain({"text": "LangChain helps build modular applications around LLMs with ease."})
print(result["summary"])

```

🔹 Here, multiple variables (`text`, `keywords`) flow between chains.

🔹 Each sub-chain can have its own input/output schema.

---

## ⚙️ How Sequential Chains Work Internally

Internally, a `SequentialChain`:

1. Defines a **variable dependency graph** (which variable is needed by which chain).
2. Executes each chain  **in order** .
3. **Merges all intermediate outputs** into a running context dictionary.
4. Returns only the specified `output_variables` at the end.

---

## 🚀 Use Cases

✅ Multi-step reasoning (extract → summarize → rewrite)

✅ Multi-prompt pipelines (question classification → retrieval → answer generation)

✅ Preprocessing or postprocessing LLM outputs

✅ Data enrichment workflows (like “fetch metadata → generate summary → make recommendations”)

---

## 📘 Learn More — Expert-Readable Resources

Here are the best official and community sources to  **master Sequential Chains** :

| Type              | Resource                                                          | Why It’s Good                                                       |
| ----------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| 📖 Official Docs  | 🔗 LangChain SequentialChain Documentation                        | Clear official guide with examples                                   |
| 💡 Tutorials      | 🔗 LangChain Cookbook (by LangChainAI GitHub)                     | Contains practical examples using Sequential & SimpleSequentialChain |
| 🧱 Medium Guide   | 🔗 Understanding LangChain Chains – A Complete Guide             | Explains with visuals + real projects                                |
| 🎥 YouTube        | 🔗 LangChain Chains Explained (by Patrick Loeber / CodeWithPanda) | Visual walkthrough of SequentialChain logic                          |
| 🧠 Deep Dive Blog | 🔗 LangChain Explained: Building Multi-Step AI Pipelines          | Conceptual + project-level examples                                  |
