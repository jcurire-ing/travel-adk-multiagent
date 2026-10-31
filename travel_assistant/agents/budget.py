from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.0-flash",
    description="Estimates basic travel budgets.",
    instruction="""You are a travel budget advisor.
Your task is to estimate a basic travel budget.
Use the available tool when destination, days and daily budget are provided.""",
    tools=[estimate_trip_budget],
)
