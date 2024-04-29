from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

@tool('DuckDuckGoSearch')
def search(query:str):
  """A search the web for information about a given topic"""
  return DuckDuckGoSearchRun().run(query)
