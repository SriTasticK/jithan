# 🤖 Jithan – Autonomous AI Agent

![Python](https://img.shields.io/badge/python-3.11+-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-black)
![License](https://img.shields.io/badge/license-GPL--3.0-green)
![Status](https://img.shields.io/badge/status-active-success)

An autonomous AI agent built using Google's Gemini API that can iteratively reason, call tools, and complete tasks through a loop-based execution model.

---

## 🚀 Features

- 🔁 Iterative reasoning loop (agent-style execution)
- 🧠 Tool-calling support (function execution)
- 💬 Stateful conversation memory
- ⚡ Fast inference using Gemini Flash
- 🛠️ Modular tool system
- 🔒 Controlled loop (max iterations)

---

## 🧱 Architecture

```text
            ┌──────────────┐
            │   User Input │
            └──────┬───────┘
                   │
                   ▼
           ┌───────────────┐
           │ Gemini Model  │
           └──────┬────────┘
                  │
        ┌─────────▼─────────┐
        │ Function Call?    │
        └──────┬────────────┘
               │ Yes
               ▼
       ┌───────────────┐
       │ Tool Execution│
       └──────┬────────┘
              │
              ▼
       ┌───────────────┐
       │ Tool Response │
       └──────┬────────┘
              │
              └──────► Back to Model

(No function call)
        ▼
┌──────────────────────┐
│ Final Response Output│
└──────────────────────┘
📂 Project Structure
.
├── main.py              # Agent loop & orchestration
├── prompts.py          # System prompt
├── call_function.py    # Tool execution layer
├── pyproject.toml      # Dependencies (uv)
├── .env                # API keys
⚙️ Setup
1. Install uv
curl -Ls https://astral.sh/uv/install.sh | sh
2. Clone repo
git clone https://github.com/SriTasticK/jithan.git
cd jithan
3. Install dependencies
uv sync
4. Set environment variable

Create .env:

GEMINI_API_KEY=your_api_key_here
▶️ Usage
uv run main.py "your prompt here"
Example:
uv run main.py "Explain how the calculator renders results to the console"
🛠️ Example Tool

Here’s a simple example of how tools are structured:

def add(a: int, b: int):
    return a + b

The model can call this automatically:

User: What is 5 + 7?
Agent:
 → Calls function: add
 → Returns: 12
Final Answer: 12
🎬 Demo
$ uv run main.py "how does the calculator render results to the console?"

→ Calling function: get_files_info
→ Calling function: get_file_content

Final response:

The calculator renders results using Python's print() function. 
It formats output via a helper function and prints it to the console.
🔁 How It Works
User prompt → sent to model
Model decides: answer OR call tool
If tool is called → executed locally
Tool result → appended to conversation
Loop continues
Stops when model returns final answer
🧠 Core Concepts
Function Calling → Model interacts with real code
Memory → Full conversation stored in messages
Agent Loop → Iterative reasoning until completion
Termination → Stops when no function calls
⚠️ Limitations
No retry logic for failed tools
No streaming output
Limited tool ecosystem
🔮 Future Improvements
🔁 Retry + error handling
📊 Logging & observability
🌐 Web browsing tools
🧠 Planning layer (ReAct / ToT)
🧩 Plugin system
📜 License

GPL-3.0 License

🙌 Contributing

PRs are welcome. Open an issue for ideas or bugs.

⭐ Support

If you like this project, give it a star ⭐
