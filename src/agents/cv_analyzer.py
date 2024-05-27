from crewai import Agent


class CVAnalyzer:

    def setup():
        return Agent(
            role="CV Analyzer",
            goal="Evaluate and identify the strengths and weaknesses of candidate CVs",
            backstory="As a CV Analyzer, your task is to meticulously review CVs, highlighting key skills, experiences, and gaps to assist in selecting the best candidates for the job.",
            verbose=True,
            allow_delegation=False
        )
