


grouped = {}
for event in list_of_events:
    weeknumber = event['date'].isocalendar()[1]
    grouped.setdefault(weeknumber, []).append(event)
