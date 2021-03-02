#!/usr/bin/env python
"""

"""
import argparse
from scholarly import scholarly

__author__ = 'Pim Bongaerts'
__copyright__ = 'Copyright (C) 2021 Pim Bongaerts'
__license__ = 'GPL'

def get_all_coauthors(author_name, min_year, max_year, max_coauthors):
    """ Get a set of all coauthors """
    search_query = scholarly.search_author(author_name)
    author = scholarly.fill(next(search_query))
    all_coauthors = set()
    for pub in author['publications']:
        if min_year <= int(pub ['bib']['pub_year']) <= max_year:
            pub_details = scholarly.fill(pub)
            coauthors = pub_details['bib']['author'].split(' and ')
            if len(coauthors) <= max_coauthors:
                for coauthor in coauthors:
                    name_split = coauthor.split()
                    all_coauthors.add('{0}, {1}'.format(name_split[len(name_split) - 1],
                                                        ' '.join(coauthor.split()[0:len(name_split) - 1])))
    return all_coauthors

def output_coauthor_list(all_coauthors):
    """ Output formatted list of co-authors """
    for coauthor in sorted(all_coauthors):
        print('A:\t{0}'.format(coauthor))

def main(author_name, min_year, max_year, max_coauthors):
    all_coauthors = get_all_coauthors(author_name, min_year, max_year, max_coauthors)
    output_coauthor_list(all_coauthors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('author_name', metavar='author_name',
                        help='full name of author (e.g. `Steven A Cholewiak`)')
    parser.add_argument('min_year', metavar='min_year',
                        help='earliest year (e.g. 2016)')
    parser.add_argument('max_year', metavar='max_year',
                        help='latest year (e.g. 2021)')
    parser.add_argument('-m', '--max_coauthors', metavar='max_coauthors', default = 10e9,
                        help='maximum number of coauthors for a publication \
                              to be considered (optional; e.g. 30)')
    args = parser.parse_args()
    main(args.author_name, int(args.min_year), int(args.max_year), int(args.max_coauthors))