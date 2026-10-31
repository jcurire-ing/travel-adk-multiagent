from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-2.0-flash",
    description="Searches the web for current travel information.",
    instruction="""You are a travel research agent.
Your task is to search the web when the user needs current travel information.
Rules:
1. Use Google Search when current information is needed.
2. Prefer official or reliable sources.
3. Summarize findings clearly.""",
    tools=[google_search],
)
