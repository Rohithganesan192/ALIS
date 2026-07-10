"""
Configuration settings for ALIS.

This module acts as the single source of truth for configurable values
used throughout the application.
"""

from pathlib import Path      #Path is a class for handling file and folder paths

# ----------------------------
# Project Paths
# ----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent 

# __file__ contains src/config.py path  
# Path(__file__) will convert it into the full absolute path.
# .parent ->moves one folder up 
# .parent.parent ->moves up two levels up in the path
# PROJECT_ROOT -> Stores the actual path
# Visulaization: config.py->src->ALIS

DATA_DIR = PROJECT_ROOT / "data"

# PROJECT_ROOT ->Contains ALIS 
# /"data" ->creates ALIS/data path
#DATA_DIR ->used to store the path

DATASET_FILE = DATA_DIR / "assembly_shop_dataset.csv"

# DATA_DIR -> Contains ALIS/data
# DATA_DIR / "assembly_shop_dataset.csv" -> Appends and creates ALIS/data/assembly_shop_dataset.csv . This is where the dataset will be live.

TEST_QUERY_FILE = DATA_DIR / "test_queries.csv"

# DATA_DIR / "test_queries.csv" -> Creates ALIS/data/test_queries.csv and stored in TEST_QUERY_FILE

CATEGORY_FILE = DATA_DIR / "category_reference.csv"

# DATA_DIR / "category_reference.csv" -> Creates DATA_DIR / "category_reference.csv" and stored in CATEGORY_FILE 

# ----------------------------
# NLP Configuration
# ----------------------------

SIMILARITY_THRESHOLD = 0.30 

# Only scores ≥ 0.30 will be accepted.
# Otherwise the chatbot will return -> "Sorry, I couldn't find a relevant answer."

LANGUAGE = "english"