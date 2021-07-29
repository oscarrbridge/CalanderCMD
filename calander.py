import datetime
from secret import *

# hour, minute, day, month, year
# This is the list format that the date is stored in

NUMBER_OF_RESULTS = 30  # Specifies the number of events to return to the program


def show_items_in_calendar(service):
    """
    Get specified number of items and make the format easier to read.
    """

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print(f'Getting the upcoming {NUMBER_OF_RESULTS} events')
    events_result = service.events().list(calendarId=calender_id,
                                          timeMin=now,
                                          maxResults=NUMBER_OF_RESULTS, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    start_time = {}

    for event in events:
        try:
            start_time[len(start_time) + 1] = [event['start']['dateTime'], event['summary']]
        except KeyError:
            pass

    for entry in start_time:
        dates = []
        for number in start_time[entry][0]:
            if number.isdigit() is True:
                dates.append(number)

        dates_int = "".join(dates)
        start_time[entry][0] = dates_int

    # print(start_time)
    for entry in start_time:
        """
        Convert given time format to one that is easier to read.
        """
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


def check_before_school(events):
    for item in events:
        # print(events[item][0][0]) This will show you the dates / times
        # print(events[item][0][1]) This will show you the summary of the event
        if events[item][1] == "Thing to look for":
            # This is the event name the program will look for ^^^
            print(f"The thing is happening on the {events[item][0][2]}th")
            # This is the response the program will give if the event is found ^^^
