from crewai import Agent, Crew, Process, Task, LLM, TaskOutput
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
import os

llm = LLM(model="gpt-4o-mini", temperature=0)


def save_output(output: TaskOutput):
    file_path = f"outputs/{output.agent.lower().replace(' ', '_')}.md"
    os.makedirs("outputs", exist_ok=True)
    with open(file_path, "w") as f:
        f.write(output.raw)

@CrewBase
class PresalesCrew():
    """PresalesCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    pdf_source = PDFKnowledgeSource(
            file_paths=["../knowledge/Client Brief_ Performance and Progression Review Software Solution.pdf"] # Update this path to your actual PDF
        )

    @agent
    def brief_interpreter(self) -> Agent:
        return Agent(
            config=self.agents_config['brief_interpreter'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.pdf_source]
        )
    
    @agent
    def user_persona_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['user_persona_creator'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.pdf_source],
        )
    
    @agent
    def gap_identifier(self) -> Agent:
        return Agent(
            config=self.agents_config['gap_identifier'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.pdf_source],
        )
    
    @agent
    def epic_story_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['epic_story_generator'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[self.pdf_source],
        )
    
    @agent
    def slide_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['slide_creator'], # type: ignore[index]
            verbose=True,
        )

    @agent
    def user_journey_mapper(self) -> Agent:
        return Agent(
            config=self.agents_config['user_journey_mapper'], # type: ignore[index]
            verbose=True,
        )

    @task
    def brief_interpretation_task(self) -> Task:
        return Task(
            config=self.tasks_config['brief_interpretation_task'], # type: ignore[index]
            callback=save_output
        )

    @task
    def user_persona_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_persona_generation_task'], # type: ignore[index]
            callback=save_output
        )

    @task
    def gap_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['gap_analysis_task'], # type: ignore[index]
            callback=save_output
        )
    
    @task
    def epic_story_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['epic_story_generation_task'], # type: ignore[index]
            callback=save_output
        )
    
    @task
    def user_journey_mapping_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_journey_mapping_task'], # type: ignore[index]
            callback=save_output
        )
    
    @task
    def slide_deck_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['slide_deck_generation_task'], # type: ignore[index]
            callback=save_output
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the PresalesCrew crew"""
    
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[self.pdf_source],
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
