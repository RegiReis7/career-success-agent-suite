from crewai import Task
from agents.cv_analyzer import CVAnalyzer
from agents.industry_expert import IndustryExpert
from textwrap import dedent
from custom_callback import writeTaskResult


class CVAnalyzerTask():

    def setup(self, job_opp, requirements):
        return Task(
            description=dedent(f"""
            Evaluate and review candidate CV to determine their suitability
            for a given role. This task involves examining the
            candidate educational background, work experience, skills, and
            achievements. You will need to identify both strengths and
            weaknesses, ensuring the best match for the job requirements.
            
            Your final report should include a detailed analysis of the CV,
            highlighting key qualifications, potential red flags, and a
            recommendation for further consideration.
            
            Job Title: {job_opp}
            Key Qualifications: {requirements}
            """),
            callback=writeTaskResult,
            context=[IndustryExpert.setup()],
            agent=CVAnalyzer.setup()
        )
