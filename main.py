import os

# Set environment variables
os.environ["LANGCHAIN_API_KEY"] = "your-langchain-key"
os.environ["LANGCHAIN_PROJECT"] = "interview-agent"
os.environ["OPENAI_API_KEY"] = "your-openapi-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

import streamlit as st
import re
import requests
import json
from interview_agent import extract_interview_data, suggest_prep, follow_up_action
from utils import create_calendar_event

def parse_json_like_string(text):
    # Remove Markdown formatting like ```json or ```
    text = text.strip().removeprefix("```json").removesuffix("```").strip()

    # Match key-value pairs like "key": value
    pattern = r'"(?P<key>[^"]+)"\s*:\s*(?P<value>null|"[^"]*")'

    result = {}
    for match in re.finditer(pattern, text):
        key = match.group("key")
        raw_value = match.group("value")

        # Convert "null" to None, or strip quotes from strings
        if raw_value == "null":
            value = None
        else:
            value = raw_value.strip('"')

        result[key] = value

    return result


if __name__ == "__main__":
    with open("/Users/sanjanagombi/langsmith/emails.json") as f:
        email_data_list = json.load(f)

    for email in email_data_list:
        print("\n📩 Processing email:", email["subject"])
        email_body = email["body"]

        try:
 
            info_json = extract_interview_data(email["subject"]+email["body"])
            interview_info = parse_json_like_string(info_json)

            print("🧠 Extracted Interview Info:")
            print(interview_info)

            create_calendar_event(interview_info)

            print("\n📚 Suggested Prep Resources:")
            print(suggest_prep(
                interview_info['company'],
                interview_info['role'],
                interview_info['interview_stage']
            ))

            print("\n💌 Follow-Up Suggestion:")
            print(follow_up_action(
                interview_info['company'],
                interview_info['interview_stage']
            ))

        except Exception as e:
            print("⚠️ Could not process email:", e)

