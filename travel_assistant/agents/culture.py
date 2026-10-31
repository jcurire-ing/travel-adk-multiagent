from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_info

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.0-flash",
    description="Recommends local food, customs, and useful phrases.",
    instruction="""You are a local culture advisor.
Your task is to provide cultural insights, typical dishes, customs, and phrases.
Use the available tool when destination is known.""",
    tools=[get_local_culture_info],
)
