#!/usr/bin/env python
"""
Use the scholarly module (https://pypi.org/project/scholarly/) to retrieve 
all publications from someone's Google Scholar's profile and output as JSON.

Example usage (to get all publications of Steven A Cholewiak)
python3 scholar_get_pubs.py 'Steven A Cholewiak'
"""
import argparse
import json
from scholarly import scholarly

__author__ = 'Pim Bongaerts'
__copyright__ = 'Copyright (C) 2021 Pim Bongaerts'
__license__ = 'GPL'


def reformat_name(author_name):
    """ Reformat author name to Lastname, Firstname Initials """
    name_split = author_name.split()
    last_name = name_split[len(name_split) - 1]
    first_names = name_split[0:len(name_split) - 1]
    if len(first_names) == 1 and first_names[0].upper() == first_names[0]:
        initials = first_names[0]
    elif len(first_names) > 1 and first_names[1].upper() == first_names[1]:
        initials = '{0}{1}'.format(first_names[0][0],
                                   ''.join(name.upper() for name in first_names[1:]))
    else:
        initials = ''.join(name[0].upper() for name in first_names)
    if initials[len(initials)-3:] == 'VAN':
        return '{0} van {1}'.format(last_name, initials[0:len(initials) - 3])
    else:
        return '{0} {1}'.format(last_name, initials)

def reformat_coauthors(coauthors):
    """ Reformat coauthors """
    return ', '.join([reformat_name(author_name) for author_name in coauthors])

def output_json(data):
    """ Output as JSON to STDOUT """
    print(json.dumps(data, indent=4))

def output_markdown(data):
    """ Output as Markdown to STDOUT """
    for publication in data['publications']:
        print('{0} ({1}) {2}. *{3}* {4}: {5}.'.format(publication['authors'],
                                                      publication['year'],
                                                      publication['title'],
                                                      publication['journal'],
                                                      publication['volume'],
                                                      publication['pages']))

def main(author_name):
    """ Print all publications as JSON to STDOUT """
    data = {}
    data['publications'] = []

    author = scholarly.fill(next(scholarly.search_author(author_name)))
    for pub in author['publications']:
        pub_details = scholarly.fill(pub)['bib']
        data['publications'].append({
            'authors': reformat_coauthors(pub_details['author'].split(' and ')),
            'year': pub_details.get('pub_year', ''),
            'title': pub_details.get('title', ''),
            'journal': pub_details.get('journal', ''),
            'volume': pub_details.get('volume', ''),
            'issue': pub_details.get('issue', ''),
            'pages': pub_details.get('pages', ''),
            'citations': pub.get('num_citations', 0),
            'pub_url': pub.get('pub_url', ''),
             #'eprint_url': pub.get('pub_url', '') # seems to be same as pub_url
        })

    output_markdown(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('author_name', metavar='author_name',
                        help='full name of author (e.g. `Steven A Cholewiak`)')
    args = parser.parse_args()
    main(args.author_name)