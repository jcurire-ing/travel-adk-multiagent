from google.adk.agents import Agent

itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.0-flash",
    description="Creates day-by-day travel itineraries.",
    instruction="""You are a travel itinerary planner.
Your task is to build clear day-by-day itineraries.
Rules:
1. Organize the response by day.
2. Avoid overloaded schedules.
3. Include morning, afternoon and evening suggestions.""",
)
