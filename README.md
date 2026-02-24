🚀 LeetCode Contest Helper
Multi-Agent System Built with Google ADK
📖 Overview

LeetCode Contest Helper is a multi-agent system developed using the Google Agent Development Kit (ADK).

The system analyzes LeetCode contest problems, identifies core problem-solving patterns, searches for relevant tutorials using Google Search, and generates a structured learning summary in markdown format.

This project demonstrates:

Multi-agent orchestration

Tool integration

Modular architecture

Real-world automation using LLM agents

🎯 Objective

The objective of this project is to design and implement a functional agentic system that:

Accepts a LeetCode contest name as input

Retrieves contest problems

Analyzes difficulty, tags, and patterns

Uses Google Search to find learning resources

Generates a structured markdown summary

The system strictly follows Google ADK requirements.

🧠 System Architecture

The project uses a Sequential Agent Orchestration Pattern.

Root Agent (LeetCodeContestHelper)
        ↓
ContestFetcherAgent
        ↓
ProblemAnalyzerAgent
        ↓
TutorialResearchAgent (uses google_search)
        ↓
ReportGeneratorAgent
🔷 Root Agent — LeetCodeContestHelper

Entry point of the system

Controls workflow execution

Delegates tasks to specialized sub-agents

Ensures structured response generation

🔷 Sub-Agents
1️⃣ ContestFetcherAgent

Extracts contest name from user input

Retrieves contest problems

Uses custom data-fetching tool

2️⃣ ProblemAnalyzerAgent

Determines difficulty level

Identifies tags (Graph, DP, BFS, etc.)

Detects dominant patterns

Summarizes technical focus of contest

3️⃣ TutorialResearchAgent

Uses mandatory google_search tool

Finds relevant tutorials and blog explanations

Enhances learning value of output

4️⃣ ReportGeneratorAgent

Combines all structured outputs

Generates final markdown file:

contest_summary.md
🛠 Tools Integration
✅ Built-in ADK Tool

google_search (Mandatory Requirement)

✅ Custom Tools Implemented

fetch_contest_problems

get_problem_details

generate_markdown_report

Each tool is documented and typed properly, providing real-world capability to agents.

📂 Project Structure
leetcode_contest_helper/
│
├── leetcode_agent/
│   ├── agent.py
│   ├── __init__.py
│   │
│   ├── sub_agents/
│   │   ├── contest_fetcher.py
│   │   ├── problem_analyzer.py
│   │   ├── tutorial_researcher.py
│   │   └── report_generator.py
│   │
│   └── tools/
│       ├── fetch_contest_problems.py
│       ├── get_problem_details.py
│       └── generate_markdown_report.py
│
├── problem_statement.md
├── README.md
├── requirements.txt
├── .env (excluded)
└── .gitignore
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd leetcode_contest_helper
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

Windows

.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Gemini API Key

Visit: https://aistudio.google.com

Generate API Key

Create .env file:

GOOGLE_API_KEY=your_api_key_here

⚠ Never commit .env.

▶️ Running the System

Run from the root directory:

CLI Mode
adk run leetcode_agent
Web Mode
adk web
Example Input
Analyze LeetCode Weekly Contest 400
Output

Structured console response

Generated file:

contest_summary.md
✅ Assignment Compliance Checklist
Requirement	Status
Google ADK Framework	✅
Stable Gemini Model	✅ gemini-1.5-flash
Root Agent	✅
Minimum 3 Sub-Agents	✅ 4
Mandatory google_search Tool	✅
3+ Custom Tools	✅
problem_statement.md Included	✅
CLI / Web Executable	✅
🏗 Design Philosophy

This system is built with:

Clear separation of responsibilities

Modular agent design

Scalable architecture

Real-world tool usage

Structured orchestration logic

The sequential execution pattern ensures predictable behavior and clear delegation across agents.

🧾 Brief Architecture Summary (Submission Version)

This project implements a multi-agent architecture using Google ADK to analyze LeetCode contest problems and generate structured learning insights. A Root Agent orchestrates four specialized sub-agents responsible for retrieving problems, analyzing difficulty and patterns, researching tutorials using the mandatory google_search tool, and generating a markdown summary report. Custom tools provide data retrieval, metadata analysis, and report generation capabilities. The system follows a sequential execution pattern to ensure modularity and controlled orchestration. This design demonstrates real-world agent collaboration, tool integration, and scalable multi-agent workflow while strictly adhering to Google ADK requirements.

🔮 Future Enhancements

Real-time LeetCode API integration

Parallel agent execution

User-specific study plans

Trend analysis across contests

Memory-based personalization

👨‍💻 Developed Using

Google ADK

Gemini API

Python
