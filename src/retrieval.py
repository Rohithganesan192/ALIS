# Retrieval Engine for ALIS

# Purpose:

# This module compares the user's query with all stored questions
# using TF-IDF vectors and Cosine Similarity. It returns the most
# relevant knowledge record if the similarity score meets the
# configured threshold. 

# ==========================================================
# IMPORT REQUIRED LIBRARIES
# ==========================================================

from sklearn.metrics.pairwise import cosine_similarity

from config import SIMILARITY_THRESHOLD

# ==========================================================
# RETRIEVE THE BEST MATCHING RECORD
# ==========================================================

def retrieve_record(query_vector, tfidf_matrix, dataset):

    #Retrieve the dataset record that best matches the user's query.

    # ------------------------------------------------------
    # Calculate cosine similarity between the user query
    # and every question stored in the dataset.
    # ------------------------------------------------------

    similarity_scores = cosine_similarity(
        query_vector, # TF-IDF vector representing the user's query.
        tfidf_matrix  # TF-IDF matrix representing all dataset questions.
    )[0]

    #dataset : Pandas DataFrame containing the knowledge base.

    # ------------------------------------------------------
    # Find the index of the highest similarity score.
    # ------------------------------------------------------

    best_match_index = similarity_scores.argmax()

    # ------------------------------------------------------
    # Check whether the similarity score is high enough.
    # ------------------------------------------------------

    if best_match_score >= SIMILARITY_THRESHOLD:

        matching_record = dataset.iloc[best_match_index]

        return matching_record, best_match_score  #tuple(record,similarity_score)

        # matching_record -> Matching dataset row if similarity >= threshold. Otherwise,None.
        # similarity_score -> Highest cosine similarity score.
        
    # ------------------------------------------------------
    # No sufficiently similar record was found.
    # ------------------------------------------------------

    return None, best_match_score