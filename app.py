import os
import streamlit as st
from dotenv import load_dotenv
from google_results_scrap import JobSearcher
from linkedIn_Job_profile import JobProfileFetcher, simplify_linkedin_url
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGSMITH_TRACING')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_API_KEY')

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

output_parser = StrOutputParser()

st.set_page_config(page_title="Job Search Assistant", layout="wide")
st.title("AI-Powered Job Search Assistant")
st.write("""
Enter the job role and location, and this tool will scrape job listings from LinkedIn, 
analyze each job's description, and generate actionable insights for you!
""")

role = st.text_input("Job Role", placeholder="e.g., Junior Data Scientist")
location = st.text_input("Location", placeholder="e.g., uk")

def generate_insights(job_description: str) -> dict:

    prompt_template = ChatPromptTemplate.from_messages([
        { 'role': 'system', 'content': 'You are an expert AI Job Search Assistant. You have been asked to analyze a job description and provide insights.' },
        { 'role': 'user', 'content': f"""
            Extract insights from the following job description:
            
            {job_description}
            
            Provide:
            - A list of required skills
            - Keywords for CV
            - A summary of what the role expects
            - The level of experience required
            - Any other relevant insights
            """ }
    ])
    
    chain = prompt_template | llm | output_parser

    response = chain.invoke({"job_description": job_description})
    return response

if st.button("Search Jobs"):
    if not role or not location:
        st.error("Please provide both a job role and location.")
    else:
        with st.spinner("Searching for jobs..."):
            searcher = JobSearcher()
            query = f'site:linkedin.com/jobs inurl:"view" "{role}" "full-time"'
            job_links = searcher.fetch_job_links(query, location)
        
        if not job_links:
            st.error("No jobs found for the given role and location.")
        else:
            st.success(f"Found {len(job_links)} jobs!, Limiting to first job for testing.")
            
            job_links = job_links[:1] 

            fetcher = JobProfileFetcher()
            job_profiles = []

            for job_url in job_links:
                cleaned_url = simplify_linkedin_url(job_url)
                st.write(f"Fetching profile for: [{cleaned_url}]({cleaned_url})")
                profile = fetcher.fetch_job_profile(cleaned_url)
                
                if profile:
                    job_profiles.append(profile)

            for i, job in enumerate(job_profiles, 1):
                st.subheader(f"Job {i}: {job.get('title', 'N/A')}")
                st.write(f"**Company:** {job.get('company', {}).get('name', 'N/A')}")  

                st.write("**AI Summary for the Role:**")
                job_description = job.get('job_description', '')
                if job_description:
                    with st.spinner("Generating insights..."):
                        insights = generate_insights(job_description)
                        st.write(insights)
                else:
                    st.write("No job description available.")