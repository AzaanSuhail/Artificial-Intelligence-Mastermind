# 🧱 Pydantic Structured Output — The Complete Guide

---

## 🚀 1️⃣ What Is Pydantic?

[Pydantic]() is a **Python library for data validation and settings management** using Python type hints.

It ensures that your data (e.g., model outputs, API responses) **strictly follows a defined structure (schema)** — automatically validating types, formats, and defaults.

---

## 🧠 2️⃣ Why Use Pydantic for Structured Outputs?

When working with  **LLMs (like GPT-4/5)** , the model outputs text — often in JSON format — but it may contain:

* missing keys 🕳️
* incorrect data types ❌
* inconsistent field names 😩

Pydantic **fixes all of that** by:

* defining a **strict schema** for the output
* **validating** model responses automatically
* returning clean, structured **Python objects**

Perfect for GenAI apps, where you want  **reliable, machine-readable responses** .

---

## 🧩 3️⃣ Pydantic Model Example

<pre class="overflow-visible!" data-start="1311" data-end="1666"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> pydantic </span><span>import</span><span> BaseModel
</span><span>from</span><span> typing </span><span>import</span><span></span><span>List</span><span>, </span><span>Optional</span><span>, </span><span>Literal</span><span>

</span><span># Define structured schema</span><span>
</span><span>class</span><span></span><span>Review</span><span>(</span><span>BaseModel</span><span>):
    key_themes: </span><span>List</span><span>[</span><span>str</span><span>]
    summary: </span><span>str</span><span>
    sentiment: </span><span>Literal</span><span>[</span><span>"positive"</span><span>, </span><span>"negative"</span><span>, </span><span>"neutral"</span><span>]
    pros: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]] = </span><span>None</span><span>
    cons: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]] = </span><span>None</span><span>
    reviewer_name: </span><span>Optional</span><span>[</span><span>str</span><span>] = </span><span>None</span><span>
</span></span></code></div></div></pre>

This schema:

* Forces the model to return keys like `key_themes`, `summary`, etc.
* Ensures `sentiment` can only be one of `"positive"`, `"negative"`, or `"neutral"`.
* Makes `pros`, `cons`, and `reviewer_name` optional.

---

## ⚙️ 4️⃣ Using Pydantic with OpenAI Structured Outputs

### ✅ Basic Example

<pre class="overflow-visible!" data-start="1977" data-end="2825"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> openai </span><span>import</span><span> OpenAI
</span><span>from</span><span> pydantic </span><span>import</span><span> BaseModel
</span><span>from</span><span> typing </span><span>import</span><span></span><span>List</span><span>, </span><span>Optional</span><span>, </span><span>Literal</span><span>
</span><span>import</span><span> json

client = OpenAI()

</span><span>class</span><span></span><span>Review</span><span>(</span><span>BaseModel</span><span>):
    key_themes: </span><span>List</span><span>[</span><span>str</span><span>]
    summary: </span><span>str</span><span>
    sentiment: </span><span>Literal</span><span>[</span><span>"positive"</span><span>, </span><span>"negative"</span><span>, </span><span>"neutral"</span><span>]
    pros: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]] = </span><span>None</span><span>
    cons: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]] = </span><span>None</span><span>
    reviewer_name: </span><span>Optional</span><span>[</span><span>str</span><span>] = </span><span>None</span><span>

prompt = </span><span>"Extract structured review information from: 'The product was amazing but delivery was late.'"</span><span>

response = client.chat.completions.create(
    model=</span><span>"gpt-4o-mini"</span><span>,
    messages=[{</span><span>"role"</span><span>: </span><span>"user"</span><span>, </span><span>"content"</span><span>: prompt}],
    response_format={</span><span>"type"</span><span>: </span><span>"json_object"</span><span>}  </span><span># enforce structured JSON</span><span>
)

</span><span># Validate output using Pydantic</span><span>
parsed_output = Review.model_validate_json(response.choices[</span><span>0</span><span>].message.content)

</span><span>print</span><span>(parsed_output)
</span><span>print</span><span>(parsed_output.</span><span>dict</span><span>())
</span></span></code></div></div></pre>

✅ **Output Example:**

<pre class="overflow-visible!" data-start="2849" data-end="3071"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Review(
  key_themes=[</span><span>'product quality'</span><span>, </span><span>'delivery'</span><span>],
  summary=</span><span>'Great product but delivery was delayed.'</span><span>,
  sentiment=</span><span>'positive'</span><span>,
  pros=[</span><span>'product quality'</span><span>],
  cons=[</span><span>'delivery delay'</span><span>],
  reviewer_name=</span><span>None</span><span>
)
</span></span></code></div></div></pre>

Here:

* `Review` acts as a  **validator and parser** .
* If a field is missing or wrongly typed → Pydantic throws a  **ValidationError** .

---

## 🧩 5️⃣ Using Pydantic with Instructor (Automatic Validation)

[`Instructor`](https://github.com/jxnl/instructor) automatically integrates Pydantic models with OpenAI structured outputs — making it super clean 👇

<pre class="overflow-visible!" data-start="3432" data-end="4060"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> instructor </span><span>import</span><span> from_openai
</span><span>from</span><span> openai </span><span>import</span><span> OpenAI
</span><span>from</span><span> pydantic </span><span>import</span><span> BaseModel
</span><span>from</span><span> typing </span><span>import</span><span></span><span>List</span><span>, </span><span>Optional</span><span>, </span><span>Literal</span><span>

client = from_openai(OpenAI())

</span><span>class</span><span></span><span>Review</span><span>(</span><span>BaseModel</span><span>):
    key_themes: </span><span>List</span><span>[</span><span>str</span><span>]
    summary: </span><span>str</span><span>
    sentiment: </span><span>Literal</span><span>[</span><span>"positive"</span><span>, </span><span>"negative"</span><span>, </span><span>"neutral"</span><span>]
    pros: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]]
    cons: </span><span>Optional</span><span>[</span><span>List</span><span>[</span><span>str</span><span>]]
    reviewer_name: </span><span>Optional</span><span>[</span><span>str</span><span>]

result = client.chat.completions.create(
    model=</span><span>"gpt-4o-mini"</span><span>,
    messages=[{</span><span>"role"</span><span>: </span><span>"user"</span><span>, </span><span>"content"</span><span>: </span><span>"The laptop is fast but battery life is poor."</span><span>}],
    response_model=Review  </span><span># <-- Magic happens here</span><span>
)

</span><span>print</span><span>(result)
</span></span></code></div></div></pre>

✅ Output:

<pre class="overflow-visible!" data-start="4072" data-end="4283"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Review(
  key_themes=[</span><span>'performance'</span><span>, </span><span>'battery'</span><span>],
  summary=</span><span>'Fast laptop but poor battery life.'</span><span>,
  sentiment=</span><span>'positive'</span><span>,
  pros=[</span><span>'fast performance'</span><span>],
  cons=[</span><span>'battery life'</span><span>],
  reviewer_name=</span><span>None</span><span>
)
</span></span></code></div></div></pre>

`Instructor` uses your **Pydantic model’s schema** to tell the model *exactly* how to format its output — and automatically parses + validates it.

---

## 🧩 6️⃣ Pydantic vs TypedDict (Quick Comparison)

| Feature         | `TypedDict`                         | `Pydantic`                                   |
| --------------- | ------------------------------------- | ---------------------------------------------- |
| Type checking   | Static (checked by IDE/type checkers) | Dynamic (runtime validation)                   |
| Default values  | ❌ No                                 | ✅ Yes                                         |
| Validation      | ❌ No                                 | ✅ Yes                                         |
| Nested models   | Limited                               | ✅ Fully supported                             |
| Error reporting | ❌ Minimal                            | ✅ Detailed & structured                       |
| Integration     | Used with basic OpenAI SDK            | Perfect with Instructor, LangChain, OpenAI SDK |

🔹 Use **TypedDict** for lightweight schemas.

🔹 Use **Pydantic** for **production-grade validation** and  **nested models** .

---

## 🧠 7️⃣ Real-World Use Cases

✅ **Entity extraction** (name, company, sentiment, etc.)

✅ **Resume parsing**

✅ **Financial report extraction**

✅ **Customer review analysis**

✅ **Automated data labeling pipelines**

In all these, you use Pydantic models to ensure the AI output fits the required structure before saving or using it.

---

## 📚 8️⃣ Recommended Resources

### 🔹 Official Docs

1. **Pydantic Documentation (Latest v2)**

   🔗 [https://docs.pydantic.dev/latest/]([https://docs.pydantic.dev/latest/]())
2. **OpenAI Structured Outputs Guide**

   🔗 [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)
3. **Instructor Library (Pydantic + OpenAI)**

   🔗 [https://github.com/jxnl/instructor](https://github.com/jxnl/instructor)
4. **DeepLearning.AI Course: Structuring LLM Outputs** (Free by Andrew Ng + OpenAI)

   🔗 [https://learn.deeplearning.ai/courses/structured-outputs]()
5. **LangChain Output Parsers** (Pydantic integration)

   🔗 [https://python.langchain.com/docs/modules/model_io/output_parsers]()

---

## 🧩 9️⃣ Summary Table

| Concept                     | Description                                   | Example                                     |
| --------------------------- | --------------------------------------------- | ------------------------------------------- |
| **Pydantic**          | Data validation library using type hints      | `class Review(BaseModel)`                 |
| **Structured Output** | Forcing LLMs to return consistent JSON        | `response_format={"type": "json_object"}` |
| **Validation**        | Ensures data is clean + typed                 | `Review.model_validate_json()`            |
| **Instructor**        | Wrapper to auto-parse LLM output via Pydantic | `response_model=Review`                   |
