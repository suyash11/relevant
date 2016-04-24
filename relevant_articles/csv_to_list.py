"""CSV to List module."""

import csv
import constants


def csv_parser(csv_file=None):
    """
    csv_parser method converts CSV file to a list.

    Modules used:
        csv

    Sample running method:
        >> csv_parser(csv_file='~/suyashshukla/Downloads/Sample.csv')
        returns [[], [], [], [], ....., []] with list values as the csv rows
        >> csv_parser()
        returns [[], [], [], [], ....., []] with list values as the csv rows
        with sample csv file from constants.py module
    """
    if not csv_file:
        csv_file = constants.csv_file
    file = open(csv_file, 'rt')
    row_list = list()
    try:
        file_reader = csv.reader(file)
        for row in file_reader:
            row_list.append(row)
    finally:
        file.close()
    return row_list
