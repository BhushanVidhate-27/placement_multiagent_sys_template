from google.adk import Agent
from google.adk.tools import google_search


agent = Agent(
    name="resume-analyser",
    model="gemini-flash-latest",
    instruction="You help users ",
    tools=[google_search],
)