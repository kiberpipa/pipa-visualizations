#!/usr/bin/python
#! -*- encoding: utf-8 -*-

import csv
import operator
import datetime
import itertools
import json

EVENTS_FILE = "../data/events.csv"
PROJECTS_FILE = "../data/projects.csv"
EVENTS_JSON_FILE = "events.json"

projects = list()

# Helper functions
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

# http://stackoverflow.com/a/15823348
def json_datetime_default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )
    return millis

with open(PROJECTS_FILE, 'r') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		projects += [row]

projects = sorted(projects, key=operator.itemgetter(0))

# 2013-10-28 18:00:00+01
# format: %Y-%m-%d %H:00:00+%z
events = list()
with open(EVENTS_FILE, 'r') as csvfile:
	reader = csv.reader(csvfile)
	for iid, title, visitors, startdate, program_id in reader:
		events += [[iid, title, visitors, datetime.datetime.strptime(startdate[:-9], "%Y-%m-%d %H"), program_id]]

events = sorted(events, key=operator.itemgetter(3))

start_begin = (events[0][3], events[-1][3])

data_bined = list()

def grouper( item ): 
    return item[3].year, item[3].month

for ((year, month), items) in itertools.groupby(events, grouper):
	data_bined += [[year, month, sorted(list(items), key=operator.itemgetter(4))]]

json.dump(data_bined, open(EVENTS_JSON_FILE, "w"), default=json_datetime_default)
