import os
import json
from typing import List, Dict, Optional
from datetime import datetime
import requests
from dotenv import load_dotenv
from google_results_scrap import JobSearcher, simplify_linkedin_url

load_dotenv()

class JobProfileFetcher:
    def __init__(self):
        self.api_key = self._get_env_var('PROXYCURL_API_KEY')
        
    def _get_env_var(self, var_name: str) -> str:
        value = os.getenv(var_name)
        if not value:
            raise ValueError(f"{var_name} not found in environment variables")
        return value

    def fetch_job_profile(self, job_url: str) -> Optional[Dict]:
        print(f"Fetching job profile for: {job_url}")
        
        api_endpoint = "https://nubela.co/proxycurl/api/linkedin/job"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"url": job_url}

        try:
            response = requests.get(api_endpoint, headers=headers, params=params
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Full response content: {response.text}")
            return None
        except Exception as e:
            print(f"Error fetching job profile: {str(e)}")
            return None

    def save_to_json(self, data: List[Dict], filename: str = None) -> str:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"job_data_{timestamp}.json"
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {filename}")
            return filename
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            return ""

def main():
    try:
        searcher = JobSearcher()
        
        search_query = 'site:linkedin.com/jobs inurl:"view" "Junior Data Scientist" "full-time"'
        location = "uk"
        
        print(f"\nFetching job links for '{search_query}' in {location.upper()}")
        job_links = searcher.fetch_job_links(search_query, location)
        
        if job_links:
            print(f"\nFound {len(job_links)} job links")

]            fetcher = JobProfileFetcher()
            
            job_links = job_links[:2]
            
            job_profiles = []
            for link in job_links:
                clean_url = simplify_linkedin_url(link)
                print(f"\nProcessing URL: {clean_url}")
                
                profile = fetcher.fetch_job_profile(clean_url)
                if profile:
                    profile['source_url'] = clean_url
                    job_profiles.append(profile)
                else:
                    print(f"Failed to fetch profile for: {clean_url}")
            
            if job_profiles:
                filename = fetcher.save_to_json(job_profiles)
                
                print("\nJob Profiles Summary:")
                for i, job in enumerate(job_profiles, 1):
                    print(f"\nJob {i}:")
                    print(f"Title: {job.get('title', 'N/A')}")
                    print(f"Company: {job.get('company', {}).get('name', 'N/A')}")
                    print(f"Location: {job.get('location', 'N/A')}")
                    print(f"URL: {job['source_url']}")
            else:
                print("No job profiles were successfully fetched")

        else:
            print("No job links found")
            
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
