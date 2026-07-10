"""
Main Application for ALIS.

Purpose:
--------
This module integrates all components of the chatbot and
controls the complete execution flow.
"""

# ==========================================================
# IMPORT MODULES
# ==========================================================

import sys
from dataset_loader import load_dataset

from preprocessing import preprocess_text

from vectorizer import (
    create_vectorizer,
    fit_vectorizer,
    transform_query
)

from retrieval import retrieve_record

from response_handler import generate_response

from cli_interface import (
    get_user_query,
    display_response
)


# ==========================================================
# LOAD DATASET
# ==========================================================

try:

    dataset = load_dataset()

except FileNotFoundError as error:

    print("\nError:")
    print(error)

    sys.exit()

except ValueError as error:

    print("\nError:")
    print(error)

    print("\nPlease populate:")
    print("data/assembly_shop_dataset.csv")

    sys.exit()

questions = dataset["question_primary"]

# ==========================================================
# CREATE TF-IDF MODEL
# ==========================================================

vectorizer = create_vectorizer()

tfidf_matrix = fit_vectorizer(
    vectorizer,
    questions
)


# ==========================================================
# MAIN APPLICATION LOOP
# ==========================================================

print("\n===================================")
print(" Assembly Line Information System ")
print("===================================")

print("\nType 'exit' to close the chatbot.\n")

while True:

    # ------------------------------------------
    # Read user input
    # ------------------------------------------

    user_query = get_user_query()

    # ------------------------------------------
    # Exit condition
    # ------------------------------------------

    if user_query.lower() == "exit":

        print("\nThank you for using ALIS.")
        break

    # ------------------------------------------
    # Preprocess user query
    # ------------------------------------------

    processed_query = preprocess_text(user_query)

    # ------------------------------------------
    # Convert query into TF-IDF vector
    # ------------------------------------------

    query_vector = transform_query(
        vectorizer,
        processed_query
    )

    # ------------------------------------------
    # Retrieve best matching record
    # ------------------------------------------

    record, score = retrieve_record(
        query_vector,
        tfidf_matrix,
        dataset
    )

    # ------------------------------------------
    # Generate final response
    # ------------------------------------------

    response = generate_response(
        record,
        score
    )

    # ------------------------------------------
    # Display response
    # ------------------------------------------

    display_response(response)