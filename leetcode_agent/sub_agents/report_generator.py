from google.adk import Agent
from tools.generate_markdown_report import generate_markdown_report

report_generator = Agent(
    name="ReportGeneratorAgent",
    model="gemini-3-flash-preview",
    tools=[generate_markdown_report],
    instruction="""
    Combine contest problems, analysis, and tutorial links.
    Generate structured markdown report.
    Save using generate_markdown_report tool.
    """
)