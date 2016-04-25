"""Object dict module."""

import collections


def return_relevant_articles_dict(input_string=None,
                                  relevant_articles=None,
                                  number_of_results=None):
    """
    return_relevant_articles_dict method.

    Purpose:
        It is used for returning selected scores that are sorted

    Returns:
        Dictionary
        Sample response:
            {
                'input_string': value of input string,
                full_articles: cosine similarity score
                ...
            }

    Modules used:
        collections

    Sample running method:
        >> return_relevant_articles_dict(relevant_articles=relevant_articles)
        returns {
                    'input_string': 'India wins again',
                    'India scores yet again',
                    ....
                }
    """
    if not relevant_articles:
        return dict()
    sorted_dict = collections.OrderedDict(sorted(relevant_articles.items()))
    return_dict = dict()
    return_dict.update({'input': input_string})
    ii = 0
    for i, value in enumerate(sorted_dict.items()):
        # print str(i) + '\n' + 'count:' + str(count) + str(number_of_results)
        if ii < number_of_results:
            # print ii
            output_key = 'output' + str(i)
            return_dict.update({output_key: value})
        ii = ii + 1
    return return_dict
