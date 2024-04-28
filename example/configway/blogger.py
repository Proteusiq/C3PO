from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.browser import search


@CrewBase
class BloggerCrew:
	"""The Tech Blogger crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def blog_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['blog_researcher'],
			tools=[search]
		)

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config = self.agents_config['blog_writer'],
		)

	@task
	def research_blog_task(self) -> Task:
		return Task(
			config = self.tasks_config['research_blog_task'],
			agent = self.blog_researcher()
		)

	@task
	def write_blog_task(self) -> Task:
		return Task(
			config = self.tasks_config['write_blog_task'],
			agent = self.blog_writer()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Tech Blogger crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)