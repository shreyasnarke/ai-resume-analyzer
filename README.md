# 🤖 AI Resume Analyzer

> Analyze, score, and improve resumes using **Python + Google Gemini LLM** in minutes.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 Resume Score | Get an overall score out of 100 |
| 💪 Strengths & Weaknesses | Detailed analysis of your resume |
| 🔍 ATS Keywords | Missing keywords that hurt your chances |
| 🎯 Job Match | Compare resume vs job description |
| ✍️ Summary Rewriter | AI rewrites your summary to be powerful |
| 💼 Job Role Suggestions | Top matching roles for your profile |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API key
```bash
cp .env.example .env
# Edit .env and add your Gemini API key
# Get FREE key at: https://aistudio.google.com/app/apikey
```

### 4. Run the demo
```bash
python demo.py
```

### 5. Run interactive mode
```bash
python app.py
```

---

## 📸 Demo Output

```
🚀 AI RESUME ANALYZER — Powered by Google Gemini LLM

📊 RESUME ANALYSIS RESULT
============================================================
**Overall Score: 42/100**

**Strengths:**
• Has relevant technical skills listed
• Includes contact information
• Shows progression from intern to developer

**Weaknesses:**
• Summary is vague and lacks impact
• Job descriptions use weak, generic language
• No quantifiable achievements or metrics
• Missing key technologies for modern roles

**Missing ATS Keywords:**
Django, FastAPI, REST API, Docker, AWS, PostgreSQL,
Agile, CI/CD, Microservices, Unit Testing

**Suggested Job Roles:**
1. Junior Python Developer
2. Frontend Developer
3. Full Stack Developer (entry level)

**Improvement Tips:**
• Add numbers: "Reduced load time by 40%"
• Use strong verbs: Built, Developed, Optimized
• Add a projects section with GitHub links
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini 1.5 Flash** (Free LLM API)
- **python-dotenv** (environment management)

---

## 📁 Project Structure

```
ai-resume-analyzer/
├── app.py              # Interactive CLI app
├── demo.py             # Auto-demo with sample resume
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── README.md
```

---

## 🔑 Get Free API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with Google
3. Click **"Create API Key"**
4. Copy and paste into your `.env` file

**It's completely FREE** with generous rate limits!

---

## 🤝 Connect

Built with ❤️ using Python + AI

⭐ Star this repo if you found it useful!
# ai-resume-analyzer
