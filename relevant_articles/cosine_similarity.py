"""Cosine_similarity module."""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def similarity_calculator(document=None,
                          input_string=None,
                          number_of_results=None):
    """
    similarity_calculator method.

    Purpose:
        It is used to calculate similarity score from documents for
        the given input_string.

    Returns:
        Dictionary
        Sample response:
            {
                'input_string': value of input string,
                full_articles: cosine similarity score
                ...
            }

    Modules used:
        scikit_learn

    Sample running method:
        >> similarity_calculator(document=document,
                                 input_string='India wins again')
        returns {
                    'input_string': 'India wins again',
                    'India scores yet again': 0.9158,
                    ....
                }
    :input_string: Input String
    :number_of_results: Number of results to be shown
    :tdidf_vectorizer: instantiating Sklearn TF-IDF Vectorizer
    :tfidf_matrix: matrix after using document set by tfidf_vectorizer
    :cosine_similar_list: list of cosine similarity scores
    :score_dict: dictionary like {
                                    full_article: score,
                                    ...
                                }
    """
    tfidf_vectorizer = TfidfVectorizer()
    document.add(input_string)
    tfidf_matrix = tfidf_vectorizer.fit_transform(document)
    cosine_similar_list = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    cosine_similar_list = np.array(cosine_similar_list).tolist()[0][1:]
    score_dict = dict()
    for count, item in enumerate(cosine_similar_list):
        score_dict.update({item: document.pop()})
    return score_dict
