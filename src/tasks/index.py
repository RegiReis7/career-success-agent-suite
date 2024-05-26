from career_consulting import CareerConsultingTask
from cv_analyzer import CVAnalyzerTask
from industry_requirements import IndustryReqTask
from streamlit.runtime.uploaded_file_manager import UploadedFile
from crewai import Task
from typing import List


class Tasks:

    def load(job_opp: str, candidate_name: str, requirements: str, cv: UploadedFile) -> List[Task]:
        return [CareerConsultingTask.setup(job_opp, candidate_name), CVAnalyzerTask.setup(job_opp, requirements, cv), IndustryReqTask.setup(job_opp)]
