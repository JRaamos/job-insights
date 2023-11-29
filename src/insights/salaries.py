from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = self.extract_salaries_from_jobs()
        max_salary = max(salaries) if salaries else 0
        return max_salary

    def extract_salaries_from_jobs(self) -> List[int]:
        salaries = []
        for job in self.jobs_list:
            salary_str = job.get("max_salary")
            if salary_str:
                try:
                    salary = int(salary_str)
                    salaries.append(salary)
                except ValueError:
                    continue
        return salaries

    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
