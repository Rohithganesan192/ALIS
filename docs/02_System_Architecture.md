# System Architecture

## 1. Introduction

The System Architecture of the Assembly Line Information System (ALIS) defines the overall structure of the chatbot, the interaction between its software components, and the flow of information from the moment a user submits a question until the system returns an appropriate response.

Unlike the Project Definition document, which explains why the project exists and what it aims to achieve, this document focuses on how the system is designed. It describes the architectural decisions taken before implementation, ensuring that every component has a clear responsibility and that the overall design remains modular, maintainable, and extensible.

ALIS follows a retrieval-based Natural Language Processing (NLP) architecture. Instead of generating answers using external Artificial Intelligence services or Large Language Models (LLMs), the chatbot retrieves information only from a developer-curated assembly-shop dataset. This design ensures that every response is traceable, deterministic, and consistent with the project's objective of building an offline, domain-specific chatbot.

The architecture emphasizes:

- Modular software design
- Separation of responsibilities
- Dataset-grounded responses
- Lightweight NLP techniques
- Maintainability
- Future extensibility

The system has been intentionally designed around beginner-friendly technologies while still following standard software engineering principles.

---

# 2. Overall System Architecture

## 2.1 Architecture Overview

ALIS follows a linear retrieval-based architecture. Every user query passes through a sequence of independent processing stages before a response is returned. Each stage performs one well-defined task and passes its output to the next stage.

The architecture avoids unnecessary complexity such as deep learning models, external APIs, conversational memory, or cloud services. Instead, it focuses on a transparent NLP pipeline that can be fully understood, implemented, and maintained by a beginner developer.

The system consists of the following logical components:

1. User Interface (CLI)
2. Text Preprocessing Module
3. Retrieval Engine
4. Assembly Shop Knowledge Base
5. Best Match Selector
6. Fallback Handler
7. Response Formatter

Each component has a single responsibility and communicates only with the components immediately required for its task.

---

## 2.2 Component Responsibilities

### 1. User Interface (CLI)

The Command Line Interface serves as the entry point into the system.

Responsibilities include:

- Accepting user questions
- Validating input
- Passing queries to the NLP pipeline
- Displaying responses
- Handling session termination

The interface contains no NLP logic.

---

### 2. Text Preprocessing Module

This component prepares raw user queries for comparison with the dataset.

Its responsibilities include:

- Lowercase conversion
- Punctuation removal
- Tokenization
- Optional stopword removal
- Optional lemmatization

The same preprocessing pipeline is applied to both the dataset and user queries to maintain consistency.

---

### 3. Retrieval Engine

The Retrieval Engine performs the core NLP processing.

Its responsibilities include:

- Transforming queries into TF-IDF vectors
- Computing cosine similarity
- Ranking candidate matches
- Applying the similarity threshold

The Retrieval Engine never generates new information. It only identifies the most relevant dataset entry.

---

### 4. Assembly Shop Knowledge Base

The knowledge base is the only source of information available to ALIS.

It contains developer-authored information including:

- Safety procedures
- Assembly procedures
- Equipment information
- Operator roles
- Shop terminology
- General workflow information

The dataset is loaded during application startup and remains read-only during execution.

---

### 5. Best Match Selector

This component evaluates the ranked similarity scores.

Its responsibilities include:

- Selecting the highest-scoring dataset entry
- Comparing the score against the predefined threshold
- Deciding whether the match is sufficiently reliable

---

### 6. Fallback Handler

If no dataset entry satisfies the similarity threshold, this component activates.

Its responsibilities include:

- Returning a predefined fallback message
- Preventing incorrect responses
- Maintaining dataset-grounded behaviour

This ensures the chatbot never fabricates information.

---

### 7. Response Formatter

The Response Formatter prepares the final output shown to the user.

Responsibilities include:

- Formatting responses consistently
- Displaying matched answers
- Displaying fallback responses
- Maintaining a uniform presentation style

---

## 2.3 Architectural Principles

The architecture follows several important software engineering principles.

### Modular Design

Each component performs only one responsibility.

This makes the system easier to understand, maintain, and extend.

---

### Low Coupling

Components communicate through clearly defined inputs and outputs.

Changes made to one module have minimal impact on the others.

---

### High Cohesion

All operations within a module are closely related.

For example, every preprocessing operation is grouped inside the Preprocessing Module rather than scattered throughout the project.

---

### Dataset Grounding

Every response originates from the developer-authored dataset.

The chatbot never accesses:

- Internet resources
- External APIs
- Online AI models
- Production databases

This guarantees predictable and verifiable responses.

---

### Extensibility

Future enhancements such as:

- Intent Classification
- Named Entity Recognition
- Semantic Embeddings
- Flask Interface
- Web Dashboard

can be added without redesigning the entire system.

---

# 3. High-Level Workflow

The High-Level Workflow describes the sequence of operations performed by ALIS whenever a user submits a question.

Each interaction is independent.

The chatbot does not remember previous questions and therefore treats every query as a new request.

The workflow consists of eight stages.

## Step 1 – Query Acquisition

The user enters a natural-language question through the Command Line Interface.

The system validates the input before processing begins.

Output:

- Raw query string

---

## Step 2 – Text Preprocessing

The raw query is normalized through several preprocessing operations.

These include:

- Lowercase conversion
- Punctuation removal
- Tokenization
- Optional stopword removal
- Optional lemmatization

Output:

- Cleaned query

---

## Step 3 – Query Vectorization

The cleaned query is transformed into a TF-IDF vector using the same fitted vectorizer that was created during application startup.

The vectorizer is never refitted during runtime.

Output:

- Query TF-IDF Vector

---

## Step 4 – Similarity Scoring

Cosine similarity is calculated between the query vector and every dataset vector.

The system produces one similarity score for each dataset entry.

Output:

- Similarity score list

---

## Step 5 – Candidate Ranking

Similarity scores are sorted in descending order.

The entry with the highest similarity score becomes the primary candidate.

Output:

- Ranked candidate list

---

## Step 6 – Threshold Checking

The highest similarity score is compared against the predefined similarity threshold.

If the threshold is satisfied:

- The candidate is accepted.

Otherwise:

- The fallback path is activated.

---

## Step 7 – Answer Resolution

If a valid match exists:

- Retrieve the corresponding answer from the dataset.

Otherwise:

- Generate the fallback response.

Output:

- Raw answer text

---

## Step 8 – Response Display

The response is formatted and displayed through the Command Line Interface.

The interaction then ends, and the chatbot waits for the next independent query.

# 4. Module Architecture

## 4.1 Overview

The ALIS software is organized into independent Python modules, where each module performs one specific responsibility. This modular architecture follows the principle of **Single Responsibility**, ensuring that each module focuses on one task without mixing unrelated functionality.

This approach provides several advantages:

- Easier debugging
- Better maintainability
- Cleaner code organization
- Simpler future enhancements
- Reduced coupling between modules

The complete system consists of nine modules that together implement the entire NLP pipeline.

---

## 4.2 Module Descriptions

### Module 1 – Dataset Loader (`dataset_loader.py`)

#### Purpose

Load the developer-authored assembly shop dataset into memory and validate its structure before the chatbot begins processing queries.

#### Responsibilities

- Read the dataset file (CSV or JSON)
- Validate required columns
- Detect missing or invalid records
- Convert data into an in-memory structure (DataFrame or list)
- Provide dataset access to other modules

#### Inputs

- Dataset file path

#### Outputs

- Structured dataset object

#### Dependencies

- pandas
- config.py

#### Future Enhancements

- Multiple dataset support
- Automatic schema validation
- Dataset version management

---

### Module 2 – Preprocessing (`preprocessing.py`)

#### Purpose

Normalize textual data so that both user queries and dataset entries are processed consistently.

#### Responsibilities

- Lowercase conversion
- Remove punctuation
- Tokenization
- Stopword removal (optional)
- Lemmatization (optional)

#### Inputs

- Raw text

#### Outputs

- Cleaned text

#### Dependencies

- NLTK

#### Future Enhancements

- Synonym normalization
- Spell correction
- Multilingual preprocessing

---

### Module 3 – Vectorizer (`vectorizer.py`)

#### Purpose

Convert processed text into TF-IDF vectors suitable for similarity comparison.

#### Responsibilities

- Fit the TF-IDF vectorizer using the dataset
- Store the fitted vectorizer
- Transform incoming user queries
- Produce dataset and query vectors

#### Inputs

- Preprocessed dataset
- Preprocessed query

#### Outputs

- Dataset TF-IDF matrix
- Query TF-IDF vector

#### Dependencies

- scikit-learn
- preprocessing.py

#### Future Enhancements

- Sentence embeddings
- Semantic vector representations

---

### Module 4 – Retrieval Engine (`retrieval.py`)

#### Purpose

Identify the most relevant dataset entry using similarity scoring.

#### Responsibilities

- Calculate cosine similarity
- Rank similarity scores
- Apply similarity threshold
- Select the best candidate

#### Inputs

- Query vector
- Dataset vectors
- Similarity threshold

#### Outputs

- Matching dataset index
- Similarity score

#### Dependencies

- scikit-learn
- vectorizer.py

#### Future Enhancements

- Intent-aware filtering
- Category-based retrieval
- Adaptive thresholds

---

### Module 5 – Response Handler (`response_handler.py`)

#### Purpose

Convert the retrieval result into a user-friendly response.

#### Responsibilities

- Retrieve the answer text
- Generate fallback responses
- Format output consistently

#### Inputs

- Match result
- Dataset object

#### Outputs

- Final chatbot response

#### Dependencies

- retrieval.py
- dataset_loader.py

#### Future Enhancements

- Confidence indicators
- Template-based responses

---

### Module 6 – CLI Interface (`cli_interface.py`)

#### Purpose

Provide a command-line interface for interacting with the chatbot.

#### Responsibilities

- Accept user input
- Validate empty input
- Display chatbot responses
- Handle exit commands

#### Inputs

- Keyboard input

#### Outputs

- Terminal output

#### Dependencies

- main.py
- response_handler.py

#### Future Enhancements

- Flask interface
- FastAPI interface
- Desktop GUI

---

### Module 7 – Evaluation (`evaluation.py`)

#### Purpose

Evaluate chatbot performance using a manually prepared test dataset.

#### Responsibilities

- Load evaluation queries
- Execute the NLP pipeline
- Compare predicted and expected responses
- Calculate evaluation metrics

#### Inputs

- Test dataset

#### Outputs

- Accuracy report
- Timing report
- Evaluation statistics

#### Dependencies

- Entire NLP pipeline

#### Future Enhancements

- Automated regression testing
- Performance benchmarking

---

### Module 8 – Configuration (`config.py`)

#### Purpose

Maintain all configurable system parameters in one location.

#### Responsibilities

- Dataset path
- Similarity threshold
- Preprocessing options
- File locations

#### Inputs

None

#### Outputs

Configuration values

#### Dependencies

None

#### Future Enhancements

- YAML configuration
- Environment variable support

---

### Module 9 – Main Application (`main.py`)

#### Purpose

Serve as the application's entry point.

#### Responsibilities

- Load configuration
- Initialize dataset
- Initialize vectorizer
- Start the CLI interface

#### Inputs

None

#### Outputs

Running chatbot application

#### Dependencies

All project modules

#### Future Enhancements

- Web server startup
- Deployment initialization

---

## 4.3 Module Relationship

The modules interact in the following sequence:

```
main.py
      │
      ▼
config.py
      │
      ▼
dataset_loader.py
      │
      ▼
preprocessing.py
      │
      ▼
vectorizer.py
      │
      ▼
retrieval.py
      │
      ▼
response_handler.py
      │
      ▼
cli_interface.py
```

The evaluation module operates independently and uses the same NLP pipeline without involving the CLI.

```
evaluation.py
        │
        ▼
preprocessing.py
        │
        ▼
vectorizer.py
        │
        ▼
retrieval.py
        │
        ▼
response_handler.py
```

---

# 5. Project Folder Structure

## 5.1 Overview

ALIS follows the standard Python **src-layout** project structure.

Separating source code, datasets, documentation, tests, and assets improves maintainability and makes the project easier to understand for future contributors, evaluators, and recruiters.

The folder organization also supports incremental development, allowing documentation and implementation to evolve independently.

---

## 5.2 Folder Structure

```text
ALIS/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── dataset_loader.py
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── retrieval.py
│   ├── response_handler.py
│   ├── cli_interface.py
│   └── evaluation.py
│
├── data/
│   ├── assembly_shop_dataset.csv
│   └── test_queries.csv
│
├── docs/
│   ├── 01_Project_Definition.md
│   ├── 02_System_Architecture.md
│   ├── 03_Dataset_Design.md
│   └── ...
│
├── tests/
│   ├── test_preprocessing.py
│   └── test_retrieval.py
│
└── assets/
    ├── architecture_diagram.png
    ├── workflow_diagram.png
    ├── dfd_level0.png
    ├── dfd_level1.png
    └── sequence_diagram.png
```

---

## 5.3 Folder Responsibilities

### `src/`

Contains the complete implementation of the chatbot.

No datasets or documentation should be stored inside this folder.

---

### `data/`

Stores all datasets used by the chatbot.

This includes:

- Assembly shop knowledge dataset
- Evaluation dataset
- Future datasets

Keeping datasets separate from code allows information to be updated without modifying program logic.

---

### `docs/`

Contains all planning and design documents.

Examples include:

- Project Definition
- System Architecture
- Dataset Design
- NLP Design
- Testing Documentation

These files form the technical documentation for the project.

---

### `tests/`

Contains scripts used to verify the correctness of individual modules.

Examples include:

- Preprocessing tests
- Retrieval tests

These are different from evaluation scripts, which measure chatbot performance.

---

### `assets/`

Stores all visual resources used in documentation.

Examples include:

- Architecture diagrams
- Workflow diagrams
- DFD diagrams
- Sequence diagrams
- Screenshots

Keeping images separate prevents clutter inside the documentation folder.

---

## 5.4 Root-Level Files

### README.md

Provides a high-level overview of ALIS for GitHub visitors.

---

### requirements.txt

Lists every Python dependency required to run the project.

Example:

- pandas
- numpy
- nltk
- scikit-learn

---

### .gitignore

Excludes unnecessary files from version control, including:

- Virtual environments
- Python cache files
- Temporary files
- IDE settings

---

## 5.5 Folder Design Principles

The project structure follows these principles:

- Clear separation between code and data
- Independent documentation
- Modular implementation
- Easy scalability
- Beginner-friendly navigation
- Standard Python project organization

# 6. Data Flow Diagram (DFD)

## 6.1 Introduction

A Data Flow Diagram (DFD) illustrates how data moves through ALIS. Unlike the workflow diagram, which focuses on the sequence of processing steps, or the module architecture, which describes software components, the DFD focuses solely on the movement and transformation of data.

The DFD identifies:

- External entities
- Internal processes
- Data stores
- Data flows

Since ALIS is a retrieval-based, single-turn chatbot, the data flows in one direction from user input to chatbot response without maintaining conversation history.

---

# 6.2 External Entity

## User

The User is the only external entity interacting with ALIS.

### Responsibilities

- Submit natural-language questions.
- Receive chatbot responses.
- Initiate every interaction.

The user does not directly access the dataset or any internal processing modules.

---

# 6.3 Data Stores

## D1 – Assembly Shop Dataset

### Purpose

Stores the complete developer-authored knowledge base.

### Contents

- Safety information
- Equipment information
- Procedures
- Roles
- KPIs
- General assembly knowledge

This dataset is read-only during chatbot execution.

---

## D2 – Dataset TF-IDF Matrix

### Purpose

Stores the vectorized representation of every dataset entry.

### Contents

- TF-IDF vectors
- Vocabulary
- Feature space

This data store is generated once during application startup and reused for every incoming query.

---

# 6.4 Processes

## Process 0.0 – Dataset Preparation

### Purpose

Prepare the dataset before user interaction begins.

### Activities

- Load dataset
- Validate records
- Apply preprocessing
- Fit TF-IDF vectorizer
- Generate dataset vectors

### Input

Assembly Shop Dataset

### Output

Dataset TF-IDF Matrix

---

## Process 1.0 – Query Preprocessing

### Purpose

Normalize user input.

### Activities

- Lowercase conversion
- Remove punctuation
- Tokenization
- Stopword removal (optional)
- Lemmatization (optional)

### Input

Raw user query

### Output

Cleaned query

---

## Process 2.0 – Query Vectorization

### Purpose

Convert the cleaned query into a TF-IDF vector.

### Input

Cleaned query

### Output

Query vector

---

## Process 3.0 – Retrieval

### Purpose

Identify the most relevant dataset entry.

### Activities

- Cosine similarity
- Ranking
- Threshold comparison

### Input

- Query vector
- Dataset vectors

### Output

Matched dataset index or fallback signal

---

## Process 4.0 – Response Generation

### Purpose

Generate the final chatbot response.

### Activities

- Retrieve answer
- Apply fallback if necessary
- Format output

### Input

- Match result
- Dataset

### Output

Formatted response

---

# 6.5 Context Diagram (Level 0)

At the highest level, ALIS behaves as a single process interacting with one external entity.

```text
                    Natural Language Query

        +-----------+                      +----------------+
        |           |                      |                |
        |   User    | ------------------> |      ALIS      |
        |           |                     |    Chatbot     |
        |           | <------------------ |                |
        +-----------+     Chatbot Reply   +----------------+
```

The internal implementation details remain hidden at this level.

---

# 6.6 Level 1 Data Flow Diagram

The Level 1 DFD expands the ALIS process into its individual processing stages.

```text
                     +---------------------------+
                     | D1 : Assembly Shop Dataset|
                     +------------+--------------+
                                  |
                                  |
                                  ▼
                      +------------------------+
                      | 0.0 Dataset Preparation|
                      +------------+-----------+
                                   |
                                   ▼
                    +-----------------------------+
                    | D2 : TF-IDF Dataset Vectors |
                    +--------------+--------------+
                                   |
                                   |
User Query                         ▼
----------> +------------------------------+
             | 1.0 Query Preprocessing      |
             +--------------+---------------+
                            |
                            ▼
             +------------------------------+
             | 2.0 Query Vectorization       |
             +--------------+---------------+
                            |
                            ▼
             +------------------------------+
             | 3.0 Retrieval                |
             +--------------+---------------+
                            |
                Match / No Match
                            |
                            ▼
             +------------------------------+
             | 4.0 Response Generation       |
             +--------------+---------------+
                            |
                            ▼
                    Chatbot Response
```

---

# 6.7 Data Flow Summary

| From                | To                  | Data             |
| ------------------- | ------------------- | ---------------- |
| User                | Query Preprocessing | Raw query        |
| Query Preprocessing | Query Vectorization | Cleaned query    |
| Query Vectorization | Retrieval           | Query vector     |
| Dataset Preparation | TF-IDF Store        | Dataset vectors  |
| TF-IDF Store        | Retrieval           | Vector matrix    |
| Retrieval           | Response Generation | Match result     |
| Dataset             | Response Generation | Answer text      |
| Response Generation | User                | Chatbot response |

---

# 6.8 Design Considerations

The DFD reflects several important architectural decisions.

- The dataset remains read-only.
- The chatbot never modifies stored knowledge.
- Dataset vectors are generated only once during startup.
- Every user query is processed independently.
- No conversational memory exists.
- No external APIs or internet resources participate in data flow.

---

# 7. NLP Pipeline Design

## 7.1 Overview

The NLP pipeline defines how textual information is transformed into a response.

Rather than generating answers using language models, ALIS retrieves the most relevant answer from a structured dataset using lightweight Natural Language Processing techniques.

The complete pipeline consists of eight sequential stages.

---

## Stage 1 – Query Input

### Purpose

Receive the user's natural-language question.

### Input

Keyboard input through the Command Line Interface.

### Output

Raw text string.

No NLP processing occurs at this stage.

---

## Stage 2 – Text Preprocessing

### Purpose

Normalize text before numerical processing.

### Operations

- Lowercase conversion
- Punctuation removal
- Tokenization
- Stopword removal (optional)
- Lemmatization (optional)

### Output

Cleaned text.

The same preprocessing pipeline is applied to both dataset entries and user queries.

---

## Stage 3 – TF-IDF Vectorization

### Purpose

Convert normalized text into numerical vectors.

### Technique

TF-IDF (Term Frequency – Inverse Document Frequency)

### Activities

- Fit vectorizer once using dataset
- Store vocabulary
- Transform user queries

### Output

Query TF-IDF vector.

---

## Stage 4 – Cosine Similarity

### Purpose

Measure similarity between the user query and every dataset entry.

### Technique

Cosine Similarity

### Output

Similarity scores ranging between 0 and 1.

Higher scores indicate stronger similarity.

---

## Stage 5 – Candidate Ranking

### Purpose

Identify the most relevant candidate.

### Activities

- Sort similarity scores
- Select highest score

### Output

Ranked list of dataset entries.

---

## Stage 6 – Threshold Evaluation

### Purpose

Determine whether the retrieved match is sufficiently reliable.

### Activities

- Compare highest score with similarity threshold.
- Accept or reject the candidate.

### Output

- Match
- No Match

This stage prevents incorrect responses.

---

## Stage 7 – Response Retrieval

### Purpose

Retrieve the appropriate answer.

### Activities

If matched:

- Retrieve dataset answer.

If unmatched:

- Generate fallback response.

### Output

Answer text.

---

## Stage 8 – Response Formatting

### Purpose

Prepare the response for presentation.

### Activities

- Format matched responses.
- Format fallback responses.
- Maintain consistent appearance.

### Output

Final chatbot response.

---

# 7.2 NLP Pipeline Diagram

```text
User Query
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Cosine Similarity
     │
     ▼
Candidate Ranking
     │
     ▼
Threshold Evaluation
     │
     ├──────────────► No Match
     │                    │
     ▼                    ▼
Retrieve Answer     Generate Fallback
         │                │
         └───────┬────────┘
                 ▼
         Response Formatting
                 │
                 ▼
          Chatbot Response
```

---

# 7.3 Pipeline Characteristics

The ALIS NLP pipeline has the following characteristics.

### Deterministic

The same query always produces the same result.

---

### Explainable

Every stage performs a clearly defined operation.

The complete decision-making process can be inspected and understood.

---

### Lightweight

No GPU or cloud infrastructure is required.

The pipeline executes efficiently on a standard student laptop.

---

### Modular

Each stage is independent.

Future techniques such as Intent Classification, Named Entity Recognition, or Sentence Embeddings can replace individual stages without redesigning the entire pipeline.

---

### Dataset Grounded

Every response originates exclusively from the developer-authored dataset.

No external knowledge sources participate in runtime processing.

# 8. Software Component Responsibility Design

## 8.1 Overview

The ALIS software architecture is divided into independent components, each responsible for one well-defined function within the chatbot. This design follows the **Single Responsibility Principle (SRP)**, ensuring that each component performs one primary task while interacting with other components through clearly defined interfaces.

This approach offers several advantages:

- Improved maintainability
- Easier debugging
- Better scalability
- Reduced coupling
- Higher code readability

Each component contributes to the overall NLP pipeline while remaining independent of the internal implementation of other components.

---

# 8.2 Software Components

## Component 1 – Dataset Loader

### Primary Responsibility

Load and validate the assembly shop dataset before the chatbot begins operation.

### Responsibilities

- Read dataset files
- Validate required fields
- Detect missing values
- Store data in memory

### Inputs

- Dataset file path

### Outputs

- Structured dataset object

### Dependencies

- Configuration Manager

### Future Enhancements

- Multiple datasets
- Schema validation
- Dataset version management

---

## Component 2 – Preprocessing Engine

### Primary Responsibility

Normalize textual data before vectorization.

### Responsibilities

- Lowercase conversion
- Remove punctuation
- Tokenization
- Stopword removal
- Lemmatization

### Inputs

- Raw text

### Outputs

- Cleaned text

### Dependencies

- NLTK

### Future Enhancements

- Spell correction
- Synonym expansion
- Multilingual support

---

## Component 3 – Vectorization Engine

### Primary Responsibility

Convert normalized text into numerical TF-IDF vectors.

### Responsibilities

- Fit TF-IDF vectorizer
- Transform user queries
- Maintain vocabulary consistency

### Inputs

- Cleaned dataset
- Cleaned query

### Outputs

- Dataset vectors
- Query vector

### Dependencies

- Preprocessing Engine

### Future Enhancements

- Sentence Embeddings
- Semantic Vectorization

---

## Component 4 – Retrieval Engine

### Primary Responsibility

Find the most relevant dataset entry.

### Responsibilities

- Cosine similarity
- Ranking
- Threshold evaluation

### Inputs

- Query vector
- Dataset vectors

### Outputs

- Match result
- Similarity score

### Dependencies

- Vectorization Engine
- Configuration Manager

### Future Enhancements

- Intent-aware retrieval
- Category filtering
- Adaptive thresholding

---

## Component 5 – Response Handler

### Primary Responsibility

Generate the final chatbot response.

### Responsibilities

- Retrieve answer
- Apply fallback logic
- Format responses

### Inputs

- Match result
- Dataset

### Outputs

- Final chatbot response

### Dependencies

- Retrieval Engine
- Dataset Loader

### Future Enhancements

- Confidence indicators
- Dynamic templates

---

## Component 6 – CLI Interface

### Primary Responsibility

Provide interaction between the user and the chatbot.

### Responsibilities

- Receive queries
- Display responses
- Handle exit commands
- Validate empty input

### Inputs

- Keyboard input

### Outputs

- Terminal output

### Dependencies

- Application Orchestrator

### Future Enhancements

- Flask interface
- FastAPI interface
- Desktop GUI

---

## Component 7 – Evaluation Harness

### Primary Responsibility

Measure chatbot performance using predefined evaluation queries.

### Responsibilities

- Execute evaluation dataset
- Compare predicted answers
- Calculate performance metrics

### Inputs

- Test dataset

### Outputs

- Evaluation report

### Dependencies

- NLP pipeline

### Future Enhancements

- Regression testing
- Comparative evaluation

---

## Component 8 – Configuration Manager

### Primary Responsibility

Maintain centralized configuration settings.

### Responsibilities

- File paths
- Similarity threshold
- Preprocessing settings
- System constants

### Inputs

None

### Outputs

Configuration values

### Dependencies

None

### Future Enhancements

- YAML configuration
- Environment variables

---

## Component 9 – Application Orchestrator

### Primary Responsibility

Initialize and coordinate the complete application.

### Responsibilities

- Load configuration
- Load dataset
- Initialize vectorizer
- Launch CLI

### Inputs

None

### Outputs

Running chatbot

### Dependencies

All project components

### Future Enhancements

- Web server startup
- Deployment initialization

---

# 8.3 Component Responsibility Matrix

| Component                | Data Access | Text Processing | Vectorization | Similarity Scoring | Decision Logic | Response Generation | User Interface | Configuration | Evaluation | Orchestration |
| ------------------------ | :---------: | :-------------: | :-----------: | :----------------: | :------------: | :-----------------: | :------------: | :-----------: | :--------: | :-----------: |
| Dataset Loader           |      ✓      |                 |               |                    |                |                     |                |               |            |               |
| Preprocessing Engine     |             |        ✓        |               |                    |                |                     |                |               |            |               |
| Vectorization Engine     |             |                 |       ✓       |                    |                |                     |                |               |            |               |
| Retrieval Engine         |             |                 |               |         ✓          |       ✓        |                     |                |               |            |               |
| Response Handler         |             |                 |               |                    |                |          ✓          |                |               |            |               |
| CLI Interface            |             |                 |               |                    |                |                     |       ✓        |               |            |               |
| Evaluation Harness       |             |                 |               |                    |                |                     |                |               |     ✓      |               |
| Configuration Manager    |             |                 |               |                    |                |                     |                |       ✓       |            |               |
| Application Orchestrator |             |                 |               |                    |                |                     |                |               |            |       ✓       |

---

# 8.4 Component Design Principles

The component architecture follows several software engineering principles.

### Single Responsibility Principle

Every component performs one primary task.

---

### Loose Coupling

Components exchange information only through clearly defined inputs and outputs.

---

### High Cohesion

Related functionality remains grouped within the same component.

---

### Reusability

Most components can be reused without modification if a web interface replaces the CLI.

---

### Extensibility

New NLP techniques can be introduced by replacing only specific components rather than redesigning the complete architecture.

---

# 9. Technology Stack Justification

## 9.1 Overview

The technology stack for ALIS has been selected based on the following criteria:

- Beginner friendliness
- Offline execution
- Low hardware requirements
- Explainability
- Ease of implementation
- Industry relevance

The selected technologies provide sufficient capability for a retrieval-based NLP chatbot while remaining simple enough for a second-year Computer Science student to understand and implement.

---

## 9.2 Technology Summary

| Technology        | Purpose                    | Justification                                                         |
| ----------------- | -------------------------- | --------------------------------------------------------------------- |
| Python            | Programming Language       | Simple syntax, extensive NLP ecosystem, existing developer knowledge  |
| VS Code           | Development Environment    | Lightweight IDE with excellent Python support                         |
| Git               | Version Control            | Tracks project history and enables safe experimentation               |
| GitHub            | Repository Hosting         | Portfolio presentation, collaboration, and backup                     |
| pandas            | Dataset Handling           | Efficient loading and manipulation of CSV datasets                    |
| NumPy             | Numerical Computing        | Provides efficient array operations required by scikit-learn          |
| NLTK              | Text Preprocessing         | Tokenization, stopword removal, and lemmatization                     |
| scikit-learn      | Machine Learning Utilities | TF-IDF Vectorizer and Cosine Similarity implementation                |
| TF-IDF            | Feature Extraction         | Converts text into numerical vectors without requiring model training |
| Cosine Similarity | Similarity Measurement     | Measures closeness between query and dataset vectors                  |
| CSV / JSON        | Data Storage               | Human-readable dataset format suitable for manual editing             |

---

## 9.3 Technology Selection Rationale

### Python

Python serves as the primary programming language because it offers a rich ecosystem of NLP libraries while remaining easy to understand and maintain.

---

### VS Code

VS Code provides an efficient development environment with integrated terminal support, debugging tools, and Git integration.

---

### Git and GitHub

Git enables systematic version control, while GitHub provides remote backup, collaboration support, and a professional portfolio repository.

---

### pandas

pandas simplifies reading, validating, filtering, and manipulating structured datasets without requiring manual file parsing.

---

### NumPy

NumPy provides optimized numerical arrays that form the computational foundation for machine learning libraries.

---

### NLTK

NLTK supplies lightweight preprocessing tools that are appropriate for beginner-level Natural Language Processing.

---

### scikit-learn

scikit-learn provides robust implementations of TF-IDF vectorization and cosine similarity, eliminating the need to implement these algorithms manually.

---

### TF-IDF

TF-IDF assigns greater importance to distinctive words while reducing the influence of frequently occurring terms.

This improves retrieval quality without requiring model training.

---

### Cosine Similarity

Cosine Similarity compares the orientation of vectors rather than their magnitude, making it effective for measuring textual similarity regardless of sentence length.

---

### CSV / JSON

CSV and JSON provide lightweight, portable storage formats that are easy to edit, inspect, and maintain throughout development.

---

# 9.4 Technology Stack Advantages

The selected technology stack provides several benefits.

- Runs entirely offline
- No GPU required
- Beginner friendly
- Lightweight implementation
- Easily explainable during project demonstrations
- Suitable for incremental development
- Simple to extend in future iterations

---

# 9.5 Limitations

Although appropriate for this project, the selected technologies have certain limitations.

- TF-IDF relies on lexical similarity rather than semantic understanding.
- Cosine Similarity cannot interpret context.
- NLTK provides basic preprocessing but not advanced language understanding.
- CSV datasets require manual maintenance.
- No conversational memory is available.

These limitations are acceptable for the current prototype and align with the project's defined scope.

# 10. Sequence Diagram

## 10.1 Overview

A Sequence Diagram illustrates the interaction between the various software components during a single user query. Unlike the Data Flow Diagram, which focuses on how data moves through the system, the Sequence Diagram emphasizes the order of communication between system components.

The diagram represents one complete query-response cycle, beginning with the user submitting a question and ending with the chatbot displaying the final response.

Since ALIS is a single-turn retrieval-based chatbot, each interaction is independent. No conversational context is maintained between successive queries.

---

## 10.2 Participants

The following participants take part in one complete interaction.

| Participant              | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **User**                 | Enters a natural-language question and receives the chatbot's response.            |
| **CLI Interface**        | Manages communication between the user and the internal NLP pipeline.              |
| **Preprocessing Module** | Cleans and normalizes the user query.                                              |
| **Retrieval Engine**     | Performs vectorization, similarity calculation, ranking, and threshold evaluation. |
| **Knowledge Base**       | Stores the assembly shop dataset and precomputed TF-IDF vectors.                   |
| **Response Handler**     | Retrieves the answer or fallback message and formats the final response.           |

---

## 10.3 Interaction Sequence

The complete interaction proceeds as follows.

### Step 1

The user enters a natural-language query through the Command Line Interface.

---

### Step 2

The CLI Interface forwards the raw query to the Preprocessing Module.

---

### Step 3

The Preprocessing Module performs:

- Lowercase conversion
- Punctuation removal
- Tokenization
- Optional stopword removal
- Optional lemmatization

The cleaned query is returned to the CLI.

---

### Step 4

The CLI forwards the cleaned query to the Retrieval Engine.

---

### Step 5

The Retrieval Engine transforms the cleaned query into a TF-IDF vector using the fitted vectorizer.

---

### Step 6

The Retrieval Engine accesses the Knowledge Base and retrieves the precomputed dataset vectors.

---

### Step 7

Cosine Similarity is calculated between the query vector and every dataset vector.

---

### Step 8

The Retrieval Engine ranks all similarity scores and evaluates the highest score against the configured similarity threshold.

---

### Step 9

The Retrieval Engine returns one of the following to the CLI.

- A matched dataset index
- A no-match signal

---

### Step 10

The CLI forwards the result to the Response Handler.

---

### Step 11

If a valid match exists, the Response Handler retrieves the corresponding answer from the Knowledge Base.

If no match exists, the Response Handler generates the predefined fallback response.

---

### Step 12

The Response Handler formats the response into a consistent presentation format.

---

### Step 13

The formatted response is returned to the CLI Interface.

---

### Step 14

The CLI displays the final response to the user.

The interaction then terminates, and the chatbot waits for the next independent query.

---

## 10.4 Sequence Diagram

```text
+------+      +-----------+      +---------------+      +----------------+      +---------------+      +----------------+
| User |      | CLI       |      | Preprocessing |      | Retrieval      |      | Knowledge     |      | Response       |
|      |      | Interface |      | Module        |      | Engine         |      | Base          |      | Handler        |
+------+      +-----------+      +---------------+      +----------------+      +---------------+      +----------------+
    |                 |                    |                      |                       |                     |
    | Query           |                    |                      |                       |                     |
    |---------------->|                    |                      |                       |                     |
    |                 | Raw Query          |                      |                       |                     |
    |                 |------------------->|                      |                       |                     |
    |                 |                    | Normalize Query      |                       |                     |
    |                 |                    |----------------------|                       |                     |
    |                 | Cleaned Query      |                      |                       |                     |
    |                 |<-------------------|                      |                       |                     |
    |                 |                    |                      |                       |                     |
    |                 |------------------------------->|          |                       |                     |
    |                 |                                | Vectorize Query                  |                     |
    |                 |                                |-------------------------------    |                     |
    |                 |                                | Request Dataset Vectors           |                     |
    |                 |                                |------------------------------->|  |                     |
    |                 |                                | Dataset Vectors                 |                     |
    |                 |                                |<-------------------------------|  |                     |
    |                 |                                | Similarity + Ranking            |                     |
    |                 |                                | Threshold Evaluation            |                     |
    |                 | Match / No Match               |                               |                     |
    |                 |<-------------------------------|                               |                     |
    |                 |                                                        Result   |                     |
    |                 |---------------------------------------------------------------->|                     |
    |                 |                                                        Retrieve Answer                |
    |                 |                                                        or Fallback                    |
    |                 |<----------------------------------------------------------------|                     |
    | Final Response  |                    |                      |                       |                     |
    |<----------------|                    |                      |                       |                     |
```

---

## 10.5 Sequence Design Characteristics

The interaction design follows several important principles.

### Synchronous Communication

Each component waits for the previous component to complete before continuing.

---

### Stateless Processing

Every query is processed independently.

No previous interaction influences the current query.

---

### Dataset Grounding

The Knowledge Base is the only source of information during runtime.

No internet resources or external APIs are accessed.

---

### Separation of Responsibilities

Each participant performs a clearly defined task.

For example:

- CLI manages interaction.
- Preprocessing handles text normalization.
- Retrieval performs similarity matching.
- Response Handler formats responses.

---

### Extensibility

Future enhancements such as:

- Intent Classification
- Named Entity Recognition
- Embedding-based Retrieval
- Flask Web Interface

can be incorporated without redesigning the overall interaction sequence.

---

# 11. Architecture Summary

The System Architecture presented in this document establishes the technical foundation of the Assembly Line Information System (ALIS). The design follows a modular, retrieval-based Natural Language Processing architecture that prioritizes simplicity, maintainability, and explainability while remaining suitable for a beginner developer.

The architecture consists of clearly separated components responsible for dataset management, text preprocessing, vectorization, retrieval, response generation, user interaction, configuration, and evaluation. This separation of concerns allows each module to be developed, tested, and extended independently, reducing system complexity and improving maintainability.

The chatbot operates through a linear NLP pipeline that transforms raw user queries into normalized text, converts them into TF-IDF vectors, computes cosine similarity against a developer-curated knowledge base, and returns either the best matching answer or an appropriate fallback response. This retrieval-based approach ensures that every response remains fully grounded in verified assembly shop data and avoids generating unsupported or fabricated information.

Several architectural models—including the overall system architecture, workflow, module architecture, data flow diagram, software component design, NLP pipeline, and sequence diagram—collectively describe the structure, behavior, and interaction of the system from multiple perspectives. Together, these models provide a comprehensive blueprint for implementation.

The selected technology stack, consisting of Python, VS Code, Git, GitHub, pandas, NumPy, NLTK, scikit-learn, TF-IDF, Cosine Similarity, and CSV/JSON datasets, aligns with the project's constraints of offline execution, limited hardware resources, and beginner-level NLP learning objectives. Each technology was chosen for its practicality, interpretability, and suitability for a lightweight retrieval-based chatbot.

Overall, the architecture satisfies the project's functional and non-functional requirements while remaining extensible for future enhancements such as intent classification, named entity recognition, semantic embeddings, web deployment, and conversational memory. This document therefore serves as the complete architectural reference for implementing the ALIS chatbot in subsequent development phases.
