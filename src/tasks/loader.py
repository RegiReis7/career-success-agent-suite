from tasks.career_consulting import CareerConsultingTask
from tasks.cv_analyzer import CVAnalyzerTask
from tasks.industry_requirements import IndustryReqTask
from streamlit.runtime.uploaded_file_manager import UploadedFile
from crewai import Task
from typing import List


class Tasks:

    def load(job_opp: str, candidate_name: str, requirements: str, cv: UploadedFile) -> List[Task]:

        industry_requirements_task = IndustryReqTask.setup(job_opp=job_opp)

        cv_analyzer_task = CVAnalyzerTask.setup(
            job_opp=job_opp, requirements=requirements, cv=cv, contextTask=industry_requirements_task)

        return [industry_requirements_task, cv_analyzer_task,  CareerConsultingTask.setup(job_opp, candidate_name, [cv_analyzer_task, industry_requirements_task])]
