from crewai import Task
from agents.career_consultant import CareerConsultant
from textwrap import dedent


class CareerConsultingTask():

    def setup(self, job_opp, candidate_name):
        return Task(
            description=dedent(f"""
            Advise and support a candidate in their career development and job
            search process. This task involves reviewing their CV, providing
            feedback, and conducting mock interviews. You will also offer
            guidance on job market trends and effective job search strategies.
            
            Your final deliverables should include personalized career plans,
            improved CVs, and a summary of interview tips and job search
            strategies.
            
            Candidate Name: {candidate_name}
            Desired Position: {job_opp}
            """),
            agent=CareerConsultant().setup()
        )
