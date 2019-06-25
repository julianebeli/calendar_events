import __init__
from api.requestor2 import API
import json
import csv


cache = 60*60*24*3
api = API('prod', cache=cache)

params = dict(methodname='list_calendar_events',
              type='event',
              all_events=True,
              context_codes=['course_3652'])

api.add_method(**params)
api.do()

# print(json.dumps(api.results, indent=4))

headers = ["id",
           "title",
           "start_at",
           "end_at",
           "created_at",
           "all_day",
           "location_address",
           "location_name",
           "context_code"]

with open('calendar_events_3652.csv', 'w') as f:
    writer = csv.DictWriter(f,
                            fieldnames=headers,
                            extrasaction='ignore',
                            lineterminator='\n')
    writer.writeheader()
    for row in api.results:
        writer.writerow(row)
