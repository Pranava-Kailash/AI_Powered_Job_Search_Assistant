# 🎉 AI-Powered Job Search Assistant

## 📚 Description
The AI-Powered Job Search Assistant is a tool designed to streamline the job search process by leveraging **LangChain**, **OpenAI**, and **Streamlit**. This application scrapes job listings from LinkedIn based on user-defined job roles and locations, retrieves detailed job profiles, and provides valuable insights to users, such as required skills, CV keywords, and role expectations.

## ✨ Features

- **🖥️ Interactive User Interface:** Built with Streamlit for user-friendly interactions.
- **🔍 Automated Job Scraping:** Fetches job listings from LinkedIn using custom scraping methods.
- **📄 Detailed Job Profiles:** Retrieves and displays comprehensive job details using the ProxyCurl API.
- **🤖 AI-Generated Insights:** Analyzes job descriptions to provide actionable insights using LangChain and OpenAI.
- **🔑 Environment Variable Management:** Uses `python-dotenv` to manage sensitive API keys securely.

## 💻 Technologies Used

- **Languages:** Python
- **Frameworks:** Streamlit, LangChain
- **APIs:** OpenAI, ProxyCurl, SerpAPI
- **Data Handling:** Python libraries for environment management, web requests, and data processing.

## 🚀 Installation

To set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-powered-job-search-assistant.git
   cd ai-powered-job-search-assistant
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
   - Activate it:
     - **Windows:** `venv\Scripts\activate`
     - **Mac/Linux:** `source venv/bin/activate`

3. **Install required packages from requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**  
   Create a `.env` file in the root directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   SERPAPI_KEY=your_serpapi_key
   PROXYCURL_API_KEY=your_proxycurl_api_key
   LANGSMITH_TRACING=true
   LANGSMITH_API_KEY=your_langsmith_api_key
   ```

## 🏁 Usage

To run the application, execute the following command in your terminal:
```bash
streamlit run app.py
```
Open your web browser and navigate to `http://localhost:8501/`.

### 🙌 How to Use

1. **📝 Enter Job Role:** Type the job title you are interested in (e.g., "Junior Data Engineer").
2. **📍 Enter Location:** Specify the preferred location for the job search (e.g., "UK").
3. Click on the **"Search Jobs"** button.
4. The application will scrape LinkedIn for relevant job listings and display detailed profiles with insights.

## 📊 Example Output

Upon entering the search details, the application will return results such as:

- **Job Title:** Junior Data Engineer
- **Company:** Information Tech Consultants
- **Location:** Central London
- **AI Summary for the Role:** Summary of the position, expected qualifications, etc. 
- **List of Required Skills:** 
  - Machine Learning
  - SQL Server
  - Data Analysis
  - Statistical Analysis
- **Keywords for CV:** Keywords to enhance your CV based on the job description.

## 📜 License

This project is licensed under the MIT License.
