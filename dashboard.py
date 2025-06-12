import streamlit as st
import json
from interview_agent import extract_interview_data, suggest_prep, follow_up_action
from utils import create_calendar_event
from main import parse_json_like_string

with open("/Users/sanjanagombi/langsmith/emails.json") as f:
    email_data_list = json.load(f)

st.title("📬 Interview Email Processor")

for email in email_data_list:
    with st.expander(f"📩 {email['subject']}"):
        st.markdown(f"**Sender:** {email['sender']}")
        st.markdown(f"**Timestamp:** {email['timestamp']}")
        st.code(email["body"], language="text")

        try:
            info_json = extract_interview_data(email["subject"] + email["body"])
            interview_info = parse_json_like_string(info_json)

            st.subheader("🧠 Extracted Info")
            st.json(interview_info)

            st.subheader("📚 Prep Suggestions")
            st.markdown(suggest_prep(
                interview_info.get('company', ''),
                interview_info.get('role', ''),
                interview_info.get('interview_stage', '')
            ))

            st.subheader("💌 Follow-Up Message")
            st.markdown(follow_up_action(
                interview_info.get('company', ''),
                interview_info.get('interview_stage', '')
            ))

        except Exception as e:
            st.error(f"❌ Error processing email: {e}")
