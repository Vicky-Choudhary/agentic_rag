from crewai import Agent
from llm.llm import crew_llm
web_search_agent = Agent(
    role="Expert Web Search Agent",
    goal="Identify and retrieve relevant web data for user queries",
    backstory="An expert in identifying valuable web sources for the user's needs",
    allow_delegation=False,
    verbose=True,
    llm=crew_llm
)

# Define the web scraping agent
web_scraper_agent = Agent(
    role="Expert Web Scraper Agent",
    goal="Extract and analyze content from specific web pages identified by the search agent",
    backstory="A highly skilled web scraper, capable of analyzing and summarizing website content accurately",
    allow_delegation=False,
    verbose=True,
    llm=crew_llm
)
