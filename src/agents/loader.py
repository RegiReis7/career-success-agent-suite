from agents.career_consultant import CareerConsultant
from agents.cv_analyzer import CVAnalyzer
from agents.industry_expert import IndustryExpert
from crewai import Agent
from typing import List


class Agents:

    def load() -> List[Agent]:

        return [CareerConsultant.setup(), CVAnalyzer.setup(), IndustryExpert.setup()]
