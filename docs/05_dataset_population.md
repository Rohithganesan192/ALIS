# Step 5 – Dataset Population

## 5.1 Overview

The objective of this phase is to populate the Assembly Line Information System (ALIS) knowledge base with verified assembly shop knowledge collected during the Hyundai internship. Unlike the previous phases, which focused on software architecture and implementation, this phase focuses on creating the dataset that powers the chatbot.

Each dataset record will follow the schema established in Step 3 and will be written according to the authoring standards, validation rules, and quality criteria previously defined.

---

## 5.2 Objectives

The objectives of this phase are:

- Populate the ALIS knowledge base with verified internship knowledge.
- Maintain consistency across all dataset records.
- Ensure every record follows the dataset schema.
- Validate every record before inclusion.
- Produce a reliable knowledge base for chatbot retrieval.

---

## 5.3 Dataset Population Workflow

Every knowledge record follows the workflow below:

1. Identify knowledge from internship notes.
2. Determine the appropriate category.
3. Draft the record.
4. Validate the record.
5. Add the record to the dataset.
6. Test retrieval using ALIS.
7. Approve the record.

No record is considered complete until it successfully passes validation and retrieval testing.

---

## 5.4 Knowledge Sources

Only verified internship knowledge may be included.

Acceptable sources include:

- Personal internship observations.
- Explanations provided by Hyundai engineers.
- Internship notebook.
- Internship report.
- Official assembly shop procedures observed during training.

Assumptions, internet information, or unverified facts must not be included.

---

## 5.5 Dataset Population Rules

Every record shall satisfy the following requirements:

- Represent exactly one question.
- Provide one complete answer.
- Belong to one category.
- Follow the approved schema.
- Use consistent terminology.
- Be understandable without external context.
- Avoid duplication.
- Maintain factual accuracy.

---

## 5.6 Category Distribution

The target distribution is:

| Category            | Target Records |
| ------------------- | -------------: |
| Safety              |             15 |
| Equipment           |             20 |
| Process             |             25 |
| Quality             |             15 |
| Station             |             15 |
| General Information |             10 |
| **Total**           |        **100** |

This distribution provides balanced coverage across the assembly shop.

---

## 5.7 Validation Process

Before a record is accepted:

- Verify factual correctness.
- Verify category assignment.
- Verify identifier format.
- Check for duplicate knowledge.
- Review wording.
- Test retrieval using ALIS.

Only validated records become part of the production dataset.

---

## 5.8 Expected Outcome

At the end of this phase, the ALIS chatbot will contain approximately 100 verified knowledge records covering the Hyundai assembly shop. These records will serve as the primary knowledge source for answering user questions.
