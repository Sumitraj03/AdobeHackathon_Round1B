Approach – Round 1B: Persona-Driven Document Intelligence

Overview
Round 1B enhances the outline extraction system by integrating persona-based analysis. It processes multiple PDFs, aligns the extracted content with a user-defined persona and goal, and outputs ranked summaries of the most relevant document sections and subsections. The system is fully offline, lightweight, and optimized for CPU execution.

Methodology

1. Input
PDF Documents: Multiple related files located in the input/ directory.

Persona Configuration: persona.json file containing the persona details and objective (job-to-be-done).

Output: A single JSON file result.json containing metadata, ranked sections, and detailed text snippets in the output/ directory.

2. Outline Extraction
The outline extraction logic identifies key headings (H1, H2, H3) and associated text snippets from each PDF using text-based heuristics:

Capitalization patterns

Short line length thresholds

Contextual grouping of subsequent lines

This structure provides a clean representation of document content regardless of formatting differences.

3. Persona and Goal Analysis
Persona and job descriptions are merged into a single text corpus.

Stopwords are removed, and the remaining words form a keyword set that defines the user’s focus areas.

These keywords serve as the basis for relevance scoring.

4. Relevance Scoring & Ranking
Each extracted heading and its snippet is compared against the keyword set.

A score is assigned based on keyword matches and sections are sorted in descending relevance.

Final JSON includes:

Extracted Sections: Ranked headings with page references.

Sub-Section Details: Supporting text snippets for deeper insights.

5. Performance
Runs fully offline with no network dependencies.

Uses lightweight libraries (PyMuPDF, NLTK) for parsing and NLP.

Executes efficiently on CPU within the time constraints and minimal memory footprint.

Advantages
Modular architecture enabling reuse of previous components.

Persona-driven ranking ensures results are customized to user goals.

Suitable for deployment in constrained environments with minimal setup.