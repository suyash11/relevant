#!/usr/bin/python
"""Main class file, used to aggreagate all modules."""

import argparse
import csv_to_list
import cosine_similarity
import constants
import object_dict

__author__ = 'Suyash Shukla'


def get_args():
    """The function parses and return arguments passed."""
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description="""Script retrieves receives the csv file and
                       outputs the relevant news articles""")
    # Add arguments
    parser.add_argument(
        '-c', '--csv_file',
        help='CSV file path as a string', required=False,
        nargs='?', default=constants.csv_file,
        type=str)
    parser.add_argument(
        '-s', '--input_string', type=str,
        help='Input string for which relevant news to be searched',
        required=False, default=constants.input_string)
    parser.add_argument(
        '-n', '--number_of_results', type=int,
        help='Number of search results to be found', required=False,
        default=constants.number_of_results)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Return all variable values
    return args.csv_file, args.input_string, args.number_of_results


def relevancy_controller(csv_file=None,
                         input_string=None,
                         number_of_results=None):
    """
    relevancy_controller method used as an aggregator method.

    Modules used:
        sys

    Algorithm used:
        cosine similarity

    Sample running method:
        >> relevancy_controller(csv_file='~/suyashshukla/Downloads/Sample.csv',
                                input_string='India wins again')
        returns TOP 10/15 articles(number defined in constants.py file)
            related to the string
        >> relevancy_controller()
        returns TOP related results, but the csv_file and input_string
            will be used from constants.py file.
    :csv_news_list: list to store the return list from csv_parser method
    :article_set: set to store the full_articles from the csv_news_list
    :relevant_articles: dictionary of relvant articles with similarity scores
    :item: iterator for csv_news_list
    """
    csv_news_list = csv_to_list.csv_parser(csv_file=csv_file)
    article_set = set()
    article_set.add(input_string)
    csv_news_list = csv_news_list[1:]
    for item in csv_news_list:
        article_set.add(item[7])
    relevant_articles = cosine_similarity.similarity_calculator(document=article_set,
                                                                input_string=input_string)
    # print relevant_articles
    return_s = object_dict.return_relevant_articles_dict(input_string=input_string,
                                                         relevant_articles=relevant_articles,
                                                         number_of_results=number_of_results)
    print return_s
    return return_s

if __name__ == '__main__':
    csv_file, input_string, number_of_results = get_args()
    relevancy_controller(csv_file=csv_file,
                         input_string=input_string,
                         number_of_results=number_of_results)
