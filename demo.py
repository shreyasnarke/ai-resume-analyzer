import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def call_gemini(prompt, retries=3, wait=15):
    for attempt in range(retries):
        try:
            return model.generate_content(prompt).text
        except Exception as e:
            err = str(e)
            if "429" in err or "RESOURCE_EXHAUSTED" in err:
                if attempt < retries - 1:
                    print(f"⚠️  Rate limit hit. Waiting {wait}s before retry ({attempt+1}/{retries})...")
                    time.sleep(wait)
                else:
                    return "❌ Quota exceeded. Get a new API key at: https://aistudio.google.com/app/apikey"
            else:
                return f"❌ Error: {err}"
    return "❌ Failed after retries."

SAMPLE_RESUME = """
Shreyas Narke
Email: shreyassandeepnarke@gmail.com | Phone: 9767710596
Github: github.com/shreyasnarke | LinkedIn: linkedin.com/in/Shreyas Narke | Portfolio: shreyasprofile

EXPERIENCE

PRAISE ARRAY PVT.LTD. | Software Developer
01 Oct 2024 - Present
- Built responsive web applications using React.js, HTML and CSS for an interactive user experience.
- Developed and integrated RESTful APIs using Express.js to connect frontend with backend services.
- Used JavaScript (ES6+) to write clean, efficient, and reusable code.
- Worked with state management (React Hooks, Context API) to handle data flow efficiently.
- Collaborated with the team to debug issues, optimize performance, and improve UI/UX and also knowledge in Unit testing.

INNOVATIVE TECHHUB PVT.LTD. | Technical Support Engineer L1
02 Feb 2024 - 10 Sept 2024
- Provided first-level technical support, troubleshooting hardware, software, and network-related issues for clients.
- Diagnosed and resolved customer inquiries through ticketing systems, emails, and calls, ensuring prompt and efficient solutions.
- Collaborated with cross-functional teams to escalate complex issues and improve support processes.
- Assisted in system updates, installations, and configurations to optimize performance.
- Delivered excellent customer service, ensuring high levels of client satisfaction and retention.

PROJECTS

DIGITAL MARKETING ANALYTICS
- Analyzed digital marketing campaign performance using SQL and Python to extract and clean data from multiple sources.
- Used Excel for data preprocessing, trend analysis, and KPI tracking.
- Applied Python (Pandas, Matplotlib, Seaborn) for data analysis.
- Built interactive Power BI dashboards to visualize key metrics like website traffic, conversion rates, and customer engagement.
- Provided data-driven recommendations to optimize marketing strategies and improve ROI.

MOVIES SEARCH ENGINE | Class Project for Distributed React Programming
- Fetches movie data using API calls, displaying details like title, ratings, release date, and more.
- Uses React's component-based architecture for a seamless, responsive, and dynamic user experience.

EDUCATION

MASTER OF SCIENCE IN COMPUTER APPLICATIONS (MSC CA)
Haribhai V. Desai College | 2022 - 2024 | SPPU, Pune, India
Percentage: 79.70% | CGPA: 8.70 | Grade: A+

BACHELOR OF COMPUTER APPLICATIONS (BCA)
Haribhai V. Desai College | 2019 - 2022 | SPPU, Pune, India
Percentage: 81.20% | CGPA: 8.76 | Grade: A+

SKILLS

PROGRAMMING
Python (Pandas, NumPy, Matplotlib, Seaborn), React.js, JavaScript (ES6+), Express.js, Node.js,
RESTful APIs, Object-Oriented Programming, Excel, SQL, GraphQL, Cypress Unit Test, Power BI, FastAPI

TECHNOLOGY PLATFORMS
Git/GitHub, Linux, Windows OS, Troubleshooting, Data Visualization, Web Scraping, API Development,
Spyder, Jupyter Notebook, MySQL Workbench, Google Colab, VS Code, Postman
"""

SAMPLE_JOB = """
Senior Python Developer - TechCorp Inc.

Requirements:
- 3+ years Python development experience
- Strong knowledge of Django/FastAPI
- Experience with AWS, Docker, Kubernetes
- REST API design and development
- PostgreSQL / MongoDB experience
- CI/CD pipelines (GitHub Actions)
- Strong problem-solving skills
- Team collaboration experience
"""


def print_section(title: str, emoji: str = ""):
    print(f"\n{emoji} {title}")
    print("=" * 60)


def run_demo():
    print("\n" + "🚀 " * 20)
    print("     AI RESUME ANALYZER — Powered by Google Gemini LLM")
    print("🚀 " * 20)

    print("\n📄 SAMPLE RESUME INPUT:")
    print("-" * 60)
    print(SAMPLE_RESUME)

    # --- Demo 1: Full Resume Analysis ---
    print_section("DEMO 1: Full Resume Analysis", "📊")
    print("⏳ Sending to Gemini AI...")

    prompt1 = f"""You are an expert HR consultant. Analyze this resume and provide:
1. **Overall Score** (out of 100)
2. **Top 3 Strengths**
3. **Top 3 Weaknesses**
4. **Missing ATS Keywords**
5. **Best Matching Job Roles**
6. **Top 3 Improvement Tips**

Resume:
{SAMPLE_RESUME}"""

    response1 = call_gemini(prompt1)
    print(response1)

    # --- Demo 2: Job Match ---
    print_section("DEMO 2: Job Description Match Score", "🎯")
    print("⏳ Matching resume against job description...")
    time.sleep(5)

    prompt2 = f"""Compare this resume to the job description. Give:
1. **Match Score** (out of 100)
2. **Matched Skills**
3. **Missing Requirements**
4. **Final Recommendation**

Resume: {SAMPLE_RESUME}
Job Description: {SAMPLE_JOB}"""

    response2 = call_gemini(prompt2)
    print(response2)

    # --- Demo 3: Rewrite Summary ---
    print_section("DEMO 3: AI-Rewritten Professional Summary", "✨")
    print("⏳ Rewriting summary with AI...")
    time.sleep(5)

    prompt3 = f"""Rewrite this resume's summary to be powerful, ATS-optimized, and professional.
Max 4 sentences. Use strong action verbs. Make it impressive.

Resume:
{SAMPLE_RESUME}

Return ONLY the new summary."""

    response3 = call_gemini(prompt3)
    print(response3)

    print("\n" + "=" * 60)
    print("✅ Demo Complete! Built with Python + Google Gemini LLM")
    print("⭐ Star the repo | 🔗 Connect on LinkedIn")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
