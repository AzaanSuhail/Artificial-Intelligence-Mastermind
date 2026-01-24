# 🧱 Understanding Structured Outputs with Pydantic + LangChain

---

## 🚀 1️⃣ What This Code Does — In Simple Words

You are asking a **language model** (GPT via LangChain’s `ChatOpenAI`) to:

> Read a review and return structured information — key themes, summary, sentiment, pros, cons, and reviewer name.

The model’s output isn’t just free text.

Instead, it’s **validated JSON** that strictly follows your  **Pydantic schema (`Review`)** .

This means the output:

* Always contains the required keys ✅
* Has the correct types (e.g., list, string, literal) ✅
* Is safe to parse and use directly ✅

---

## 🧩 2️⃣ Step-by-Step Code Breakdown

### 🔹 Step 1: Imports and Setup

<pre class="overflow-visible!" data-start="990" data-end="1207"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> langchain_openai </span><span>import</span><span> ChatOpenAI
</span><span>from</span><span> dotenv </span><span>import</span><span> load_dotenv
</span><span>from</span><span> typing </span><span>import</span><span> TypedDict, Annotated, </span><span>Optional</span><span>, </span><span>Literal</span><span>
</span><span>from</span><span> pydantic </span><span>import</span><span> BaseModel, Field

load_dotenv()
model = ChatOpenAI()
</span></span></code></div></div></pre>

* `ChatOpenAI()` → initializes the OpenAI chat model inside LangChain.
* `load_dotenv()` → loads your API key from `.env` file.
* We’ll use `Pydantic` to define the structure we want from the model.

---

### 🔹 Step 2: Defining the Schema (Pydantic Model)

<pre class="overflow-visible!" data-start="1471" data-end="2122"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>class</span><span></span><span>Review</span><span>(</span><span>BaseModel</span><span>):
    key_themes: </span><span>list</span><span>[</span><span>str</span><span>] = Field(description=</span><span>"Write down all the key themes discussed in the review in a list"</span><span>)
    summary: </span><span>str</span><span> = Field(description=</span><span>"A brief summary of the review"</span><span>)
    sentiment: </span><span>Literal</span><span>[</span><span>"pos"</span><span>, </span><span>"neg"</span><span>] = Field(description=</span><span>"Return sentiment of the review either negative, positive or neutral"</span><span>)
    pros: </span><span>Optional</span><span>[</span><span>list</span><span>[</span><span>str</span><span>]] = Field(default=</span><span>None</span><span>, description=</span><span>"Write down all the pros inside a list"</span><span>)
    cons: </span><span>Optional</span><span>[</span><span>list</span><span>[</span><span>str</span><span>]] = Field(default=</span><span>None</span><span>, description=</span><span>"Write down all the cons inside a list"</span><span>)
    name: </span><span>Optional</span><span>[</span><span>str</span><span>] = Field(default=</span><span>None</span><span>, description=</span><span>"Write the name of the reviewer"</span><span>)
</span></span></code></div></div></pre>

This is your  **output schema** .

Let’s decode what each field does 👇

| Field          | Type                      | Description                                                                     | Required?     |
| -------------- | ------------------------- | ------------------------------------------------------------------------------- | ------------- |
| `key_themes` | `list[str]`             | Extracts all the main topics discussed                                          | ✅            |
| `summary`    | `str`                   | Short, readable summary                                                         | ✅            |
| `sentiment`  | `Literal["pos", "neg"]` | Only allows `"pos"`or `"neg"`— ensures model doesn’t output random values | ✅            |
| `pros`       | `Optional[list[str]]`   | List of pros, can be `None`                                                   | ⚙️ Optional |
| `cons`       | `Optional[list[str]]`   | List of cons, can be `None`                                                   | ⚙️ Optional |
| `name`       | `Optional[str]`         | Reviewer name, can be `None`                                                  | ⚙️ Optional |

✅ `Field(description="...")` provides **natural-language hints** to guide the LLM on what to fill in.

These descriptions are automatically included in the prompt the model receives.

---

### 🔹 Step 3: Attach Schema to Model

<pre class="overflow-visible!" data-start="2998" data-end="3067"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>structured_model = model.with_structured_output(Review)
</span></span></code></div></div></pre>

This is the **LangChain magic** 🪄

`with_structured_output(Review)` tells LangChain:

> “When I call this model, make sure the response follows the `Review` schema.”

LangChain will:

* Send the schema’s description to the LLM (using JSON schema under the hood)
* Parse the model’s raw response back into a **validated `Review` Pydantic object**

---

### 🔹 Step 4: Invoke the Model

<pre class="overflow-visible!" data-start="3453" data-end="3562"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra...
""")
</span></span></code></div></div></pre>

Here, you send a **long review** as the input.

The model analyzes it and generates a  **structured JSON response** , like:

<pre class="overflow-visible!" data-start="3687" data-end="4199"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"key_themes"</span><span>:</span><span></span><span>[</span><span>"Performance"</span><span>,</span><span></span><span>"Camera"</span><span>,</span><span></span><span>"Battery"</span><span>,</span><span></span><span>"Build Quality"</span><span>,</span><span></span><span>"Price"</span><span>]</span><span>,</span><span>
  </span><span>"summary"</span><span>:</span><span></span><span>"The Samsung Galaxy S24 Ultra delivers exceptional performance and camera quality but feels heavy and expensive."</span><span>,</span><span>
  </span><span>"sentiment"</span><span>:</span><span></span><span>"pos"</span><span>,</span><span>
  </span><span>"pros"</span><span>:</span><span></span><span>[</span><span>
    </span><span>"Powerful Snapdragon 8 Gen 3 processor"</span><span>,</span><span>
    </span><span>"Excellent 200MP camera"</span><span>,</span><span>
    </span><span>"Long battery life"</span><span>,</span><span>
    </span><span>"S-Pen functionality"</span><span>
  </span><span>]</span><span>,</span><span>
  </span><span>"cons"</span><span>:</span><span></span><span>[</span><span>
    </span><span>"Bulky and heavy design"</span><span>,</span><span>
    </span><span>"Pre-installed bloatware"</span><span>,</span><span>
    </span><span>"High price tag"</span><span>
  </span><span>]</span><span>,</span><span>
  </span><span>"name"</span><span>:</span><span></span><span>"Nitish Singh"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

This JSON is then automatically converted into a Python object of type `Review`.

---

### 🔹 Step 5: View Result

<pre class="overflow-visible!" data-start="4316" data-end="4343"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>print</span><span>(result)
</span></span></code></div></div></pre>

You’ll get something like:

<pre class="overflow-visible!" data-start="4373" data-end="4746"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>Review(
  key_themes=[</span><span>'performance'</span><span>, </span><span>'camera'</span><span>, </span><span>'battery'</span><span>, </span><span>'price'</span><span>, </span><span>'build quality'</span><span>],
  summary=</span><span>'The Samsung Galaxy S24 Ultra offers top-tier performance and camera but is heavy and expensive.'</span><span>,
  sentiment=</span><span>'pos'</span><span>,
  pros=[</span><span>'Powerful processor'</span><span>, </span><span>'Stunning camera'</span><span>, </span><span>'Long battery life'</span><span>],
  cons=[</span><span>'Heavy design'</span><span>, </span><span>'Bloatware'</span><span>, </span><span>'High price'</span><span>],
  name=</span><span>'Nitish Singh'</span><span>
)
</span></span></code></div></div></pre>

It’s now a  **fully validated, structured Python object** , not just text.

---

## 🧠 3️⃣ What Happens Internally

Here’s what LangChain does internally when you use `with_structured_output()`:

1. It converts your Pydantic model (`Review`) into a  **JSON schema** :
   <pre class="overflow-visible!" data-start="5015" data-end="5254"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
     </span><span>"type"</span><span>:</span><span></span><span>"object"</span><span>,</span><span>
     </span><span>"properties"</span><span>:</span><span></span><span>{</span><span>
       </span><span>"key_themes"</span><span>:</span><span></span><span>{</span><span>"type"</span><span>:</span><span></span><span>"array"</span><span>,</span><span></span><span>"items"</span><span>:</span><span></span><span>{</span><span>"type"</span><span>:</span><span></span><span>"string"</span><span>}</span><span>}</span><span>,</span><span>
       </span><span>"summary"</span><span>:</span><span></span><span>{</span><span>"type"</span><span>:</span><span></span><span>"string"</span><span>}</span><span>,</span><span>
       </span><span>"sentiment"</span><span>:</span><span></span><span>{</span><span>"enum"</span><span>:</span><span></span><span>[</span><span>"pos"</span><span>,</span><span></span><span>"neg"</span><span>]</span><span>}</span><span>,</span><span>
       ...
     </span><span>}</span><span>
   </span><span>}</span><span>
   </span></span></code></div></div></pre>
2. Sends this schema (and descriptions) to the LLM as part of the prompt.
3. The model generates a JSON object that fits the schema.
4. LangChain parses it, validates it with Pydantic, and gives you a ready-to-use Python object.

✅ Any mismatch (like wrong key type or missing field) → `ValidationError`

✅ This guarantees  **predictable** ,  **safe** , and **consistent** AI outputs.

---

## ⚙️ 4️⃣ Why This Is So Useful in GenAI Apps

| Use Case             | Benefit                                            |
| -------------------- | -------------------------------------------------- |
| Review analysis      | Extract sentiment, pros, cons from product reviews |
| Resume parsing       | Extract name, education, skills                    |
| Chatbot responses    | Structured, validated answers                      |
| Knowledge base       | Clean data extraction from documents               |
| Automation pipelines | Reliable JSON for downstream tools                 |

---

## 🧩 5️⃣ References & Resources

### 🔹 LangChain Structured Output Docs

📘 [https://python.langchain.com/docs/modules/model_io/structured_outputs]()

### 🔹 Pydantic Documentation

📘 [https://docs.pydantic.dev/latest/]()

### 🔹 OpenAI Structured Output Guide

📘 [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)

### 🔹 DeepLearning.AI + OpenAI Free Course

📘 [Structuring LLM Outputs]()

### 🔹 Instructor Library (Pydantic + OpenAI)

📘 [https://github.com/jxnl/instructor](https://github.com/jxnl/instructor)

---

## 🧭 6️⃣ Summary Table

| Concept                            | Description                 | Example                                  |
| ---------------------------------- | --------------------------- | ---------------------------------------- |
| **Pydantic Model**           | Defines schema of output    | `class Review(BaseModel)`              |
| **Field()**                  | Adds metadata + description | `Field(description="...")`             |
| **Literal**                  | Restricts values            | `"pos"`or `"neg"`                    |
| **with_structured_output()** | Forces LLM to follow schema | `model.with_structured_output(Review)` |
| **invoke()**                 | Sends input to model        | `.invoke("text")`                      |
| **Validated Output**         | Returns a Python object     | `Review(...)`                          |
