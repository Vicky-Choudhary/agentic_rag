import os 
from agent.agents import web_scraper_agent, web_search_agent
from crewai import Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool



search_tool = SerperDevTool()  # Tool for performing web searches
scrape_website = ScrapeWebsiteTool()  # Tool for extracting data from websites

# Define the web search task
search_task = Task(
    description=(
        "Identify the most relevant web page or article for the topic: '{topic}'. "
        "Use all available tools to search for and provide a link to a web page "
        "that contains valuable information about the topic. Keep your response concise."
    ),
    expected_output=(
        "A concise summary of the most relevant web page or article for '{topic}', "
        "including the link to the source and key points from the content."
    ),
    tools=[search_tool],
    agent=web_search_agent,
)

# Define the web scraping task
scraping_task = Task(
    description=(
        "Extract and analyze data from the given web page or website. Focus on the key sections "
        "that provide insights into the topic: '{topic}'. Use all available tools to retrieve the content, "
        "and summarize the key findings in a concise manner."
    ),
    expected_output=(
        "A detailed summary of the content from the given web page or website, highlighting the key insights "
        "and explaining their relevance to the topic: '{topic}'. Ensure clarity and conciseness."
    ),
    tools=[scrape_website],
    agent=web_scraper_agent,
)

