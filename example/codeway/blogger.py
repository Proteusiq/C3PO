from datetime import date
from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
from langchain_community.tools import DuckDuckGoSearchRun




technology = input("Which technology to explore? ")

DAY_LOOKUP = {
    '01': 'st',
    '21': 'st',
    '31': 'st',
    '02': 'nd',
    '22': 'nd',
    '03': 'rd',
    '23': 'rd'
}


today = (f"{date.today(): %B %d{DAY_LOOKUP.get('%B', 'th')} %Y}")


@tool('DuckDuckGoSearch')
def search(query:str):
  """A search the web for information about a given topic"""
  return DuckDuckGoSearchRun().run(query)

# Define the researcher agent
researcher = Agent(
  role='Senior Research Analyst',
  goal='Discover and analyze novel technology',
  backstory=f"""A curious explorer at a {technology} tech think tank, skilled in identifying and evaluating new trends in technology.
  You thrive on uncovering innovative ideas and translating them into digestible insights. Today is {today}""",
  verbose=True,
  max_inter=3,
  allow_delegation=False,
  tools=[search]
)

# Define the writer agent
writer = Agent(
  role='Storytelling Content Creator',
  goal='Write engaging and narrative-driven blog posts about tech topic',
  backstory=f"""A talented storyteller known for captivating articles that combine technical accuracy with narrative flair.
  You excel at transforming intricate tech concepts into relatable stories, appealing to both experts and enthusiasts. Today is {today}""",
  verbose=True,
  allow_delegation=True,
  max_inter=5,
)

# Task for the researcher
research = Task(
  description=f"""Research the most exciting {technology} advancements of the current year.
  Focus on identifying innovative technologies and their implications for various industries.""",
  expected_output="A detailed research report in an easy-to-understand format",
  agent=researcher
)

# Task for the writer
write = Task(
  description="""Craft a blog post based on the research findings.
  The post should weave the technical details into a compelling narrative that captivates a tech-savvy audience.
  Use vivid language to create an engaging and memorable reader experience.""",
  expected_output="A creatively written blog post of at least 6 paragraphs in a story-like way in a markdown",
  agent=writer
)

# Create a crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[research, write],
  verbose=2
)

# Execute the tasks
results = crew.kickoff()

print("######################")
print(results)
