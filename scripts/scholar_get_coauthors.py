#!/usr/bin/env python
"""
Use the scholarly module (https://pypi.org/project/scholarly/) to retrieve 
a list of co-authos based on publications from a certain time range.

Example usage (to get all co-authors of Steven A Cholewiak for articles
published between 2020 and 2021, but ignoring publications with more than 10 
co-authors, and including those without a publication year:
python3 scholar_get_coauthors.py 'Steven A Cholewiak' 2020 2021 -m 10 -i
"""
import argparse
from scholarly import scholarly

__author__ = 'Pim Bongaerts'
__copyright__ = 'Copyright (C) 2021 Pim Bongaerts'
__license__ = 'GPL'


def reformat_name(author_name):
    """ Reformat author name to Lastname, Firstname Initials """
    name_split = author_name.split()
    return '{0}, {1}'.format(name_split[len(name_split) - 1],
                             ' '.join(name_split[0:len(name_split) - 1]))

def get_all_coauthors(author_name, min_year, max_year, max_coauthors, 
                      include_no_year):
    """ Get a set of all coauthors """
    author = scholarly.fill(next(scholarly.search_author(author_name)))
    all_coauthors = set()
    for pub in author['publications']:
        # Evaluate if publication year is indicated (if not, ignore depending
        # on presence of --include_no_year flag)
        if 'pub_year' in pub['bib']:
            pub_year = int(pub['bib']['pub_year'])
        elif include_no_year:
            pub_year = max_year
        else:
            pub_year = min_year - 1

        # Evaluate whether publication falls within indicated timerange
        if min_year <= pub_year <= max_year:
            coauthors = scholarly.fill(pub)['bib']['author'].split(' and ')
            # Evaluate if number of coauthors meets optional threshold
            if len(coauthors) <= max_coauthors:
                [all_coauthors.add(reformat_name(coauthor)) for coauthor in coauthors]             
    return all_coauthors

def output_coauthor_list(all_coauthors):
    """ Output formatted list of co-authors - and prepend 'A:' for NSF COA """
    [print('A:\t{0}'.format(coauthor)) for coauthor in sorted(all_coauthors)]

def main(author_name, min_year, max_year, max_coauthors, include_no_year):
    # Get the set of coauthors from Google Scholar
    all_coauthors = get_all_coauthors(author_name, min_year, max_year, 
                                      max_coauthors, include_no_year)
    # Output formatted list of co-authors
    output_coauthor_list(all_coauthors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('author_name', metavar='author_name',
                        help='full name of author (e.g. `Steven A Cholewiak`)')
    parser.add_argument('min_year', metavar='min_year',
                        help='earliest year (e.g. 2016)')
    parser.add_argument('max_year', metavar='max_year',
                        help='latest year (e.g. 2021)')
    parser.add_argument('-m', '--max_coauthors', metavar='max_coauthors', 
                        default = 10e9,
                        help='maximum number of coauthors for a publication \
                              to be considered (optional; e.g. 30)')
    parser.add_argument('-i', '--include_no_year',
                        action = 'store_true',
                        help='include publications without a year (not \
                        included by default)')
    args = parser.parse_args()
    main(args.author_name, int(args.min_year), int(args.max_year), 
         int(args.max_coauthors), args.include_no_year)