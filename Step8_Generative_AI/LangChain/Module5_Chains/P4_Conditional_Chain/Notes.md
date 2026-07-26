## **Conditional (Branching) Chains in LangChain / GenAI Workflows**

---

### 🧠 1. Intuitive Understanding

A *conditional chain* (also sometimes called a  *branching chain* ) allows your pipeline to **make decisions** — i.e., “If X then do Chain A, else do Chain B”.

This is more advanced than a straight sequential chain. For example:

* If the user sentiment is positive → respond with “Thanks for the feedback!” chain
* If the sentiment is negative → respond with “How can we improve?” chain
  Thus, you add logic / branching into your GenAI workflow.

---

### ⚙️ 2. Definition

> A Conditional Chain is a workflow component that evaluates a condition (based on input or intermediate output) and routes execution to one of multiple sub-chains depending on which condition is satisfied.

Key features:

* **Input** arrives → some decision logic (function or LLM) runs
* Based on result → one of several sub-chains is executed
* Output comes from whichever branch was chosen
* You can also have a *default branch* if none of the conditions match

---

### 🪄 3. Visual Intuition

```
             [Input]
                ↓
         [Decision Logic]
          /            \\
   Condition A true   Condition A false
       ↓                     ↓
  [Chain A]             [Chain B / Default]
       ↓                     ↓
    [Output]             [Output]

```

You can think of it like a “fork” in your pipeline where the road splits based on a check.

---

### 💻 4. Example: Conditional Chain in Python

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import RunnableBranch
from langchain.chat_models import ChatOpenAI

# 1) Setup LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2) Define chains
template_positive = PromptTemplate(
    input_variables=["review"],
    template="Respond to this positive review in a friendly way:\\n\\n{review}"
)
positive_chain = LLMChain(llm=llm, prompt=template_positive)

template_negative = PromptTemplate(
    input_variables=["review"],
    template="Respond to this negative review with empathy and ask how we can improve:\\n\\n{review}"
)
negative_chain = LLMChain(llm=llm, prompt=template_negative)

# 3) Decision function
def is_positive(input_dict: dict) -> bool:
    # simple heuristic: check for “good” word (for demo)
    return "good" in input_dict["review"].lower()

# 4) Build conditional branch
conditional = RunnableBranch(
    (is_positive, positive_chain),   # if condition true → positive_chain
    negative_chain                   # else → negative_chain (default)
)

# 5) Run
result = conditional.invoke({"review": "The product is good and I loved it!"})
print(result)  # Will run positive_chain

result2 = conditional.invoke({"review": "I’m disappointed with the product quality."})
print(result2)  # Will run negative_chain

```

In this example:

* If the review text contains “good” → route to `positive_chain`
* Otherwise → route to `negative_chain`

---

### 🔍 5. Use-Cases

| Use-Case                 | Why Conditional Chain?                                                         |
| ------------------------ | ------------------------------------------------------------------------------ |
| Sentiment-based response | Different replies for positive vs negative feedback                            |
| Topic routing            | Route queries about “billing”, “tech”, “general” to separate chains      |
| Input length check       | If text is very long → summarise; else → detailed answer                     |
| Data quality check       | If input missing fields → ask user for more info; else → proceed normal flow |

---

### 🧩 6. Implementation Details & Tips

* Your **decision logic** can be a simple Python function (`lambda`), or even another LLM chain that classifies.
* There should be a **default branch** to handle “none of the conditions matched” scenarios.
* Branches should ideally return the same schema of output (or you should normalize afterwards).
* Always test with inputs that go down each branch.
* Think about  **fallbacks** : what happens if decision logic fails?

---

### 🚀 7. Real-World Analogy

Imagine you’re at a restaurant kiosk:

* You press “Vegetarian” → kiosk shows vegetarian menu (Chain A)
* You press “Non-Vegetarian” → shows non-veg menu (Chain B)
* If you press nothing / unclear → shows “Please select option” screen (Default chain)
  That is the idea of a **conditional chain** in a GenAI workflow.

---


### ✅ 8. Summary

* **Conditional Chain** = branching logic in your chain workflow
* It allows you to dynamically choose which sub-chain to run based on input or intermediate result
* Great for real-world apps where one path doesn’t always fit all inputs
* Key parts: decision function, branches (chain A, chain B, …), default fallback
