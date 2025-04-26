
# AutoSDLC Architect Pro

---

📚 **Project Overview**

AutoSDLC Architect Pro is a web-based application designed to automate the majority of the Software Development Life Cycle (SDLC) phases using Generative AI technologies. By taking a natural language software idea from the user, the system generates functional requirements, non-functional requirements, system architecture, UML diagrams, prototype code snippets, and test cases — all powered through local LLMs (via Ollama) for maximum privacy and control.

---

✨ **Features**

- ✅ Automated Functional Requirements Generation
- ✅ Automated Non-Functional Requirements Generation
- ✅ System Architecture and Flow Design Automation
- ✅ UML Diagram Generation (Class, Sequence)
- ✅ Prototype Code Snippet Generation
- ✅ Automated Test Case Creation
- ✅ Organized and Interactive Tabbed Output Interface
- ✅ Local Model Processing (Ollama) — No Cloud Dependency
- ✅ Modular Agent-based Architecture for Scalability

---

🛠 **Technology Stack**

- **Backend**: Python 3.10, Flask
- **Frontend**: HTML5, CSS3 (Flask Templates)
- **AI/LLM Engine**: Ollama (Local Model Runner)
- **Agents**: Custom Python-based modular agents
- **Utilities**: Python FileManager, Prompt Engineering
- **Deployment**: Local Machine or Server Deployment

---

⚙️ **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/AutoSDLC_Architect_Pro.git
   cd AutoSDLC_Architect_Pro
   ```

2. **Set Up Python Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama (Local LLM Server)**
   > Ensure Ollama is installed and running. Models like `llama3`, `codellama`, or fine-tuned SDLC models are recommended.

5. **Run the App**
   ```bash
   python app.py
   ```

6. **Access the App**
   Open your browser and go to `http://localhost:5000/`

---

📁 **Project Structure**

```
AutoSDLC_Architect_Pro/
│
├── app.py                    # Main Flask application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── utils/
│   └── file_manager.py        # File handling utilities
├── agents/
│   ├── planner_agent.py       # Planning and task distribution
│   ├── requirements_agent.py  # Generates requirements
│   ├── architecture_agent.py  # Generates system architecture descriptions
│   ├── uml_agent.py           # Generates UML diagrams
│   ├── code_agent.py          # Generates prototype code
│   └── testcase_agent.py      # Generates test cases
└── static/ (optional)         # UI static files (CSS/JS)
```

---

📊 **Percentage of Automation**

| Module | Description | Automation Percentage |
|:---|:---|:---|
| Requirements Agent | Functional and non-functional requirements generation | **95%** |
| Architecture Agent | System architecture design and description | **90%** |
| UML Agent | UML diagrams (Class, Sequence) | **85%** |
| Code Agent | Prototype code snippet generation | **80%** |
| Testcase Agent | Test case generation based on requirements | **85%** |
| Evaluator Agent | Aggregating and organizing outputs | **90%** |
| **Overall Automation** | End-to-end SDLC coverage based on user input | **~88%** |

> ⚡ Note: Minor human fine-tuning might still be needed for large or complex projects.

---

🙏 **Acknowledgements**

- Special thanks to the developers and open-source contributors behind **Ollama** for enabling local, secure LLM execution.
- This project was created as part of the **COT6930 - Generative AI and Software Development Lifecycles** course at Florida Atlantic University under the supervision of **Dr. Fernando Koch**.
- Developed by **Team Z**:
  - [Your Name 1]
  - [Your Name 2]
  - [Your Name 3]

---
