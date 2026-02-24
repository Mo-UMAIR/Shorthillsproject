🚀 LeetCode Contest Helper
Multi-Agent System using Google ADK
📌 Overview

LeetCode Contest Helper is a multi-agent system built using Google Agent Development Kit (ADK).

The system analyzes LeetCode contest problems, identifies key patterns and skills required, searches for relevant tutorials using Google Search, and generates a structured markdown report.

This project demonstrates:

Agent orchestration

Tool integration

Modular multi-agent architecture

Real-world automation workflow

🎯 Problem Statement

Design and implement a multi-agent system that:

Retrieves problems from a given LeetCode contest

Analyzes difficulty levels, tags, and patterns

Uses Google Search to find tutorials and learning resources

Generates a structured markdown summary

The system must:

Use Google ADK

Include 1 Root Agent + minimum 3 Sub-Agents

Use the built-in google_search tool

Implement at least 3 custom tools

Run using adk run or adk web

🧠 Architecture

The system follows a Sequential Multi-Agent Pattern.

Root Agent (LeetCodeContestHelper)
        ↓
ContestFetcherAgent
        ↓
ProblemAnalyzerAgent
        ↓
TutorialResearchAgent (uses google_search)
        ↓
ReportGeneratorAgent
🔹 Root Agent — LeetCodeContestHelper

Entry point of the system

Orchestrates sub-agents

Controls execution flow

🔹 Sub-Agents
1️⃣ ContestFetcherAgent

Extracts contest name from user input

Retrieves contest problems

2️⃣ ProblemAnalyzerAgent

Analyzes difficulty

Identifies tags

Detects problem-solving patterns

3️⃣ TutorialResearchAgent

Uses mandatory google_search tool

Finds tutorials and blog explanations

Searches relevant learning resources

4️⃣ ReportGeneratorAgent

Combines analysis + tutorials

Generates structured markdown file

🛠 Tools Used
✅ Built-in Tool (Mandatory)

google_search — Used for fetching tutorials and explanations

✅ Custom Tools Implemented

fetch_contest_problems

get_problem_details

generate_markdown_report

These tools provide real-world capabilities and support agent execution.

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
├── .env  (not committed)
└── .gitignore
⚙️ Setup Instructions
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

Go to: https://aistudio.google.com

Generate API Key

Create .env file in root directory:

GOOGLE_API_KEY=your_api_key_here

⚠ Do NOT push .env to GitHub.

▶️ Running the Project

Run from the project root directory:

CLI Mode
adk run leetcode_agent
Web Mode
adk web
Example Input
Analyze LeetCode Weekly Contest 400
Output

Console-based structured analysis

contest_summary.md generated in project directory

📦 Assignment Requirements Compliance
Requirement	Status
Google ADK Framework	✅ Used
Stable Gemini Model	✅ gemini-1.5-flash
Root Agent	✅ Implemented
Minimum 3 Sub-Agents	✅ 4 Sub-Agents
google_search Tool	✅ Integrated
3+ Custom Tools	✅ Implemented
problem_statement.md	✅ Included
CLI / Web Execution	✅ Supported
🏗 Design Approach

The system is designed with modularity and scalability in mind. Each agent has a clearly defined responsibility, ensuring clean separation of concerns. The Root Agent manages workflow, while sub-agents focus on specialized tasks such as analysis, research, and reporting. Custom tools provide structured data handling, and the built-in google_search tool enhances real-world capability. The sequential execution pattern ensures controlled orchestration and predictable behavior.

🧾 Brief Architecture Explanation (Submission Version)

This project implements a multi-agent architecture using Google ADK to analyze LeetCode contest problems and generate structured learning insights. A Root Agent orchestrates four specialized sub-agents responsible for fetching problems, analyzing difficulty and patterns, researching tutorials using the mandatory google_search tool, and generating a markdown summary report. Custom tools were implemented for data retrieval, metadata extraction, and report generation. The system follows a sequential execution pattern to ensure clear workflow management and modular responsibility separation. This design demonstrates agent orchestration, tool integration, and real-world task automation while adhering strictly to Google ADK requirements.

🚀 Future Improvements

Real-time LeetCode API integration

Parallel agent execution

Memory-based learning recommendations

Difficulty trend analysis

Personalized user study plans

👨‍💻 Author

Built using Google ADK for multi-agent system development.
