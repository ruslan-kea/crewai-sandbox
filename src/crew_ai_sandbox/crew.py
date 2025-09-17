from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewAiSandbox():
    """Software Development Crew"""
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True
        )

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'],
            verbose=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_developer'],
            verbose=True
        )

    @agent
    def frontend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_developer'],
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'],
            verbose=True
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            verbose=True
        )

    @task
    def requirements_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['requirements_analysis'],
            agent=self.product_manager(),
            output_file='01_requirements_analysis.md'
        )

    @task
    def system_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['system_architecture'],
            agent=self.software_architect(),
            output_file='02_system_architecture.md'
        )

    @task
    def backend_implementation(self) -> Task:
        return Task(
            config=self.tasks_config['backend_implementation'],
            agent=self.backend_developer(),
            output_file='03_backend_implementation.md'
        )

    @task
    def frontend_implementation(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_implementation'],
            agent=self.frontend_developer(),
            output_file='04_frontend_implementation.md'
        )

    @task
    def quality_assurance(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assurance'],
            agent=self.qa_engineer(),
            output_file='05_quality_assurance.md'
        )

    @task
    def deployment_setup(self) -> Task:
        return Task(
            config=self.tasks_config['deployment_setup'],
            agent=self.devops_engineer(),
            output_file='06_deployment_setup.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Software Development crew"""
        return Crew(
            agents=[
                self.product_manager(),
                self.software_architect(),
                self.backend_developer(),
                self.frontend_developer(),
                self.qa_engineer(),
                self.devops_engineer()
            ],
            tasks=[
                self.requirements_analysis(),
                self.system_architecture(),
                self.backend_implementation(),
                self.frontend_implementation(),
                self.quality_assurance(),
                self.deployment_setup()
            ],
            process=Process.sequential,
            verbose=True
        )
