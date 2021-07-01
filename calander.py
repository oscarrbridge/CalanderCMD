from main import *
import datetime
import datetime
from googleapiclient.discovery import build
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def show_items_in_calendar(service):

    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='nikniulp2ftvmqqdvthn3p7je0@group.calendar.google.com',
                                          timeMin='Z',
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    for event in events:
        start_time = event['start'].get('dateTime', event['start'].get('date'))
        print(start_time, event['summary'])

        """  # This will give the id's for calendars
        calendar_list = service.calendarList().list().execute()
        for calendar_list_entry in calendar_list['items']:
            print("calendar list", calendar_list_entry)
        """
