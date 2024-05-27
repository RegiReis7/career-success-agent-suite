from crewai import Task
from agents.industry_expert import IndustryExpert
from textwrap import dedent
from tasks.custom_callback import writeTaskResult
from crewai_tools import EXASearchTool


class IndustryReqTask():

    def setup(job_opp):

        exa_tool = EXASearchTool()

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
            expected_output=f"""A full report with the best advices to get the job opp of ({
                job_opp})""",
            tools=[exa_tool],
            callback=writeTaskResult,
            agent=IndustryExpert.setup()
        )
