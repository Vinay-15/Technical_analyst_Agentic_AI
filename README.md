# 🧠 Agentic AI Research Assistant

An **agent-based AI research assistant** built with **LangChain**, **Groq LLMs**, and **custom tools** to automatically research a topic, validate facts, analyze trends, generate citations, and optionally save results to a file — all through a single prompt-driven workflow.

---

## 🚀 Features

* 🔍 **Wikipedia-first research** (primary source validation)
* ✅ **Fact checking** to reduce hallucinations
* 📈 **Trend & popularity analysis** for topics
* 📚 **Automatic citation generation**
* 💾 **Save research output to a file**
* 🧩 **Agent-based tool calling** using LangChain
* 📦 **Structured JSON output** using Pydantic models

---

## Architecture Overview

```

User Prompt
↓
Agent (LangChain)
↓
Tool Selection & Reasoning Loop
├── Wikipedia Search
├── Fact Check
├── Trend Analysis
├── Citation Generation
└── Save Output
↓
Structured JSON Response

````

---

## 🛠️ Tech Stack

| Layer | Technology |
|----|----|
| Language | Python |
| LLM | Groq – `llama-3.3-70b-versatile` |
| Agent Framework | LangChain |
| Output Validation | Pydantic |
| Secrets Management | dotenv |

---

## 🧠 How It Works

1. User inputs a research topic.
2. The AI agent:

   * Searches **Wikipedia first**
   * Cross-checks facts using a fact-checking tool
   * Analyzes popularity or trends
   * Generates citations
   * Optionally saves the output
3. The final response is **always returned in structured JSON format**:

   ```json
   {
     "topic": "...",
     "summary": "...",
     "sources": ["..."],
     "tools_used": ["..."]
   }
   ```

---

## 🧩 Agent Tools Used

| Tool                | Description                                     |
| ------------------- | ----------------------------------------------- |
| `wiki_tool`         | Fetches and verifies information from Wikipedia |
| `fact_check`        | Validates claims against known sources          |
| `analyze_trends`    | Analyzes topic popularity or relevance          |
| `generate_citation` | Produces citations for sources                  |
| `save_tool`         | Saves generated research to a file              |

---

## 📂 Project Structure

```
.
├── main.py
├── tools.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vinay-15/Technical_analyst_Agentic_AI.git
cd Technical_analyst_Agentic_AI
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file (do **not** commit this):

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can refer to `.env.example` for the format.

---

## ▶️ Running the Application

```bash
python main.py
```

You’ll be prompted with:

```
What can I help you Research?
```

Example input:

```
Impact of AI on supply chain management
```

---

## 📤 Sample Output

```json
{
  "topic": "AI in Supply Chain Management",
  "summary": "Artificial intelligence is transforming supply chains by...",
  "sources": ["Wikipedia", "Industry Reports"],
  "tools_used": ["wiki_tool", "fact_check", "analyze_trends"]
}
```

---

## 🔐 Security Notes

* API keys are managed using `.env`
* `.env` is excluded via `.gitignore`
* Always rotate keys if exposed

---

## 🌱 Future Enhancements

* Web UI or Streamlit interface
* Multi-source research beyond Wikipedia
* Confidence scoring for facts
* Async tool execution
* Vector-based memory for long-term research

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!
Feel free to fork the repo or open an issue.

---

## 🌱 Hackathon Extensions (Easy Wins)

* 🌐 Web UI (Streamlit / Next.js)
* 🧠 Multi-agent collaboration
* 🔗 External APIs (news, finance, healthcare)
* 🧾 Confidence scoring per claim
* 🗂️ Vector memory for long-term research

---

## 👥 Ideal For

* Hackathons (LA Hacks, HackMIT, etc.)
* AI agent demos
* Research automation
* Tool-augmented LLM experiments

---

## 📜 License

MIT License

```
