import datetime

# hour, minute, day, month, year

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
    # print(events)

    for event in events:
        start_time[len(start_time) + 1] = [event['start']['dateTime'], event['summary']]
        #  print(start_time[1][0]['dateTime'], event['summary'])

    for entry in start_time:
        dates = []
        # print(start_time[entry])
        for number in start_time[entry][0]:
            # print(number, number.isdigit())
            # print(start_time[entry][0])
            if number.isdigit() is True:
                dates.append(number)

        dates_int = "".join(dates)  # change this to int()
        start_time[entry][0] = dates_int
        # print(start_time[entry][0])

    # print(start_time)
    for entry in start_time:
        year = []
        month = []
        day = []
        hour = []
        minute = []
        for i in range(0, 4):
            year.append(start_time[entry][0][i])
            if len(year) == 4:
                year = int("".join(year))

        for i in range(4, 6):
            month.append(start_time[entry][0][i])
            if len(month) == 2:
                month = int("".join(month))

        for i in range(6, 8):
            day.append(start_time[entry][0][i])
            if len(day) == 2:
                day = int("".join(day))

        for i in range(8, 10):
            hour.append(start_time[entry][0][i])
            if len(hour) == 2:
                hour = int("".join(hour))

        for i in range(10, 12):
            minute.append(start_time[entry][0][i])
            if len(minute) == 2:
                minute = int("".join(minute))

        start_time[entry][0] = [hour, minute, day, month, year]

    return start_time

    # print(start_time[entry][0][3])


def check_before_school(events):
    for item in events:
        print(events[item][0][0])
        print(events[item][0][1])
        if events[item][0][0] <= 8 and events[item][0][1] <= 50:
            print("you can go to anna's")
        else:
            print("you cant go to anna's")


"""
    for entry in start_time:
        for number in start_time[entry][0]:
            start_time[entry]["year"] = number[:4]
            print(start_time[entry]["year"])
"""


"""  # This will give the id's for calendars
calendar_list = service.calendarList().list().execute()
for calendar_list_entry in calendar_list['items']:
    print("calendar list", calendar_list_entry)
"""
