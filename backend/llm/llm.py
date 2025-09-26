import os 
from crewai import Agent, Task, Crew, LLM
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GEMINI=os.getenv("GEMINI")

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-specdec",
    temperature=0,
    max_tokens=500,
    timeout=None,
    max_retries=2,
)

crew_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=GEMINI,
    max_tokens=500,
    temperature=0.7
)


print("success")
