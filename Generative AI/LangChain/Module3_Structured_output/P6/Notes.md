# 🧠 Understanding: Structured Output with JSON Schema

When you use `with_structured_output(json_schema)` in LangChain (or the new OpenAI SDK),

you’re **telling the model to return responses that strictly follow the schema** you define — just like validating JSON in APIs.

This is different from:

* **TypedDict** ✅ (Python typing-based schema)
* **Pydantic BaseModel** ✅ (Python class-based schema)
* **JSON Schema** ✅ (Language-agnostic schema, widely used in APIs)

All three achieve the same goal — **forcing structure in LLM output** — but JSON Schema is the  **most flexible and universal** .

---

## 💡 Step-by-Step Breakdown

### 1. Import and Setup

<pre class="overflow-visible!" data-start="922" data-end="1042"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> langchain_openai </span><span>import</span><span> ChatOpenAI
</span><span>from</span><span> dotenv </span><span>import</span><span> load_dotenv

load_dotenv()
model = ChatOpenAI()
</span></span></code></div></div></pre>

You load your OpenAI key and initialize a model that can follow structured output constraints.

---

### 2. Define a JSON Schema

<pre class="overflow-visible!" data-start="1173" data-end="2300"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>json_schema = {
    </span><span>"title"</span><span>: </span><span>"Review"</span><span>,
    </span><span>"type"</span><span>: </span><span>"object"</span><span>,
    </span><span>"properties"</span><span>: {
        </span><span>"key_themes"</span><span>: {
            </span><span>"type"</span><span>: </span><span>"array"</span><span>,
            </span><span>"items"</span><span>: {</span><span>"type"</span><span>: </span><span>"string"</span><span>},
            </span><span>"description"</span><span>: </span><span>"Write down all the key themes discussed in the review in a list"</span><span>,
        },
        </span><span>"summary"</span><span>: {</span><span>"type"</span><span>: </span><span>"string"</span><span>, </span><span>"description"</span><span>: </span><span>"A brief summary of the review"</span><span>},
        </span><span>"sentiment"</span><span>: {
            </span><span>"type"</span><span>: </span><span>"string"</span><span>,
            </span><span>"enum"</span><span>: [</span><span>"pos"</span><span>, </span><span>"neg"</span><span>],
            </span><span>"description"</span><span>: </span><span>"Return sentiment of the review either negative, positive or neutral"</span><span>,
        },
        </span><span>"pros"</span><span>: {
            </span><span>"type"</span><span>: [</span><span>"array"</span><span>, </span><span>"null"</span><span>],
            </span><span>"items"</span><span>: {</span><span>"type"</span><span>: </span><span>"string"</span><span>},
            </span><span>"description"</span><span>: </span><span>"Write down all the pros inside a list"</span><span>,
        },
        </span><span>"cons"</span><span>: {
            </span><span>"type"</span><span>: [</span><span>"array"</span><span>, </span><span>"null"</span><span>],
            </span><span>"items"</span><span>: {</span><span>"type"</span><span>: </span><span>"string"</span><span>},
            </span><span>"description"</span><span>: </span><span>"Write down all the cons inside a list"</span><span>,
        },
        </span><span>"name"</span><span>: {
            </span><span>"type"</span><span>: [</span><span>"string"</span><span>, </span><span>"null"</span><span>],
            </span><span>"description"</span><span>: </span><span>"Write the name of the reviewer"</span><span>,
        },
    },
    </span><span>"required"</span><span>: [</span><span>"key_themes"</span><span>, </span><span>"summary"</span><span>, </span><span>"sentiment"</span><span>],
}
</span></span></code></div></div></pre>

Let’s unpack this 👇

| Key                             | Meaning                                                        |
| ------------------------------- | -------------------------------------------------------------- |
| `"title"`                     | A human-readable name for your schema.                         |
| `"type": "object"`            | The top-level data must be a JSON object (like a Python dict). |
| `"properties"`                | Defines the fields (keys) and their expected types.            |
| `"type": "array"`             | That field expects a list.                                     |
| `"items": {"type": "string"}` | The list should only contain strings.                          |
| `"enum": ["pos", "neg"]`      | Restricts values to these exact strings.                       |
| `"required": [...]`           | Keys that**must**be present in the output.               |

---

### 3. Bind the Schema to the Model

<pre class="overflow-visible!" data-start="2889" data-end="2963"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>structured_model = model.with_structured_output(json_schema)
</span></span></code></div></div></pre>

🧩 This line is **crucial** — it instructs the model:

> “You must return the output as a valid JSON object matching this schema.”

LangChain (or OpenAI API under the hood) automatically enforces and validates this structure.

---

### 4. Invoke the Model

<pre class="overflow-visible!" data-start="3221" data-end="3310"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>result = structured_model.invoke(</span><span>""" ... review text ... """</span><span>)
</span><span>print</span><span>(result)
</span></span></code></div></div></pre>

👉 The LLM reads your schema, analyzes the text, and produces a **Python dictionary** like this:

<pre class="overflow-visible!" data-start="3410" data-end="3881"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>{
    </span><span>'key_themes'</span><span>: [</span><span>'Camera'</span><span>, </span><span>'Battery'</span><span>, </span><span>'Performance'</span><span>, </span><span>'S-Pen'</span><span>, </span><span>'Build Quality'</span><span>],
    </span><span>'summary'</span><span>: </span><span>'The Samsung Galaxy S24 Ultra is a high-performance device with an exceptional camera, strong battery life, and S-Pen support but is heavy and expensive.'</span><span>,
    </span><span>'sentiment'</span><span>: </span><span>'pos'</span><span>,
    </span><span>'pros'</span><span>: [</span><span>'Powerful processor'</span><span>, </span><span>'200MP camera'</span><span>, </span><span>'Fast charging'</span><span>, </span><span>'S-Pen support'</span><span>],
    </span><span>'cons'</span><span>: [</span><span>'Heavy size'</span><span>, </span><span>'Expensive'</span><span>, </span><span>'Bloatware in One UI'</span><span>],
    </span><span>'name'</span><span>: </span><span>'Nitish Singh'</span><span>
}
</span></span></code></div></div></pre>

✅ The model is now  **guaranteed to return a structured dictionary** , not free text!

---

## ⚙️ How It Works Internally

1. **LangChain → OpenAI** : LangChain sends your schema along with the prompt.
2. **OpenAI’s JSON Mode** (structured output feature):

   Forces the model to output only JSON that matches your schema.
3. **LangChain parses & validates** :

   It parses the response safely into a Python dict using the JSON Schema validator.

---

## 🧠 When to Use JSON Schema

| Use Case                                             | Recommended Schema Type |
| ---------------------------------------------------- | ----------------------- |
| Small project / quick prototype                      | `TypedDict`           |
| Larger app with validation & error handling          | `Pydantic BaseModel`  |
| Multi-language systems (Java, Node, etc.) or OpenAPI | `JSON Schema`         |

---

## 📚 Further Learning Resources

Here are the best resources to master this:

1. **🧾 Official JSON Schema Docs:**

   [https://json-schema.org/understanding-json-schema]()
2. **🧠 OpenAI Structured Outputs Guide:**

   [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)
3. **🧩 LangChain Structured Output Reference:**

   [https://python.langchain.com/docs/how_to/structured_output/]()
4. **📘 Learn JSON Schema (Interactive):**

   [https://www.learnjsonschema.com/]()

---

## 🪄 Bonus Tip

If you print:

<pre class="overflow-visible!" data-start="5373" data-end="5406"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>print</span><span>(</span><span>type</span><span>(result))
</span></span></code></div></div></pre>

You’ll see:

<pre class="overflow-visible!" data-start="5419" data-end="5441"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span><</span><span>class</span><span></span><span>'dict'</span><span>>
</span></span></code></div></div></pre>

So you can access items easily:

<pre class="overflow-visible!" data-start="5475" data-end="5540"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>print</span><span>(result[</span><span>"summary"</span><span>])
</span><span>print</span><span>(result[</span><span>"sentiment"</span><span>])</span></span></code></div></div></pre>
