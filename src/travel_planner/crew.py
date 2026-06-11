import os

from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

llm=LLM(model="groq/llama-3.3-70b-versatile",temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY"))





@CrewBase
class TravelPlanner():
    """TravelPlanner crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def local_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['local_expert'], # type: ignore[index]
            tools=[SerperDevTool()],
            llm=llm,
            verbose=True
        )

    @agent
    def logistics_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['logistics_specialist'], # type: ignore[index]
            tools=[SerperDevTool()],
            llm=llm,
            verbose=True
        )
    
    @agent
    def itinerary_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_optimizer'], # type: ignore[index]
            tools=[],
            llm=llm,
            verbose=True
        )

    @task
    def local_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def logistics_task(self) -> Task:
        return Task(
            config=self.tasks_config['logistics_task'], # type: ignore[index]
        )

    @task
    def itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlanner crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            chat_llm=llm
        )
