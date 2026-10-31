from google.adk.agents import Agent

from travel_assistant.agents.budget import budget_agent
from travel_assistant.agents.culture import local_culture_agent
from travel_assistant.agents.itinerary import itinerary_agent
from travel_assistant.agents.risk import risk_reviewer_agent
from travel_assistant.agents.web_search import web_search_agent

travel_coordinator_agent = Agent(
    name="travel_coordinator_agent",
    model="gemini-2.0-flash",
    description="Coordinates a team of travel agents.",
    instruction="""You are the coordinator of a travel planning multiagent system.
Coordinate the sub-agents and return a structured response in Spanish.""",
    sub_agents=[
        web_search_agent,
        itinerary_agent,
        budget_agent,
        risk_reviewer_agent,
        local_culture_agent,
    ],
)
