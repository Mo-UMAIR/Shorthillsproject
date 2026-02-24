from google.adk import Agent
from tools.fetch_contest_problems import fetch_contest_problems

contest_fetcher = Agent(
    name="ContestFetcherAgent",
    model="gemini-3-flash-preview",
    tools=[fetch_contest_problems],
    instruction="""
    Extract contest name from user input.
    Use fetch_contest_problems tool.
    Return structured list of problems.
    """
)