#!/usr/bin/env python
"""
Reformat bibtex to format used for Mesophotic.org upload sheet
"""
import argparse
import bibtexparser

__author__ = 'Pim Bongaerts'
__copyright__ = 'Copyright (C) 2023 Pim Bongaerts'
__license__ = 'GPL'

def reformat_name(author_name):
    """ Reformat author name to Lastname, Firstname Initials """
    if not author_name:
        return ''
    name_split = author_name.replace('{', '').replace('}', '').replace('.', ' ').split()
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
        #print(author_name, '->', '{0} van {1}'.format(last_name, initials[0:len(initials) - 3]))
        return '{0} van {1}'.format(last_name, initials[0:len(initials) - 3])
    else:
        #print(author_name, '->', '{0} {1}'.format(last_name, initials))
        return '{0} {1}'.format(last_name, initials)    

def reformat_authors(authors):
    """ Reformat coauthors """
    authors_list = authors.split(' and ')
    if authors_list:
        return ', '.join([reformat_name(author_name) for author_name in authors_list])
    else:
        return ''

def reformat_doi(doi):
    """ Reformat doi """
    return doi.replace('https://doi.org/', '')

def reformat_abstract(abstract):
    """ Reformat abstract """
    return abstract.replace('\t', '').replace('\n', '')

def format_as_mesophotic_csv(publication):

    formatted_output = '\t'.join(['FALSE', '', '', '', '', '',  # Status, Date added, PubID, Upload, Metadata, Val#1, Val#2
                                publication.get('title', ''), 
                                reformat_authors(publication.get('author', '')),
                                publication.get('year', ''), 
                                reformat_abstract(publication.get('abstract', '')),
                                publication.get('journal', ''),
                                reformat_doi(publication.get('doi', '')),
                                publication.get('volume', ''),
                                publication.get('issue', ''),
                                publication.get('pages', ''),
                                publication.get('url', ''),
                                ''])         # Notes, Date added, PubID
    return formatted_output

def main(filename):
    with open(filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for publication in bib_database.entries:
        print(format_as_mesophotic_csv(publication))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', metavar='filename',
                        help='bibtex filename')
    args = parser.parse_args()
    main(args.filename)