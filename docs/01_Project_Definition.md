# Assembly Line Information System (ALIS)

## Project Definition

---

# 1. Problem Statement

## 1.1 Background

Automobile assembly shops operate as high-throughput, safety-critical environments where multiple stations, machines, and personnel must coordinate within tight time constraints (takt time). New operators, trainees, interns, and even visiting staff frequently require quick and accurate access to information regarding procedures, safety rules, equipment usage, workflows, and role responsibilities. In practice, this information is scattered across manuals, Standard Operating Procedures (SOPs), verbal instructions from supervisors, and informal on-floor knowledge possessed by experienced workers.

## 1.2 Existing Problem

This creates a recurring problem: first-time or unfamiliar users—such as new operators, interns, and trainees—cannot easily obtain answers to practical, everyday questions. Examples include:

- What safety gear is required at the welding station?
- What is the correct sequence for the door-fitting process?
- What is the responsibility of a line supervisor?
- What tools are used at a particular workstation?

Instead of obtaining information quickly, users are often forced to:

- Interrupt supervisors or senior operators.
- Search lengthy manuals and SOP documents.
- Depend on informal verbal explanations.

This approach is inefficient, inconsistent, and, in a safety-critical environment, increases the risk of misunderstanding or incomplete knowledge transfer.

## 1.3 Causes of the Problem

The problem exists primarily because:

- Assembly-shop documentation is written for reference rather than conversational lookup.
- Domain knowledge is distributed across multiple independent sources such as safety manuals, process sheets, role charts, and KPI documents.
- Supervisors and experienced operators cannot continually answer repetitive questions while maintaining production responsibilities.
- New users are unfamiliar with the technical terminology used in official documentation, making keyword searches and traditional FAQ systems ineffective.

## 1.4 Impact

The lack of an accessible knowledge source affects several groups:

- New operators and trainees require rapid onboarding support.
- Interns and students need simplified explanations of assembly-shop concepts.
- Supervisors spend valuable time answering repetitive operational questions.
- Overall knowledge sharing becomes slower and less consistent.
- Incorrect or incomplete information may negatively affect safety and operational efficiency.

## 1.5 Proposed Solution

The **Assembly Line Information System (ALIS)** addresses this challenge through a Natural Language Processing (NLP)-based chatbot that enables users to ask questions in their own words rather than relying on fixed keywords or predefined FAQ menus.

Unlike traditional document searches, ALIS interprets natural-language questions and retrieves the most relevant information from a developer-curated assembly-shop dataset. All responses are grounded exclusively in the developer-provided knowledge base, ensuring consistency while preventing unsupported or fabricated information.

The chatbot serves as a centralized knowledge assistant for first-time and unfamiliar users, providing accurate information about:

- Assembly procedures
- Safety rules
- Equipment
- Workflows
- Roles and responsibilities
- General assembly-shop terminology

---

# 2. Project Objectives

## 2.1 Primary Objective

To design and implement a Natural Language Processing (NLP)-based chatbot capable of understanding natural-language questions related to automobile assembly-shop procedures, safety rules, equipment, workflows, and personnel roles, and retrieving accurate responses exclusively from a developer-curated dataset without relying on a fixed Frequently Asked Questions (FAQ) structure.

## 2.2 Secondary Objectives

### 2.2.1 Dataset Construction

Develop a structured assembly-shop dataset containing information related to procedures, safety rules, equipment, workflows, personnel roles, and general terminology. The dataset will serve as the chatbot's only knowledge source.

### 2.2.2 Text Preprocessing Pipeline

Implement a preprocessing pipeline capable of preparing both dataset entries and user queries through operations such as:

- Lowercase conversion
- Tokenization
- Punctuation removal
- Stop-word removal
- Lemmatization (where appropriate)

### 2.2.3 Intent Understanding

Develop a lightweight mechanism capable of identifying the user's information need, such as safety-related questions, equipment queries, workflow queries, or role-related questions, using beginner-friendly NLP techniques.

### 2.2.4 Retrieval-Based Question Answering

Design a retrieval mechanism that identifies the most relevant dataset entry using similarity-based techniques such as TF-IDF and Cosine Similarity.

### 2.2.5 Robustness to Query Variations

Enable the chatbot to understand multiple phrasings of similar questions without requiring users to match the wording used in the dataset.

### 2.2.6 System Evaluation

Create a repeatable evaluation methodology using manually prepared test questions, expected responses, and performance measurements to assess chatbot quality objectively.

### 2.2.7 Documentation and Reproducibility

Prepare comprehensive documentation describing:

- Project architecture
- Dataset design
- NLP pipeline
- Installation process
- Usage instructions
- Future enhancement possibilities

---

# 3. Target Users

ALIS is primarily intended for users who have limited familiarity with an automobile assembly shop and require quick, reliable access to assembly-related information.

## 3.1 Primary Users

### 3.1.1 New Operators and Trainees

New operators require immediate access to information about safety practices, work procedures, equipment usage, and assembly sequences. ALIS allows them to obtain this information without repeatedly depending on supervisors.

### 3.1.2 Interns and Student Trainees

Students undergoing industrial training generally have limited knowledge of assembly-shop terminology and workflows. ALIS provides simplified explanations that support self-learning throughout the internship period.

### 3.1.3 Rotating or Temporary Shop-Floor Staff

Employees assigned to unfamiliar workstations can quickly learn station-specific procedures, equipment, and safety requirements without consulting extensive documentation.

## 3.2 Secondary Users

### 3.2.1 Supervisors and Senior Operators

Supervisors benefit by reducing the number of repetitive questions they receive from new workers. They may also use the chatbot as a quick reference tool.

### 3.2.2 Safety and Compliance Officers

Safety personnel can verify whether safety-related information presented by the chatbot remains accurate and consistent with the developer-provided dataset.

### 3.2.3 Academic Evaluators

Faculty members, project reviewers, and placement interviewers can use ALIS to evaluate the chatbot's NLP capabilities, system design, and overall project quality.

### 3.2.4 Visitors

Visitors unfamiliar with assembly-shop operations can ask simple questions to understand basic processes, equipment, and safety practices during guided visits.

## 3.3 Target User Summary

| User Group                       | Category  | Primary Purpose                                |
| -------------------------------- | --------- | ---------------------------------------------- |
| New Operators and Trainees       | Primary   | Learn assembly procedures and safety practices |
| Interns and Student Trainees     | Primary   | Understand assembly-shop concepts              |
| Rotating or Temporary Staff      | Primary   | Learn unfamiliar workstations                  |
| Supervisors and Senior Operators | Secondary | Quick reference and reduced repetitive queries |
| Safety and Compliance Officers   | Secondary | Verify safety information                      |
| Academic Evaluators              | Secondary | Assess project capabilities                    |
| Visitors                         | Secondary | Learn basic assembly-shop information          |

---

# 4. Project Scope

The scope of the Assembly Line Information System (ALIS) defines the features and functionalities included in the current version of the project, as well as those intentionally excluded. Clearly defining the scope ensures that the project remains achievable within the available development timeline while focusing on the primary objective of developing a retrieval-based NLP chatbot.

---

## 4.1 In Scope

The following functionalities are included in Version 1 of ALIS.

### 4.1.1 Dataset

The chatbot will use a developer-curated dataset created from knowledge acquired during a 15-day automobile assembly-shop internship.

The dataset will:

- Be stored in CSV or JSON format.
- Contain approximately **80–120 entries**.
- Cover **4–6 major assembly-shop categories**, including:
  - Safety Rules
  - Assembly Procedures
  - Equipment
  - Roles and Responsibilities
  - Workflow
  - General Assembly-Shop Information

---

### 4.1.2 Text Preprocessing

The NLP preprocessing pipeline will prepare both user queries and dataset entries before retrieval.

The preprocessing operations include:

- Lowercase conversion
- Punctuation removal
- Tokenization
- Stop-word removal
- Lemmatization or stemming (where applicable)

---

### 4.1.3 Information Retrieval

The chatbot will:

- Accept natural-language questions.
- Compare user queries with the developer-created dataset.
- Retrieve the most relevant answer using **TF-IDF Vectorization** and **Cosine Similarity**.
- Return responses exclusively from the dataset.
- Display a predefined fallback message if no relevant answer is found.

---

### 4.1.4 User Interaction

The chatbot will support:

- Command Line Interface (CLI)
- Single-turn conversations
- Natural-language question answering
- Consistent responses for identical queries

---

### 4.1.5 Evaluation

The project includes:

- Manual testing using predefined test questions.
- Testing with paraphrased user queries.
- Performance measurement based on retrieval accuracy and response time.

---

### 4.1.6 Documentation

Complete project documentation will include:

- Project Definition
- System Architecture
- Dataset Design
- NLP Pipeline
- Installation Guide
- User Guide
- GitHub Documentation

---

## 4.2 Out of Scope

The following features are intentionally excluded from Version 1.

### 4.2.1 Advanced NLP

The project will not include:

- Large Language Models (LLMs)
- Deep Learning models
- Transformer-based models
- Fine-tuned language models
- Named Entity Recognition (NER)
- Sentiment Analysis

---

### 4.2.2 Advanced Chatbot Features

The chatbot will not support:

- Multi-turn conversations
- Conversation memory
- Context tracking
- Personalized responses
- Voice input
- Voice output
- Spell correction
- Grammar correction
- Multilingual support

---

### 4.2.3 External Knowledge Sources

The chatbot will not:

- Access the Internet
- Use ChatGPT, Gemini, Claude, or other AI APIs
- Retrieve information from Wikipedia
- Access company databases
- Generate responses beyond the developer-provided dataset

---

### 4.2.4 Deployment

The current version does not include:

- Cloud deployment
- Docker
- Authentication
- Multi-user support
- Database servers
- Production deployment

These features are reserved for future versions.

---

## 4.3 Future Enhancements

Potential improvements include:

- Semantic Search using Sentence Transformers
- Intent Classification
- Named Entity Recognition
- Web Interface
- REST API using Flask or FastAPI
- Multi-turn conversations
- Voice interaction
- Expanded assembly-shop dataset
- Performance optimization

---

## Scope Summary

| Included (Version 1)       | Excluded (Future Work)     |
| -------------------------- | -------------------------- |
| Developer-created dataset  | External knowledge sources |
| TF-IDF Retrieval           | Deep Learning              |
| Cosine Similarity          | Large Language Models      |
| Text Preprocessing         | Multi-turn conversations   |
| CLI Interface              | Voice Interaction          |
| Manual Evaluation          | Cloud Deployment           |
| Single-turn QA             | Named Entity Recognition   |
| Dataset-grounded responses | Production Integration     |

---

# 5. Functional Requirements

Functional requirements describe the core capabilities that ALIS must provide. They define **what** the chatbot should do without specifying **how** it is implemented.

| ID   | Functional Requirement       | Description                                                                                                                          |
| ---- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| FR-1 | Natural Language Query Input | The chatbot shall accept user questions written in free-form natural language through a Command Line Interface (CLI).                |
| FR-2 | Text Preprocessing           | The chatbot shall preprocess user queries before information retrieval using NLP preprocessing techniques.                           |
| FR-3 | Dataset-Grounded Retrieval   | The chatbot shall retrieve answers exclusively from the developer-provided dataset.                                                  |
| FR-4 | Query Matching               | The chatbot shall identify relevant responses even when users ask similar questions using different wording.                         |
| FR-5 | Multi-Category Support       | The chatbot shall answer questions related to safety, procedures, equipment, workflow, roles, and general assembly-shop information. |
| FR-6 | Fallback Response            | The chatbot shall display an appropriate fallback message whenever a suitable answer cannot be found.                                |
| FR-7 | Single-Turn Interaction      | The chatbot shall process each query independently without remembering previous conversations.                                       |
| FR-8 | Consistent Responses         | The chatbot shall return the same response for identical user queries to ensure deterministic behavior.                              |

---

## Functional Requirement Summary

Version 1 of ALIS focuses on providing reliable, single-turn, retrieval-based question answering using a developer-created knowledge base. The chatbot emphasizes accuracy, consistency, and dataset-grounded responses while intentionally excluding advanced conversational capabilities.

---

# 6. Non-Functional Requirements

Non-functional requirements define the quality attributes of ALIS. They describe **how well** the chatbot should perform.

| ID    | Non-Functional Requirement | Description                                                                                                                                          |
| ----- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NFR-1 | Performance                | The chatbot shall respond within **3 seconds** for at least **95%** of valid queries on a standard student laptop.                                   |
| NFR-2 | Usability                  | The chatbot shall provide a simple and user-friendly Command Line Interface with clear prompts and readable responses.                               |
| NFR-3 | Maintainability            | The source code shall be organized into modular components to simplify maintenance and future enhancements.                                          |
| NFR-4 | Scalability                | The system shall support future expansion of the dataset to approximately **150–200 entries** without major architectural modifications.             |
| NFR-5 | Reliability                | The chatbot shall always return either a relevant answer or a fallback message without crashing.                                                     |
| NFR-6 | Portability                | The chatbot shall execute on any computer with Python 3.x and the required dependencies installed, without requiring internet access during runtime. |

---

## Non-Functional Requirement Summary

The non-functional requirements ensure that ALIS remains lightweight, reliable, maintainable, portable, and suitable for academic demonstrations. Since the project targets a beginner-friendly implementation running on a standard student laptop, emphasis is placed on simplicity, modularity, and deterministic behavior rather than production-scale performance.

---

# 7. Project Constraints

Project constraints define the limitations and boundaries within which the Assembly Line Information System (ALIS) is designed, developed, and evaluated. These constraints influence the project's design decisions, implementation strategy, and achievable outcomes.

---

## 7.1 Time Constraints

The project is planned to be completed within approximately **5–6 days**.

Development is divided into two phases:

- **Zone 1 – NLP Core**
- **Zone 2 – Application Layer**

The NLP Core must be completed, tested, and validated before beginning the application layer. Due to the limited development timeline, only one major implementation and refinement cycle is planned.

---

## 7.2 Dataset Constraints

The chatbot relies entirely on a **developer-created dataset** based on knowledge acquired during a **15-day automobile assembly-shop internship**.

Dataset constraints include:

- No external datasets will be used.
- No company confidential documents will be included.
- No internet-based information will be added.
- Approximately **80–120 entries** distributed across **4–6 assembly-shop categories**.
- The dataset represents a prototype knowledge base rather than a complete industrial knowledge repository.

---

## 7.3 Hardware Constraints

Development and testing will be performed on a standard student laptop.

Hardware limitations include:

- No GPU available.
- Moderate system resources.
- Local execution only.
- No cloud computing infrastructure.

The system must operate efficiently without requiring specialized hardware.

---

## 7.4 Software Constraints

The project will be developed using:

- Python 3.x
- Visual Studio Code
- Git and GitHub
- Standard Python virtual environments

Additional software constraints include:

- Offline execution during runtime.
- No paid APIs.
- No cloud AI services.
- Lightweight NLP libraries only.
- Beginner-friendly implementation.

---

## 7.5 Developer Constraints

The project is developed by a single undergraduate student.

Developer-related constraints include:

- Beginner-level knowledge of NLP and Machine Learning.
- Limited project duration.
- Primary focus on learning and understanding NLP concepts.
- Independent implementation with mentor guidance.

---

## 7.6 NLP Constraints

The chatbot follows a retrieval-based NLP approach.

Known NLP limitations include:

- Retrieval depends on textual similarity.
- No semantic reasoning beyond implemented techniques.
- No conversational memory.
- No multilingual support.
- No spelling correction.
- No voice processing.

These limitations are acceptable for the current academic prototype and will be considered for future enhancements.

---

## Constraint Summary

| Constraint Category | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| Time                | 5–6 day development timeline                                   |
| Dataset             | Developer-created dataset (80–120 entries)                     |
| Hardware            | Standard student laptop without GPU                            |
| Software            | Python, VS Code, Offline Execution                             |
| Developer           | Single beginner NLP developer                                  |
| NLP                 | Retrieval-based chatbot with limited conversational capability |

---

# 8. Project Assumptions

Project assumptions define the conditions considered to be true throughout the design and development of ALIS. These assumptions provide the foundation for architectural and implementation decisions.

---

## 8.1 Dataset Assumptions

The project assumes that:

- The developer-created dataset accurately represents assembly-shop knowledge.
- Every question has one correct and unambiguous answer.
- The dataset is written entirely in English.
- Information is categorized consistently.
- The dataset will be maintained as the project grows.

---

## 8.2 User Assumptions

It is assumed that:

- Users can communicate using simple English.
- Users ask one question at a time.
- Users interact through text input.
- Users seek genuine information rather than attempting malicious interactions.

---

## 8.3 Hardware Assumptions

The system assumes:

- Execution on a standard student laptop.
- Single-user interaction.
- Sufficient memory and storage for local execution.

---

## 8.4 Software Assumptions

The project assumes:

- Python 3.x is installed.
- Required libraries can be installed successfully.
- A dedicated Python virtual environment is used.
- Internet access is unnecessary after dependency installation.

---

## 8.5 Usage Environment Assumptions

The project assumes:

- ALIS is used for academic learning.
- The chatbot is demonstrated in a controlled environment.
- Users understand that responses are limited to the developer-created dataset.
- Sessions consist of independent question-answer interactions.

---

## Assumption Summary

| Assumption Category | Description                               |
| ------------------- | ----------------------------------------- |
| Dataset             | Accurate developer-created dataset        |
| Users               | Text-based single-question interaction    |
| Hardware            | Standard student laptop                   |
| Software            | Python environment with offline execution |
| Usage Environment   | Academic prototype                        |

---

# 9. Success Criteria

Success criteria define measurable indicators used to determine whether ALIS satisfies its objectives and requirements.

---

## Success Criteria Table

| ID   | Success Criterion     | Target                 | Measurement Method                                                                               |
| ---- | --------------------- | ---------------------- | ------------------------------------------------------------------------------------------------ |
| SC-1 | Retrieval Accuracy    | ≥ 75%                  | Compare chatbot responses with expected answers using a prepared test dataset.                   |
| SC-2 | Category Coverage     | 100%                   | Verify that each assembly-shop category is represented by at least one correctly answered query. |
| SC-3 | Paraphrase Robustness | ≥ 60%                  | Test paraphrased user questions and evaluate successful retrieval.                               |
| SC-4 | Fallback Correctness  | 100%                   | Ensure unknown questions always produce the predefined fallback response.                        |
| SC-5 | Response Consistency  | 100%                   | Execute identical queries multiple times and compare outputs.                                    |
| SC-6 | Response Time         | ≤ 3 Seconds            | Measure execution time for each query on the development system.                                 |
| SC-7 | System Stability      | 0 Unhandled Exceptions | Test normal and edge-case inputs to ensure stable execution.                                     |
| SC-8 | Dataset Groundedness  | 100%                   | Verify that all responses originate from the developer-created dataset.                          |

---

## Evaluation Methodology

The chatbot will be evaluated using a manually prepared test set consisting of:

- Standard user queries
- Paraphrased questions
- Unknown questions
- Edge-case inputs
- Empty inputs
- Long queries
- Special-character inputs

Each response will be compared with the expected output to determine whether the corresponding success criterion has been achieved.

---

## Success Criteria Summary

| Evaluation Area      | Target         |
| -------------------- | -------------- |
| Retrieval Accuracy   | ≥ 75%          |
| Category Coverage    | All Categories |
| Paraphrase Handling  | ≥ 60%          |
| Fallback Response    | 100%           |
| Response Consistency | 100%           |
| Response Time        | ≤ 3 Seconds    |
| Crash Rate           | 0              |
| Dataset Groundedness | 100%           |

---

# 10. Project Overview

## 10.1 Introduction

The **Assembly Line Information System (ALIS)** is a Natural Language Processing (NLP)-based chatbot designed to assist first-time or unfamiliar users in understanding automobile assembly-shop operations. The system enables users to ask questions in natural language and retrieves relevant information exclusively from a developer-created assembly-shop dataset without relying on external knowledge sources.

ALIS combines real-world industrial exposure with practical NLP concepts. The project is inspired by a **15-day internship in an automobile assembly shop** and aims to transform the acquired domain knowledge into an intelligent, retrieval-based information system.

The primary objective of the project is not only to build a chatbot but also to gain practical experience in Natural Language Processing by designing, implementing, evaluating, and improving every major component of the NLP pipeline.

---

## 10.2 Problem Overview

Knowledge within an automobile assembly shop is often distributed across multiple sources, including:

- Standard Operating Procedures (SOPs)
- Safety manuals
- Equipment documentation
- Workflow charts
- Supervisor guidance
- Practical experience of senior operators

New operators, interns, trainees, and visitors frequently struggle to obtain information quickly because they may not know the technical terminology or documentation structure.

Consequently, they often depend on supervisors for repetitive questions, resulting in:

- Increased onboarding time
- Reduced operational efficiency
- Inconsistent knowledge sharing
- Potential safety risks due to incorrect or incomplete information

ALIS addresses this problem by providing a centralized knowledge assistant capable of understanding natural-language questions and retrieving accurate responses from a structured dataset.

---

## 10.3 Project Objectives

The primary objective of ALIS is to design and implement a retrieval-based NLP chatbot capable of understanding user questions and retrieving accurate responses exclusively from a developer-created assembly-shop dataset.

The project also aims to:

- Build a structured assembly-shop knowledge base.
- Understand the complete NLP pipeline.
- Learn text preprocessing techniques.
- Implement information retrieval using TF-IDF and Cosine Similarity.
- Evaluate chatbot performance through systematic testing.
- Produce well-organized technical documentation.

---

## 10.4 Target Users

### Primary Users

- New Operators and Trainees
- Interns and Student Trainees
- Rotating or Temporary Shop-Floor Staff

### Secondary Users

- Supervisors and Senior Operators
- Safety and Compliance Officers
- Academic Evaluators
- Visitors

These user groups represent individuals requiring quick access to assembly-shop knowledge without depending entirely on experienced personnel.

---

## 10.5 Development Approach

The development of ALIS follows a structured, incremental methodology.

### Phase 1 – Project Planning

- Requirements gathering
- Problem analysis
- Scope definition
- System planning

### Phase 2 – System Design

- System architecture
- Dataset design
- NLP pipeline design
- Module planning

### Phase 3 – NLP Core Development

- Dataset preparation
- Text preprocessing
- Feature extraction
- TF-IDF vectorization
- Cosine similarity calculation
- Response retrieval

### Phase 4 – Application Development

- Command Line Interface (CLI)
- User interaction
- Integration of NLP modules

### Phase 5 – Testing and Evaluation

- Functional testing
- Retrieval accuracy testing
- Edge-case testing
- Performance evaluation

### Phase 6 – Documentation

- Technical documentation
- GitHub repository
- Project report
- Installation guide
- User manual

---

## 10.6 Technology Stack

The project uses lightweight, beginner-friendly technologies to ensure clarity, maintainability, and ease of learning.

| Category             | Technology                 |
| -------------------- | -------------------------- |
| Programming Language | Python 3.x                 |
| IDE                  | Visual Studio Code         |
| Version Control      | Git                        |
| Repository Hosting   | GitHub                     |
| Data Storage         | CSV / JSON                 |
| Data Processing      | pandas                     |
| Numerical Computing  | NumPy                      |
| NLP                  | NLTK                       |
| Machine Learning     | scikit-learn               |
| Retrieval Method     | TF-IDF + Cosine Similarity |
| Documentation        | Markdown                   |

---

## 10.7 Expected Deliverables

Upon completion, ALIS will include:

- Developer-created assembly-shop dataset
- Retrieval-based NLP chatbot
- Text preprocessing pipeline
- TF-IDF retrieval engine
- Command Line Interface
- Complete project documentation
- Testing and evaluation reports
- GitHub repository

---

## 10.8 Expected Outcomes

The successful completion of ALIS is expected to provide:

### Academic Outcomes

- Practical understanding of Natural Language Processing concepts.
- Experience in designing and implementing an NLP application.
- Strong major project documentation.

### Technical Outcomes

- Modular chatbot architecture.
- Well-organized assembly-shop knowledge base.
- Lightweight retrieval-based question-answering system.
- Reusable NLP components for future enhancement.

### Professional Outcomes

The project will serve as a portfolio project demonstrating:

- Software engineering practices
- NLP implementation skills
- Documentation quality
- Problem-solving ability
- Real-world application of internship experience

These outcomes will strengthen the developer's profile for internships, placements, and future NLP-based projects.

---

## 10.9 Current Project Status

**Current Phase:** Project Definition Completed

### Completed

- Problem Definition
- Objectives
- Target Users
- Scope Definition
- Functional Requirements
- Non-Functional Requirements
- Constraints
- Assumptions
- Success Criteria
- Project Overview

### Upcoming

- System Architecture
- Dataset Design
- NLP Pipeline Design
- Project Structure
- Implementation
- Testing
- Evaluation
- GitHub Documentation

---

## 10.10 Conclusion

The Assembly Line Information System (ALIS) is designed as a retrieval-based NLP chatbot that demonstrates the practical application of Natural Language Processing within the context of an automobile assembly shop. By combining structured dataset design, text preprocessing, similarity-based retrieval, and systematic evaluation, the project aims to provide an accessible knowledge source for first-time users while enabling the developer to gain a strong understanding of fundamental NLP concepts.

Although the current version focuses on a lightweight and beginner-friendly implementation, the modular architecture allows future enhancements such as semantic search, intent classification, named entity recognition, and web-based deployment. Consequently, ALIS serves as both an academic learning project and a professional portfolio project that reflects real-world industrial experience.
