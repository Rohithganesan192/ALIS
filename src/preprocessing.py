# 
# Text Preprocessing Module for ALIS.

# Purpose:
# --------
# This module performs basic preprocessing on user queries before
# they are passed to the retrieval engine.

# Current preprocessing steps:
# 1. Convert text to lowercase.
# 2. Remove leading and trailing whitespace.
# 3. Replace multiple spaces with a single space.
# 

# ==========================================================
# IMPORT REQUIRED LIBRARIES
# ==========================================================

import re

# "re" stands for REGULAR EXPRESSIONS
# It is used for searching and modifying text such as removal of punctuation ,special characters,etc.


# ==========================================================
# PREPROCESS USER QUERY
# ==========================================================

def preprocess_text(text: str) -> str:
    """
    Clean and normalize user input.

    Parameters
    ----------
    text : str
        Raw user query.

    Returns
    -------
    str
        Cleaned query.
    """

    # ------------------------------------------------------
    # Convert the text to lowercase.
    # This ensures that "PPE" and "ppe" are treated equally.
    # ------------------------------------------------------
    text = text.lower()

    # ------------------------------------------------------
    # Remove unwanted spaces at the beginning and end.
    # Example:
    # "   hello   " -> "hello"
    # ------------------------------------------------------
    text = text.strip()

    # ------------------------------------------------------
    # Replace multiple spaces with a single space.
    #
    # Example:
    # "what    is     ppe"
    #
    # becomes
    #
    # "what is ppe"
    # ------------------------------------------------------
    text = re.sub(r"\s+", " ", text)

    # sub(r"\s+", " ", text)->Used to replace every group of one or more whitespace characters with a single space.

    return text


# ==========================================================
# MODULE TESTING
# ==========================================================

if __name__ == "__main__":

    sample_query = "   What     IS      PPE???   "

    print("Original Query :")
    print(sample_query)

    print("\nProcessed Query :")
    print(preprocess_text(sample_query))