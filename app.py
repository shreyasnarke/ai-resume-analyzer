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

SYSTEM_PROMPT = """You are an expert HR consultant and resume reviewer with 15+ years of experience.
Analyze the given resume and provide:

1. **Overall Score** (out of 100)
2. **Strengths** (3-5 bullet points)
3. **Weaknesses** (3-5 bullet points)
4. **Missing Keywords** (for ATS optimization)
5. **Suggested Job Roles** (top 3 matching roles)
6. **Improvement Tips** (actionable advice)

Be specific, professional, and constructive. Format your response clearly with sections."""


def analyze_resume(resume_text: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\n--- RESUME ---\n{resume_text}\n--- END RESUME ---"
    return call_gemini(prompt)


def match_job(resume_text: str, job_description: str) -> str:
    prompt = f"""You are an expert recruiter. Compare this resume against the job description.

Provide:
1. **Match Score** (out of 100)
2. **Matching Skills** 
3. **Missing Skills/Requirements**
4. **Recommendation** (Should they apply? Why?)

--- RESUME ---
{resume_text}

--- JOB DESCRIPTION ---
{job_description}"""
    return call_gemini(prompt)


def improve_summary(resume_text: str) -> str:
    prompt = f"""Rewrite the professional summary section of this resume to make it more impactful, 
ATS-friendly, and compelling. Keep it under 4 sentences. Use strong action verbs.

Resume:
{resume_text}

Return ONLY the improved summary paragraph."""
    return call_gemini(prompt)


def main():
    print("=" * 60)
    print("       🤖 AI Resume Analyzer - Powered by Gemini LLM")
    print("=" * 60)

    print("\nOptions:")
    print("  1. Analyze Resume")
    print("  2. Match Resume to Job Description")
    print("  3. Improve Resume Summary")
    print("  4. Exit")

    while True:
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "4":
            print("Goodbye! 👋")
            break

        if choice in ["1", "2", "3"]:
            print("\nPaste your resume text (type END on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            resume_text = "\n".join(lines)

            if not resume_text.strip():
                print("❌ Resume text cannot be empty.")
                continue

            print("\n⏳ Analyzing with Gemini AI...\n")

            if choice == "1":
                result = analyze_resume(resume_text)
                print("📊 RESUME ANALYSIS RESULT")
                print("=" * 60)
                print(result)

            elif choice == "2":
                print("\nPaste the Job Description (type END on a new line when done):")
                jd_lines = []
                while True:
                    line = input()
                    if line.strip() == "END":
                        break
                    jd_lines.append(line)
                job_desc = "\n".join(jd_lines)
                result = match_job(resume_text, job_desc)
                print("🎯 JOB MATCH RESULT")
                print("=" * 60)
                print(result)

            elif choice == "3":
                result = improve_summary(resume_text)
                print("✨ IMPROVED SUMMARY")
                print("=" * 60)
                print(result)

        else:
            print("❌ Invalid choice. Enter 1-4.")


if __name__ == "__main__":
    main()
