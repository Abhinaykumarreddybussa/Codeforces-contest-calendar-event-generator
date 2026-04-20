import requests
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1. Fetch Codeforces Contests
response = requests.get('https://codeforces.com/api/contest.list')
data = response.json()

if data['status'] != 'OK':
    print("Failed to fetch contests")
    exit()

contests = data['result']
now = datetime.datetime.utcnow()

# 2. Filter contests (e.g., upcoming contests in the next 7 days)
upcoming_contests = []
for contest in contests:
    if contest['phase'] == 'BEFORE':
        start_time = datetime.datetime.utcfromtimestamp(contest['startTimeSeconds'])
        # Check if it falls within your specific range (e.g., next 7 days)
        if 0 < (start_time - now).days <= 7:
            upcoming_contests.append(contest)

# 3. Setup Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
# Load credentials from a secure location/environment variable in production
creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
service = build('calendar', 'v3', credentials=creds)

CALENDAR_ID = '22b0904@iitb.ac.in'

# 4. Add Events
for contest in upcoming_contests:
    start_time = datetime.datetime.utcfromtimestamp(contest['startTimeSeconds'])
    end_time = start_time + datetime.timedelta(seconds=contest['durationSeconds'])
    
    event = {
        'summary': f"Codeforces: {contest['name']}",
        'description': f"Link: https://codeforces.com/contests/{contest['id']}",
        'start': {
            'dateTime': start_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
    }
    
    # Check if event already exists (omitted for brevity) then insert
    event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"Event created: {event_result.get('htmlLink')}")
