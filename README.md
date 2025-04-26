
# AutoSDLC Architect Pro

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Made With ❤️](https://img.shields.io/badge/Made%20with-❤️-red)

---

📚 **Project Overview**

AutoSDLC Architect Pro is a web-based solution designed to automate over 90% of the Software Development Lifecycle (SDLC) phases by leveraging local Generative AI models through Ollama. Users simply submit a software idea, and the system automatically generates structured functional requirements, non-functional requirements, system architecture, UML diagrams, prototype code, and evaluation metrics. It aims to streamline early-stage software development and reduce manual workload in requirement analysis, ...

---

✨ **Features**

- ✅ Automated Functional and Non-Functional Requirements Generation
- ✅ System Architecture and UML Diagram Generation
- ✅ Prototype Code Snippet Generation
- ✅ Automated Test Case Generation
- ✅ Modular Multi-Agent System Architecture
- ✅ Local LLM Model Processing (Ollama) for Privacy and Control
- ✅ Tabbed, User-Friendly Output Display

---

🛠 **Technology Stack**

- **Backend**: Python 3.10, Flask
- **Frontend**: HTML5, CSS3 (Flask Template Engine)
- **LLM Engine**: Ollama (Local Model Deployment)
- **Agents**: PlannerAgent, ModelerAgent, CoderAgent, EvaluatorAgent
- **Prompt Engineering**: Custom Pipelines and Templates
- **Deployment**: Localhost / EC2 Instance

---

⚙️ **Installation**

```bash
# Clone the repository
git clone https://github.com/yourusername/AutoSDLC_Architect_Pro.git
cd AutoSDLC_Architect_Pro

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Make sure Ollama is running with required local models

# Run the Flask App
python app.py
```
Access the application at: `http://localhost:5000/`

---

📁 **Project Structure**

```
AutoSDLC_Architect_Pro/
├── app.py
├── requirements.txt
├── README.md
├── prototype/
│   └── prompts/
│       ├── tutor_prompt.txt
│       ├── quiz_prompt.txt
│       ├── summary_prompt.txt
│       └── evaluation_prompt.txt
├── agents/
│   ├── planner_agent.py
│   ├── requirements_agent.py
│   ├── architecture_agent.py
│   ├── uml_agent.py
│   ├── code_agent.py
│   └── testcase_agent.py
└── utils/
    └── file_manager.py
```

---

📊 **Percentage of Automation**

| Module | Description | Automation Percentage |
|:---|:---|:---|
| Requirements Agent | Generates functional and non-functional requirements from idea | **95%** |
| Architecture Agent | Generates system architecture from specifications | **90%** |
| UML Agent | Produces UML diagrams (Class, Sequence) | **85%** |
| Code Agent | Generates initial prototype code | **80%** |
| Testcase Agent | Generates test cases based on system design | **85%** |
| Evaluator Agent | Organizes and displays outputs | **90%** |
| **Overall SDLC Automation** | From idea to prototype | **~88%** |

---

🧠 **Solution Architecture Overview**

The user submits a software idea via the web application. The Flask backend forwards the request to the **PlannerAgent**, which interacts with **Ollama** to generate functional and non-functional requirements. Once requirements are ready, the **ModelerAgent** processes requests for architecture and UML diagram generation. Finally, the **CoderAgent** and **EvaluatorAgent** generate code snippets, test cases, and organize the outputs into a user-friendly interface.

Each agent specializes in a different phase of the SDLC, forming a modular, highly scalable system.

---

🧩 **System Modeling and Sequences**

- **Solution Idea Input Sequence**: User idea → PlannerAgent → Ollama → Requirements generated.
- **Architecture and Modeling Sequence**: User requests modeling → ModelerAgent → Ollama → UML diagrams generated.
- **Prototype Code Generation Sequence**: User triggers code → CoderAgent → Ollama → Prototype code generated.

---

🚀 **Prototype Implementation Plan**

- Multi-Agent Coordination: PlannerAgent, ModelerAgent, CoderAgent, EvaluatorAgent
- Local LLM Deployment: Ollama models (Llama3, Codellama)
- Prompt Engineering Pipelines for each task
- Dataset Generation (Synthetic examples if needed)
- Flexible, expandable modular codebase

---

🌟 **Acknowledgements**

- **Florida Atlantic University**  
- **Course**: COT6930 – Generative AI and Software Development Lifecycles  
- **Instructor**: Dr. Fernando Koch  
- **Team: Team Z**
  - Pavan Thadari (pthadari2024@fau.edu)
  - Manish Lnu
  - Sree Teja Reddy Chappidi

---

# 📎 GitHub Repository

> Link: [GitHub Repository URL Here](https://github.com/pavanthadari/TEAM_Z_FINAL_PROJECT)

---

# 🧹 Professional Touch

- ✔️ Full automation from idea to prototype
- ✔️ Clean multi-agent system architecture
- ✔️ Local and private AI model processing
- ✔️ Flexible and extendable codebase

---
<!-- Updated by Pavan Thadari -->
