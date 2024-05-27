from crewai import Task
from tasks.custom_callback import writeTaskResult
from agents.career_consultant import CareerConsultant
from textwrap import dedent
from typing import List

class CareerConsultingTask():

    def setup(job_opp: str, candidate_name: str, contextTasks: List[Task]):
        
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
            expected_output=f"""A full report with the best advices to get the job opp ({
                job_opp})""",
            context=contextTasks,
            output_file=f'{"-".join(job_opp.split())}-task-output.md',
            agent=CareerConsultant.setup(),
            callback=writeTaskResult
        )
