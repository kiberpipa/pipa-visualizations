#!/usr/bin/python
#! -*- encoding: utf-8 -*-

import json
import csv
import bisect
import copy

"""
File 
Pipeline:
Input: CSV file with startups, CSV file with person and where they work.
Output: JSON file suitable for d3 consumption. 
"""

STARTUPS_FILE = 'startups.csv'
PERSONS_FILE = 'persons.csv'
STARTUPS_PERSONS_JSON_FILE = 'startups.json'

startups = list()
persons = list()

nodes = list()
edges = list()

# Helper functions
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

def best_match(word, options):
    _bm_score = 100.
    _bm_match = ""
    for option in options:
        lev = float(levenshtein(word, option))
        rellev = lev/len(option)
        if rellev < _bm_score:
            _bm_score = rellev
            _bm_match = option
    return (_bm_score, _bm_match)

def normalize_company(company):
    return company.strip()

with open(PERSONS_FILE, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) < 2:
            continue
        for company in row[1].split(','):
            startups.append(normalize_company(company))

startups = sorted(set(startups))
# nodes = copy.deepcopy(startups)
nodes = [{'name': s, 'group': 1, 'weight': 0} for s in startups]

with open(PERSONS_FILE, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i, row in enumerate(csvreader):
        if len(row) != 2:
            continue
        handle, companies = row
        weight = 0

        for company in companies.split(','):
            weight += 1
            company = normalize_company(company)
            handle_index = len(nodes)

            try:
                company_index = index(startups, company)
                edges += [{
                    'source':handle_index,
                    'target':company_index,
                }]
                # nodes[company_index]['weight'] += 1

            except ValueError:
                print "Found a new startup: {company} with {handle} on row {row} (I won't autofix)".format(**{
                    'company': company,
                    'handle': handle,
                    'row': i+1
                })
                bs, bm = best_match(company, startups)
                print "    Best match: {company} with score {score}".format(**{
                    'company': bm,
                    'score': bs
                })
        nodes += [{'name': handle, 'group': 2, 'weight': weight}]


nodes_and_links = {
    'nodes': nodes,
    'links': edges
}

print nodes_and_links

json.dump(nodes_and_links, open(STARTUPS_PERSONS_JSON_FILE, "w"))
