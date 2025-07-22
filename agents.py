from crewai import Agent, LLM
from tools import scraper_tool, file_tool
import os
from dotenv import load_dotenv

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-1.5-pro",
)

page_scanner = Agent(
    role="Web Page Scanner",
    goal="Capture and analyze webpage structure for URL: {url}",
    verbose=True,
    backstory="You are a web analysis expert who captures detailed webpage structures including key elements that automation scripts typically interact with.",
    tools=[scraper_tool, file_tool],
    allow_delegation=True,
    llm=gemini_llm
)

change_detector = Agent(
    role="UI Change Detector", 
    goal="Compare webpage snapshots and identify all structural and content changes",
    verbose=True,
    backstory="You are a change detection specialist who can identify even subtle differences between webpage versions that could affect automation.",
    tools=[file_tool],
    allow_delegation=False,
    llm=gemini_llm
)

impact_analyzer = Agent(
    role="Automation Impact Analyzer",
    goal="Assess how detected changes would impact browser automation and web agents",
    verbose=True,
    backstory="You are an expert in web automation who understands how UI changes break browser agents, scripts, and automated workflows.",
    tools=[],
    allow_delegation=False,
    llm=gemini_llm
)