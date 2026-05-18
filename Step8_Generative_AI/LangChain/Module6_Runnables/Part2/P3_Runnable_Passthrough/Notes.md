## ⚙️ What is `RunnablePassthrough`?

`RunnablePassthrough` is a **built-in utility runnable** in LangChain that simply  **returns the input it receives without changing it** .

It’s extremely useful when you need:

* To **preserve or forward** data through a chain.
* To **merge or branch** data flows in parallel chains.
* To **debug or inspect** intermediate results in pipelines.

In essence:

<pre class="overflow-visible!" data-start="632" data-end="693"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>RunnablePassthrough(</span><span>input</span><span>) ➜ returns same </span><span>input</span><span>
</span></span></code></div></div></pre>

---

## 🧩 Basic Example

<pre class="overflow-visible!" data-start="721" data-end="960"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> langchain_core.runnables </span><span>import</span><span> RunnablePassthrough

</span><span># Create a passthrough runnable</span><span>
passthrough = RunnablePassthrough()

</span><span># Run it with some data</span><span>
result = passthrough.invoke({</span><span>"message"</span><span>: </span><span>"Hello LangChain!"</span><span>})
</span><span>print</span><span>(result)
</span></span></code></div></div></pre>

🟢 **Output:**

<pre class="overflow-visible!" data-start="977" data-end="1022"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>{</span><span>'message'</span><span>: </span><span>'Hello LangChain!'</span><span>}
</span></span></code></div></div></pre>

✅ Nothing changes — the input is simply returned.

---

## 🧠 Why It’s Useful

In real-world LangChain pipelines, you often have **multiple Runnables connected** using `RunnableSequence` or `RunnableParallel`.

You might want to keep some parts of the data *untouched* while transforming others.

### Example — Combining with `RunnableParallel`

<pre class="overflow-visible!" data-start="1371" data-end="1968"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> langchain_core.runnables </span><span>import</span><span> RunnableParallel, RunnablePassthrough
</span><span>from</span><span> langchain_core.prompts </span><span>import</span><span> PromptTemplate
</span><span>from</span><span> langchain_openai </span><span>import</span><span> ChatOpenAI

</span><span># Prompt + LLM runnable</span><span>
prompt = PromptTemplate.from_template(</span><span>"Summarize the following text:\n{text}"</span><span>)
llm = ChatOpenAI(model=</span><span>"gpt-4-turbo"</span><span>)

</span><span># Define parallel pipeline</span><span>
chain = RunnableParallel({
    </span><span>"original"</span><span>: RunnablePassthrough(),   </span><span># keeps input unchanged</span><span>
    </span><span>"summary"</span><span>: prompt | llm,              </span><span># generates a summary</span><span>
})

output = chain.invoke({</span><span>"text"</span><span>: </span><span>"LangChain simplifies LLM orchestration."</span><span>})
</span><span>print</span><span>(output)
</span></span></code></div></div></pre>

🟩 **Output:**

<pre class="overflow-visible!" data-start="1985" data-end="2136"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>{
  </span><span>"original"</span><span>: {</span><span>"text"</span><span>: </span><span>"LangChain simplifies LLM orchestration."</span><span>},
  </span><span>"summary"</span><span>: </span><span>"LangChain helps organize LLM workflows efficiently."</span><span>
}
</span></span></code></div></div></pre>

### 💡 Here:

* `RunnablePassthrough()` kept the original text.
* `prompt | llm` produced the summary.
* Both outputs were returned together in one dictionary.

---

## 🧩 When to Use It

| Situation                                          | Why `RunnablePassthrough`Helps |
| -------------------------------------------------- | -------------------------------- |
| You need to retain raw input for logging/debugging | It passes data through untouched |
| You want to merge multiple outputs                 | Useful in `RunnableParallel`   |
| You want a placeholder step                        | Acts as a no-op (no operation)   |
| You’re incrementally building a pipeline          | Keeps data structure consistent  |

---

## 🧰 Advanced Example — Adding Metadata

You can extend passthrough logic using **RunnableLambda** along with it:

<pre class="overflow-visible!" data-start="2847" data-end="3139"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>from</span><span> langchain_core.runnables </span><span>import</span><span> RunnablePassthrough, RunnableLambda, RunnableSequence

add_meta = RunnableLambda(</span><span>lambda</span><span> x: {</span><span>"data"</span><span>: x, </span><span>"meta"</span><span>: </span><span>"v1.0"</span><span>})
chain = RunnableSequence(first=RunnablePassthrough(), last=add_meta)

</span><span>print</span><span>(chain.invoke({</span><span>"message"</span><span>: </span><span>"Pipeline active"</span><span>}))
</span></span></code></div></div></pre>

🟢 **Output:**

<pre class="overflow-visible!" data-start="3156" data-end="3226"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>{</span><span>'data'</span><span>: {</span><span>'message'</span><span>: </span><span>'Pipeline active'</span><span>}, </span><span>'meta'</span><span>: </span><span>'v1.0'</span><span>}
</span></span></code></div></div></pre>

---

## 🔗 Authoritative Reading & Learning Resources

1. **Official RunnablePassthrough Docs (LangChain)**

   🔗 [https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnablePassthrough.html]()
2. **LangChain Expression Language (LCEL) Concepts**

   🔗 [https://python.langchain.com/docs/concepts/lcel/](https://python.langchain.com/docs/concepts/lcel/?utm_source=chatgpt.com)
3. **How to use Runnables (Guide)**

   🔗 [https://python.langchain.com/docs/how_to/](https://python.langchain.com/docs/how_to/)
4. **LangChain Cookbook – Runnables Section (GitHub)**

   🔗 [https://github.com/langchain-ai/langchain/tree/master/cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)
5. **Medium: Mastering Runnables and LCEL**

   🔗 [https://medium.com/@mishra.sagar25/langchain-series-part-8-mastering-runnables-and-lcel-9e1273aeed7a]()
