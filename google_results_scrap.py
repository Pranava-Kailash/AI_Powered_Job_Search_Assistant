import re
from serpapi import GoogleSearch
from urllib.parse import urlparse, urlunparse
from dotenv import load_dotenv
import os

load_dotenv()

def simplify_linkedin_url(job_url: str) -> str:
    try:
        job_id_match = re.search(r'view/(?:.*?-)?(\d+)', job_url)
        if job_id_match:
            job_id = job_id_match.group(1)
            return f"https://www.linkedin.com/jobs/view/{job_id}"
        return job_url
    except Exception as e:
        print(f"Error processing URL {job_url}: {str(e)}")
        return job_url

class JobSearcher:
    def __init__(self):
        self.api_key = self._get_env_var('SERPAPI_KEY')
        
    def _get_env_var(self, var_name: str) -> str:
        value = os.getenv(var_name)
        if not value:
            raise ValueError(f"{var_name} not found in environment variables")
        return value

    def fetch_job_links(self, query: str, location: str = "uk") -> list:
        print(f"Fetching job links for: {query} in {location.upper()}")

        params = {
            "engine": "google",
            "q": query,
            "hl": "en",
            "gl": location,
            "api_key": self.api_key
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            
            raw_job_links = [
                result.get("link")
                for result in results.get("organic_results", [])
                if result.get("link") and "linkedin.com/jobs/view" in result.get("link")
            ]
            
            job_links = []
            for link in raw_job_links:
                simplified_url = simplify_linkedin_url(link)
                job_links.append(simplified_url)
            
            print(f"Found {len(job_links)} job links")
            return job_links
            
        except Exception as e:
            print(f"Error fetching job links: {str(e)}")
            return []

if __name__ == "__main__":
    searcher = JobSearcher()
    query = 'site:linkedin.com/jobs inurl:"view" "Data Scientist" "full-time"'
    links = searcher.fetch_job_links(query)
    print("\nFinal Results:")
    for link in links:
        print(link)
