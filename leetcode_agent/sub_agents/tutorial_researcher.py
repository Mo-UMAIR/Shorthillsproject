from google.adk import Agent
from google.adk.tools import google_search

tutorial_researcher = Agent(
    name="TutorialResearchAgent",
    model="gemini-3-flash-preview",
    tools=[google_search],
    instruction="""
    For each contest problem, search for tutorials and blog explanations.
    Use google_search tool.
    Return top 2 relevant tutorial links per problem.
    """
)