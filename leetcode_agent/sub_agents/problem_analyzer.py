from google.adk import Agent
from tools.get_problem_details import get_problem_details

problem_analyzer = Agent(
    name="ProblemAnalyzerAgent",
    model="gemini-3-flash-preview",
    tools=[get_problem_details],
    instruction="""
    For each problem, fetch difficulty and tags.
    Identify common patterns (Graph, DP, Greedy, etc.).
    Return structured analysis.
    """
)