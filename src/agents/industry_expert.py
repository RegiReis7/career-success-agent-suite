from crewai import Agent


class IndustryExpert():
    
    def setup(self):
        return Agent(
            role="Tech Industry Expert",
            goal="Provide insights on current technological advancements and industry dynamics",
            backstory="As a Tech Industry Expert, your expertise in the tech sector will help identify emerging trends, competitive landscapes, and strategic opportunities to inform decision-making processes.",
            verbose=True
        )