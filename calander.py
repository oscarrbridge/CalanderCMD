import datetime


def show_items_in_calendar(service):

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # gets
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='nikniulp2ftvmqqdvthn3p7je0@group.calendar.google.com',
                                          timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    start_time = {}
    print(events)

    for event in events:
        start_time[len(start_time) + 1] = event['start']['dateTime']
        print(start_time)
        #  print(start_time[1][0]['dateTime'], event['summary'])


"""  # This will give the id's for calendars
calendar_list = service.calendarList().list().execute()
for calendar_list_entry in calendar_list['items']:
    print("calendar list", calendar_list_entry)
"""
