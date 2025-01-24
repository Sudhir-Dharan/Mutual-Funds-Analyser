from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
# Instantiate the MF search tool


@CrewBase
class MFAnalyserCrew():
    """MF Analyzer crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
						verbose=True
        )
    
    @agent
    def financial_data_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_data_gatherer'],
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            allow_delegation=False,
                        verbose=True
        )

    @agent
    def investment_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['investment_advisor'],
            tools=[],
            allow_delegation=False,
						verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.financial_researcher()
        )
    
    @task
    def data_gatherer_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_gatherer_task'],
            agent=self.financial_data_gatherer(),
            context=[self.research_task()]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            agent=self.financial_analyst(),
            context=[self.research_task(), self.data_gatherer_task()]
        )

    @task
    def advisor_task(self) -> Task:
        return Task(
            config=self.tasks_config['advisor_task'],
            agent=self.investment_advisor(),
            context=[self.analysis_task(), self.data_gatherer_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the mf investment advisor crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
