def create_calendar_event(info):
    print("\n📅 Creating Calendar Event:")
    print(f"Title: {info.get('interview_stage', 'Interview')} - {info.get('company', 'Unknown Company')}")
    print(f"Date: {info.get('interview_date')} at {info.get('interview_time')}")
    print(f"With: {info.get('interviewer', 'N/A')}")