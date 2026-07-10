# Step 4 – NLP Implementation

## Task 4.1 – Project Setup

### Objective

Prepare the Assembly Line Information System (ALIS) development environment for implementation by establishing a standardized project structure, configuring dependencies, and creating the initial application modules.

### Activities Performed

- Created the project directory structure.
- Configured the Python virtual environment.
- Installed the required NLP libraries.
- Generated the `requirements.txt` file.
- Created the core Python modules.
- Created the dataset files.
- Implemented the centralized configuration module (`config.py`).
- Configured Visual Studio Code to use the project virtual environment.

### Output

The ALIS project is now ready for implementation. All future modules will utilize the centralized configuration settings and standardized project structure established during this task.

---

## Task 4.2 – Dataset Loader

### Objective

Implement the Dataset Loader module responsible for reading the ALIS knowledge base from the dataset file and making it available to the remaining application modules. The loader also performs basic validation to ensure the dataset exists and contains valid records before further processing begins.

### Design Rationale

The Dataset Loader follows the Single Responsibility Principle by assigning all dataset loading operations to a dedicated module. Instead of allowing multiple modules to independently read the dataset file, a centralized loader provides a consistent and validated interface for accessing the knowledge base.

This design improves maintainability, reduces code duplication, and ensures that every component of the chatbot works with the same validated dataset.

### Activities Performed

- Created the `dataset_loader.py` module.
- Imported the dataset path from the centralized configuration module.
- Implemented the `load_dataset()` function.
- Loaded the dataset using the Pandas library.
- Added exception handling for missing dataset files.
- Added validation to detect empty datasets.
- Returned the dataset as a Pandas DataFrame.
- Included an independent testing block for module verification.

### Validation Performed

The module verifies that:

- The dataset file exists.
- The dataset can be successfully loaded.
- The dataset contains at least one knowledge record.
- The dataset is returned in a usable DataFrame format.

If any validation fails, an appropriate exception is raised with a descriptive error message.

### Output

The Dataset Loader provides a reusable interface for loading the ALIS knowledge base. All subsequent modules, including preprocessing, retrieval, evaluation, and the main application, will obtain the dataset through this module rather than accessing the CSV file directly.

### Result

A centralized dataset loading component has been successfully implemented. The module establishes the foundation for the NLP pipeline by ensuring that every downstream component operates on a validated and consistent dataset.

---

## Task 4.3 – Text Preprocessing

### Objective

Implement the text preprocessing module responsible for normalizing user queries before retrieval.

### Activities Performed

- Created the preprocessing module.
- Converted user input to lowercase.
- Removed leading and trailing whitespace.
- Normalized multiple spaces into a single space.
- Tested preprocessing independently using sample queries.

### Output

A reusable preprocessing function capable of producing standardized text suitable for the retrieval engine.

---

## Task 4.4 – TF-IDF Vectorization

### Objective

Implement the TF-IDF Vectorization module responsible for converting textual questions into numerical vector representations. These vectors enable the chatbot to mathematically compare user queries with the knowledge base and retrieve the most relevant answer.

### Design Rationale

Computers cannot directly compare natural language sentences because they operate on numerical data rather than textual information. Therefore, every question in the dataset must first be transformed into a numerical representation before similarity calculations can be performed.

The TF-IDF (Term Frequency – Inverse Document Frequency) algorithm was selected because it is lightweight, interpretable, and well suited for small and medium-sized retrieval-based NLP systems such as ALIS. It assigns higher importance to words that are significant within a document while reducing the influence of commonly occurring words.

To maintain consistency, the vectorizer is trained only once using the dataset questions. User queries are then transformed using the same learned vocabulary, ensuring that both dataset records and user queries exist within the same vector space.

### Activities Performed

- Created the `vectorizer.py` module.
- Imported the `TfidfVectorizer` class from Scikit-learn.
- Implemented a reusable function for creating the TF-IDF vectorizer.
- Configured the vectorizer for lowercase text processing.
- Implemented dataset vectorization using the `fit_transform()` method.
- Implemented user query transformation using the `transform()` method.
- Separated dataset training from query transformation to preserve vocabulary consistency.
- Documented each processing stage through inline code comments.

### Validation Performed

The following conditions were verified:

- The vectorizer object is successfully created.
- Dataset questions are converted into TF-IDF vectors.
- User queries are transformed using the existing vocabulary.
- The vocabulary remains unchanged after user queries are processed.
- Dataset vectors and user-query vectors belong to the same feature space, allowing similarity calculations.

### Output

The TF-IDF Vectorization module provides a reusable interface for converting textual information into numerical vectors. The generated vectors will serve as the input to the Retrieval Engine, where cosine similarity will be used to identify the most relevant knowledge record.

### Result

A complete TF-IDF vectorization component has been successfully implemented. The module establishes the mathematical representation of textual data required for semantic similarity matching and forms the core NLP foundation of the ALIS retrieval pipeline.

---

## Task 4.5 – Retrieval Engine

### Objective

Implement the retrieval engine responsible for identifying the most relevant knowledge record for a user's query using TF-IDF vectors and cosine similarity.

### Activities Performed

- Created the `retrieval.py` module.
- Calculated cosine similarity between the query vector and dataset vectors.
- Identified the highest similarity score.
- Retrieved the corresponding dataset record.
- Applied the configured similarity threshold.
- Returned either the matching record or a no-match result.

### Output

A reusable retrieval module capable of selecting the most relevant knowledge record from the ALIS dataset based on semantic similarity while preventing weak matches through threshold validation.

---

## Task 4.6 – Response Handler

### Objective

Implement the Response Handler responsible for formatting the retrieved knowledge record into a clear and user-friendly response before displaying it to the user.

### Design Rationale

The Retrieval Engine is responsible only for identifying the most relevant record. Presenting that record directly would expose unnecessary internal information and reduce readability. Therefore, a dedicated Response Handler module is introduced to separate retrieval logic from presentation logic.

This separation improves modularity, maintainability, and future extensibility by allowing response formatting to evolve independently of retrieval functionality.

### Activities Performed

- Created the `response_handler.py` module.
- Implemented response generation for successful retrievals.
- Implemented fallback response generation when no suitable match is found.
- Extracted relevant fields from the retrieved record.
- Formatted the final response into a user-friendly structure.

### Validation Performed

The module verifies that:

- A valid record is correctly formatted.
- Missing records generate a fallback response.
- The similarity score is displayed consistently.
- Internal dataset fields not intended for users are not exposed.

### Output

The Response Handler produces a clean textual response containing the record identifier, category, answer, and similarity score, or a fallback message when no suitable answer exists.

### Result

A dedicated presentation component has been successfully implemented. The module separates retrieval logic from response formatting, improving the modular design of the ALIS chatbot.
