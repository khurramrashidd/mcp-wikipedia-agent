# 🤖 MCP Wikipedia Agent 2.0 (Flask & ADK-Ready)

## 📌 Overview

This project is an AI-powered agent built using a **Model Context Protocol (MCP)**-style architecture. The agent connects to an external data source (Wikipedia) to retrieve structured information, perform data analytics, and generate a highly interactive, user-friendly response. 

Version 2.0 features a completely redesigned, mobile-responsive UI with modern theming and a suite of 10 advanced features designed to enhance user experience and accessibility. The system demonstrates how AI agents can be integrated with real-world tools while maintaining a clear separation between reasoning, tool execution, and the user interface.

👉 **Live Demo:** https://mcp-wikipedia-agent.onrender.com

---

## 🚀 The 10 New Features (v2.0)

1. **🌗 Persistent Light/Dark Mode:** Seamless theme toggling saved via `localStorage`.
2. **🌍 Multi-Language Support:** Query Wikipedia in English, Spanish, French, or Hindi.
3. **🔊 Text-to-Speech (TTS):** Native browser integration to read summaries aloud in the selected language.
4. **📊 Content Analytics:** Auto-calculates estimated reading time and word count.
5. **🏷️ Category Extraction:** Automatically pulls and cleans Wikipedia category tags for broader context.
6. **📋 Quick Copy:** One-click "Copy to Clipboard" for easy sharing of summaries.
7. **🔗 Direct Source Integration:** Quick link to read the full, unedited article on Wikipedia.
8. **🕒 Local Search History:** Homepage automatically tracks and displays recent searches for quick access.
9. **📱 Fully Responsive Design:** CSS Grid & Flexbox implementation for perfect mobile and desktop scaling.
10. **🛡️ Enhanced Error UI:** Graceful, themed error states when a topic is not found.

---

## 🧠 Architecture & MCP Implementation

```text
User → UI (Flask) → Agent Layer → MCP Tool Layer → Wikipedia API
                                         ↓
                                  Structured Data
                                         ↓
                               Final Response (UI/API)
```

### Key Concept:
The agent does not directly fetch external data. Instead, it interacts with a highly decoupled tool layer (the MCP-style function `get_wikipedia_summary`). 

This allows external **Agent Development Kits (ADKs)** to easily consume the tool via the `/tool` API endpoint without relying on the web UI.

---

## 🌐 Endpoints

### 1. Web Interface (Human UI)
* `GET /` : Modern search homepage with history tracking.
* `GET /search?query=topic&lang=en` : Displays the formatted, interactive result card.

### 2. MCP API Endpoint (Machine / ADK UI)
* `GET /tool?query=topic&lang=en` : Returns pure structured JSON.
  * **Input:** `query` (string), `lang` (string code).
  * **Output:** JSON containing title, summary, word count, reading time, categories, and source URL.

---

## 🧪 Example API Response (`/tool?query=Mumbai`)

```json
{
  "title": "Mumbai",
  "summary": "Mumbai is the capital city of the Indian state of Maharashtra...",
  "url": "[https://en.wikipedia.org/wiki/Mumbai](https://en.wikipedia.org/wiki/Mumbai)",
  "word_count": 450,
  "reading_time": 2,
  "categories": ["Cities in Maharashtra", "Megacities", "Port cities in India"],
  "language": "en"
}
```

---

## 🎯 Hackathon Requirement Mapping

| Requirement | Implementation in Project |
| :--- | :--- |
| **Build an AI Agent** | Flask-based agent handling natural language queries and routing. |
| **Implemented using ADK** | The architecture strictly separates the tool logic, exposing a `/tool` endpoint ready for any ADK (LangChain, Vertex, etc.) to consume. |
| **MCP Integration** | Tool function (`get_wikipedia_summary`) acts as the isolated MCP server providing context to the agent. |
| **External Data Source** | Real-time Wikipedia API integration. |
| **Data Retrieval** | Retrieves and processes text, metadata, and URLs into structured JSON. |
| **Final Response** | Generates an interactive HTML interface for humans and a JSON schema for machines. |

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **External API:** `Wikipedia-API` library
* **Frontend:** HTML5, Vanilla JavaScript, Modern CSS (Variables, Grid, Flexbox)
* **Deployment Ready:** Gunicorn, Cloud Run / Render compatible

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone <your-repo-link>
cd mcp-wikipedia-agent

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

Open your browser and navigate to: `http://127.0.0.1:10000/`

---

## 👨‍💻 Author

**Khurram Rashid**

---

## 📜 License

This project was built for educational and hackathon purposes.
```
