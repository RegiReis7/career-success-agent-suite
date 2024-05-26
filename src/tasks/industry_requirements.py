from crewai import Task
from agents.industry_expert import IndustryExpert
from textwrap import dedent
from custom_callback import writeTaskResult


class IndustryReqTask():

    def setup(self, job_opp):
        return Task(
            description=dedent(f"""
            Research and provide a comprehensive overview of the latest trends,
            challenges, and opportunities in the tech industry. This task
            involves analyzing market reports, industry news, and emerging
            technologies to offer strategic insights.

            Your final report should cover key industry developments, potential
            competitive threats, and opportunities for innovation and growth.

            Job Opportunity Role: {job_opp}
            """),
            callback=writeTaskResult,
            agent=IndustryExpert().setup()
        )
