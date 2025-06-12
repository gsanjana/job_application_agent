from langsmith.run_helpers import traceable
from langchain_openai import ChatOpenAI
import os
os.environ["LANGCHAIN_API_KEY"] = "your-langchain-api-key"
os.environ["LANGCHAIN_PROJECT"] = "interview-agent"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

llm = ChatOpenAI(
    openai_api_key="your-openapi-key",
    model="gpt-4o",
    temperature=0.3,
)

from langsmith.utils import tracing_is_enabled
print("📡 LangSmith Tracing Active?", tracing_is_enabled())

@traceable(name="Extract Interview Info")
def extract_interview_data(email_body):
    prompt = f"""
You are an AI helping extract interview details from emails. Parse this email and output JSON with:
- company
- role
- interview_stage (e.g., 'Phone Screen')
- interview_date
- interview_time
- calendar_link (if any)
- interviewer
Email content: {email_body}

Only output valid JSON. No commentary or extra text.

Email content:
\"\"\"
{email_body}
\"\"\"
"""
    response = llm.invoke(prompt).content
    return response

@traceable(name="Suggest Prep Resources")
def suggest_prep(company, role, stage):
    prompt = f"""
Suggest 2-3 prep resources (links or summaries) for someone preparing for a {stage} at {company} for a {role} role.
Output as a list.
"""
    return llm.invoke(prompt).content

@traceable(name="Follow-up Generator")
def follow_up_action(company, stage):
    prompt = f"""
Generate a short, professional follow-up or thank-you message after completing a {stage} with {company}.
"""
    return llm.invoke(prompt).content