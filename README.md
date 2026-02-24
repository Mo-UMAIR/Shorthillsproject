# 🚀 LeetCode Contest Helper
### Multi-Agent System Built with Google ADK

**LeetCode Contest Helper** is an advanced multi-agent system developed using the **Google Agent Development Kit (ADK)**. The system automates the analysis of LeetCode contest problems by identifying core patterns, fetching high-quality tutorials via Google Search, and generating structured learning summaries in Markdown format.

---

## 📖 Overview
This project demonstrates the power of modular agentic workflows, featuring:
* **Multi-agent orchestration** using the Google ADK.
* **Deep Tool Integration**: Combines built-in Google Search with custom-built data tools.
* **Sequential Architecture**: Ensures a reliable pipeline from data fetching to report generation.
* **Real-world automation**: Leverages Gemini 1.5 Flash for intelligent problem-solving analysis.

---

## 🎯 Objective
The objective of this project is to implement a functional **agentic system** that:
* Accepts a LeetCode contest name as input.
* Retrieves specific contest problems and metadata.
* Analyzes difficulty, tags (DP, Graph, BFS, etc.), and dominant patterns.
* Uses Google Search to find high-quality tutorials and explanations.
* Generates a structured `contest_summary.md` file for the user.

---

## 🧠 System Architecture
The project follows a **Sequential Agent Orchestration Pattern**.

### Workflow:
1.  **Root Agent (`LeetCodeContestHelper`)**: The entry point that controls the workflow execution and ensures structured response generation.
2.  **ContestFetcherAgent**: Extracts the contest name from user input and retrieves problem data using custom tools.
3.  **ProblemAnalyzerAgent**: Determines difficulty levels and identifies technical patterns/tags.
4.  **TutorialResearchAgent**: Uses the mandatory `Google Search` tool to find external learning resources.
5.  **ReportGeneratorAgent**: Combines all outputs into a final, polished Markdown file.

---

## 🛠️ Tools Integration

| Tool | Type | Description |
| :--- | :--- | :--- |
| `Google Search` | **Built-in** | Mandatory tool for finding tutorials and blog explanations. |
| `fetch_contest_problems` | **Custom** | Fetches the list of problems for a given contest. |
| `get_problem_details` | **Custom** | Retrieves specific metadata for individual problems. |
| `generate_markdown_report` | **Custom** | Logic for compiling and saving the final `.md` file. |

---

## 📂 Project Structure
```text
leetcode_contest_helper/
├── leetcode_agent/
│   ├── agent.py               # Root Agent & Orchestration logic
│   ├── sub_agents/            # Individual Agent definitions
│   │   ├── contest_fetcher.py
│   │   ├── problem_analyzer.py
│   │   ├── tutorial_researcher.py
│   │   └── report_generator.py
│   └── tools/                 # Tool implementations
│       ├── fetch_contest_problems.py
│       ├── get_problem_details.py
│       └── generate_markdown_report.py
├── problem_statement.md       # Compliance requirements
├── README.md
├── requirements.txt
└── .env                       # API Keys (Git ignored)

```
---

## 📦 Assignment Requirements Compliance

| Requirement | Status |
|-------------|--------|
| Google ADK Framework | ✅ Used |
| Stable Gemini Model | ✅ gemini-1.5-flash |
| Root Agent | ✅ Implemented |
| Minimum 3 Sub-Agents | ✅ 4 Sub-Agents |
| google_search Tool | ✅ Integrated |
| 3+ Custom Tools | ✅ Implemented |
| problem_statement.md | ✅ Included |
| CLI / Web Execution | ✅ Supported |

---

## 🏗 Design Approach

The system is designed with modularity and scalability in mind. Each agent has a clearly defined responsibility, ensuring clean separation of concerns. The Root Agent manages workflow, while sub-agents focus on specialized tasks such as analysis, research, and reporting. Custom tools provide structured data handling, and the built-in `google_search` tool enhances real-world capability. The sequential execution pattern ensures controlled orchestration and predictable behavior.

---

## 🧾 Brief Architecture Explanation (Submission Version)

This project implements a multi-agent architecture using Google ADK to analyze LeetCode contest problems and generate structured learning insights. A Root Agent orchestrates four specialized sub-agents responsible for fetching problems, analyzing difficulty and patterns, researching tutorials using the mandatory `google_search` tool, and generating a markdown summary report. Custom tools were implemented for data retrieval, metadata extraction, and report generation. The system follows a sequential execution pattern to ensure clear workflow management and modular responsibility separation. This design demonstrates agent orchestration, tool integration, and real-world task automation while strictly adhering to Google ADK requirements.

