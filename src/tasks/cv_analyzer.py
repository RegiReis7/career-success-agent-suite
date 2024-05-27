from crewai import Task
from agents.cv_analyzer import CVAnalyzer
from agents.industry_expert import IndustryExpert
from textwrap import dedent
from tasks.custom_callback import writeTaskResult
from tools.search_documents import SeachDocument
from streamlit.runtime.uploaded_file_manager import UploadedFile


class CVAnalyzerTask():

    def setup(job_opp: str, requirements: str, cv: UploadedFile | None, contextTask: Task):

        search_documents_tool = SeachDocument(cv).search_document

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
            tools=[search_documents_tool],
            context=contextTask,
            agent=CVAnalyzer.setup()
        )
