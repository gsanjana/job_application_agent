# job_application_agent

# 🤖 Interview Agent

A smart AI assistant that helps parse interview-related emails, extracts critical details, schedules calendar events, suggests prep resources, and generates follow-up messages — all powered by LLMs and LangChain.

## 📂 Project Structure

├── main.py # Entry point for processing emails
├── interview_agent.py # Functions for LLM-powered extraction and suggestion
├── utils.py # Helper for calendar event creation
├── emails.json # Sample email input data
├── dashboard.py # Streamlit dashboard for UI
└── README.md

## 🚀 Setup Instructions
1. ###Create and Activate a Virtual Environment

python -m venv langsmith-env
source langsmith-env/bin/activate   # On Windows: langsmith-env\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Set Environment Variables

2. ###Set the following keys before running:

export LANGCHAIN_API_KEY=your_langchain_key
export LANGCHAIN_PROJECT=interview-agent
export OPENAI_API_KEY=your_openai_key
On Windows use set instead of export.

3. ###Run the Email Processor

python main.py
Run the UI Dashboard (Optional)
streamlit run dashboard.py

📧 Email Input Format
Make sure emails.json follows this structure:

[
  {
    "id": "1",
    "sender": "recruiter@example.com",
    "subject": "Interview Invitation",
    "body": "We'd like to interview you on June 15 at 2:00 PM...",
    "timestamp": "2025-06-10T10:12:00Z"
  }
]

📊 Features
✅ Extract interview details from raw emails

📅 Schedule calendar events

📚 Recommend prep resources

💌 Auto-generate professional follow-ups

🌐 LangSmith/LangChain tracing enabled

🖥️ Streamlit dashboard for visual summary

🛠️ Tech Stack
Python

OpenAI (via langchain)

LangSmith (for tracing)

Streamlit (for dashboard)

🧪 Example Run

📩 Processing email: Interview Invitation for Software Engineer - MLOps
🧠 Extracted Interview Info:
{
  "company": "AeroVect",
  "role": "Software Engineer - MLOps",
  "interview_stage": "Technical Interview",
  "interview_date": "June 15, 2025",
  "interview_time": "2:00 PM CST"
}
📅 Creating Calendar Event...
📚 Suggested Prep Resources:
- Link 1
- Link 2
💌 Follow-Up Suggestion:
Thank you message...
📎 License
MIT License © 2025 [Your Name]


### 📄 `README.txt` (Text editor–friendly version)
