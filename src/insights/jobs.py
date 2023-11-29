from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path: str) -> List[Dict]:
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = [row for row in csv_reader]
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()
        for job in self.jobs_list:
            if "job_type" in job:
                unique_job_types.add(job["job_type"])
        return unique_job_types

    def filter_by_multiple_criteria(self, jobs, filter_criteria):
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        filtered_jobs = []
        for job in jobs:
            if all(
                job.get(key) == value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)
        return filtered_jobs
