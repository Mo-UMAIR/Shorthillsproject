from google.adk import Agent
from sub_agents.contest_fetcher import contest_fetcher
from sub_agents.problem_analyzer import problem_analyzer
from sub_agents.tutorial_researcher import tutorial_researcher
from sub_agents.report_generator import report_generator

root_agent = Agent(
    name="LeetCodeContestHelper",
    model="gemini-3-flash-preview",
    sub_agents=[
        contest_fetcher,
        problem_analyzer,
        tutorial_researcher,
        report_generator
    ],
    instruction="""
    Workflow:
    1. Identify contest name.
    2. Fetch contest problems.
    3. Analyze problems.
    4. Research tutorials using google_search.
    5. Generate final markdown summary.
    """
)