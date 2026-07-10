"""
TF-IDF Vectorization Module for ALIS.

Purpose:
--------
This module converts textual questions into numerical vectors
using the TF-IDF (Term Frequency - Inverse Document Frequency)
algorithm. These vectors are later compared using cosine
similarity inside the retrieval engine.
"""

# ==========================================================
# IMPORT REQUIRED LIBRARIES
# ==========================================================

# Import the TF-IDF vectorizer from Scikit-learn.
from sklearn.feature_extraction.text import TfidfVectorizer


# ==========================================================
# CREATE TF-IDF VECTORIZER
# ==========================================================

def create_vectorizer():
    """
    Create and return a TF-IDF vectorizer.

    Returns
    -------
    TfidfVectorizer
        Configured TF-IDF vectorizer object.
    """

    # ------------------------------------------------------
    # lowercase=True
    # Converts every word into lowercase before learning.
    #
    # stop_words=None
    # We are intentionally NOT removing stop words yet.
    # This keeps the implementation simple and allows
    # future experimentation.
    # ------------------------------------------------------

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words=None
    )

    return vectorizer


# ==========================================================
# CREATE TF-IDF MATRIX
# ==========================================================

def fit_vectorizer(vectorizer, questions):
    """
    Learn the vocabulary from dataset questions and convert
    every question into a TF-IDF vector.

    Parameters
    ----------
    vectorizer : TfidfVectorizer

    questions : list
        List containing every question in the dataset.

    Returns
    -------
    scipy sparse matrix
        TF-IDF representation of all dataset questions.
    """

    # ------------------------------------------------------
    # fit_transform() performs TWO operations:
    #
    # 1. Learns the vocabulary from the dataset.
    # 2. Converts every question into a TF-IDF vector.
    # ------------------------------------------------------

    tfidf_matrix = vectorizer.fit_transform(questions)

    return tfidf_matrix


# ==========================================================
# TRANSFORM USER QUERY
# ==========================================================

def transform_query(vectorizer, query):
    """
    Convert a user query into TF-IDF vector format.

    Parameters
    ----------
    vectorizer : TfidfVectorizer

    query : str
        User's processed question.

    Returns
    -------
    scipy sparse matrix
        TF-IDF vector of the user query.
    """

    # ------------------------------------------------------
    # transform() DOES NOT learn anything.
    #
    # It simply converts the new query using the vocabulary
    # already learned from the dataset.
    # ------------------------------------------------------

    return vectorizer.transform([query])