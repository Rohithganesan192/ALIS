# Response Handler for ALIS.

# Purpose:
# --------
# This module formats the response returned by the retrieval
# engine before it is displayed to the user.


# ==========================================================
# FORMAT CHATBOT RESPONSE
# ==========================================================

def generate_response(record, similarity_score):
    """
    Generate a user-friendly response.

    Parameters
    ----------
    record : pandas.Series or None
        The dataset record returned by the retrieval engine.

    similarity_score : float
        Similarity score of the matched record.

    Returns
    -------
    str
        Formatted chatbot response.
    """

    # ------------------------------------------------------
    # If no matching record was found, return a fallback
    # message to the user.
    # ------------------------------------------------------
    if record is None:

        return (
            "Sorry, I couldn't find a relevant answer "
            "to your question."
        )

    # ------------------------------------------------------
    # Extract useful information from the matched record.
    # ------------------------------------------------------
    record_id = record["record_id"]

    category = record["category"]

    answer = record["answer"]

    # ------------------------------------------------------
    # Build a clean response string.
    # ------------------------------------------------------
    response = (
        f"\nRecord ID : {record_id}\n"
        f"Category  : {category}\n\n"
        f"Answer:\n{answer}\n\n"
        f"(Similarity Score: {similarity_score:.2f})"
    )

    return response