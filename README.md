# Codeforces Contest Calendar Event Generator

Automatically sync upcoming Codeforces programming contests to your Google Calendar. Never miss a contest again!

## Overview

This project fetches upcoming Codeforces contests from the official API and automatically creates calendar events in your Google Calendar. It filters contests based on your preferences (e.g., within the next 7 days) and avoids duplicate entries.

## Features

-  **Automatic Contest Fetching**: Retrieves contest data from Codeforces API
-  **Google Calendar Integration**: Creates events directly in your Google Calendar
-  **Smart Filtering**: Configurable filters for contest timing (e.g., next 7 days)
-  **Duplicate Prevention**: Checks for existing events before adding new ones
-  **Event Details**: Each calendar event includes:
  - Contest name
  - Start and end times
  - Direct link to the contest
  - UTC timezone support

## Prerequisites

Before you get started, you'll need:

1. **Python 3.7+** installed on your system
2. **Google Account** with access to Google Calendar
3. **Google Cloud Project** with Calendar API enabled
4. **Service Account Credentials** for Google API authentication

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abhinaykumarreddybussa/Codeforces-contest-calendar-event-generator.git
   cd Codeforces-contest-calendar-event-generator
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

3. **Set up Google Cloud credentials**:
   - Create a Google Cloud Project
   - Enable the Google Calendar API
   - Create a Service Account
   - Download the service account credentials JSON file
   - Save it as `credentials.json` in the project root

## Configuration

1. **Update `sync_contests.py`** with your calendar ID:
   ```python
   CALENDAR_ID = 'your-email@gmail.com'  # Replace with your Google Calendar ID
   ```

2. **Adjust contest filtering** (optional):
   ```python
   # Modify the filter to change the time range
   if 0 < (start_time - now).days <= 7:  # Change 7 to your desired number of days
       upcoming_contests.append(contest)
   ```

## Usage

Run the script to sync contests:

```bash
python sync_contests.py
```

### Scheduling (Optional)

To run this automatically at regular intervals, you can use:

**On Linux/Mac** (using cron):
```bash
# Edit crontab
crontab -e

# Add this line to run every day at 9 AM
0 9 * * * cd /path/to/repo && python sync_contests.py
```

**On Windows** (using Task Scheduler):
1. Open Task Scheduler
2. Create a new task
3. Set trigger to your desired schedule
4. Set action to run: `python C:\path\to\sync_contests.py`

## How It Works

1. **Fetch Contests**: Retrieves all contests from Codeforces API (`/api/contest.list`)
2. **Filter Events**: Filters contests based on phase (`BEFORE`) and time range
3. **Authenticate**: Uses service account credentials to access Google Calendar API
4. **Check Duplicates**: Fetches existing events from the specified time range
5. **Create Events**: Adds new contest events to your calendar with all details
6. **Notify**: Prints confirmation of created events

## API Details

### Codeforces API
- **Endpoint**: `https://codeforces.com/api/contest.list`
- **No authentication required** for public contest data

### Google Calendar API
- **Scopes**: `https://www.googleapis.com/auth/calendar.events`
- **Service Account**: Used for secure, scheduled automation

## Example Output

```
Event already exists: Codeforces: Codeforces Round #XXX
Event created: https://calendar.google.com/calendar/u/0/r/eventedit/...
Event created: https://calendar.google.com/calendar/u/0/r/eventedit/...
```

## Troubleshooting

### Issue: "credentials.json not found"
- Ensure your service account credentials file is saved as `credentials.json` in the project root
- Verify the file path is correct

### Issue: "Calendar API not enabled"
- Log in to [Google Cloud Console](https://console.cloud.google.com/)
- Navigate to your project
- Enable the Google Calendar API

### Issue: "Invalid calendar ID"
- Use your full email address as the calendar ID
- Or find your calendar ID in Google Calendar settings

### Issue: "Permission denied" errors
- Verify your service account has access to the target calendar
- Share the calendar with your service account email address

## Security Notes

**Important**: Never commit `credentials.json` to version control
- Add `credentials.json` to `.gitignore`
- In production, use environment variables or secure credential management

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check existing GitHub issues
2. Create a new issue with detailed information
3. Include error messages and relevant code snippets

## Future Enhancements

- [ ] Add support for filtering by contest difficulty
- [ ] Add support for multiple calendars
- [ ] Implement web interface for configuration
- [ ] Add email notifications
- [ ] Support for other competitive programming platforms

---

**Happy coding and good luck with your Codeforces contests! 🚀**
