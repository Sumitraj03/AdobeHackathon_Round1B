# Persona-Driven Document Intelligence (Round 1B)

This project extends a PDF outline extraction system to implement persona-driven document intelligence. It processes multiple PDFs, understands the defined persona and objective, and outputs ranked summaries of relevant sections and subsections.

---
```
## Project Structure

round1b/
│
├── input/                # Input PDFs and persona.json
│   ├── sample.pdf
│   ├── sample2.pdf
│   └── persona.json
│
├── output/               # Output JSON (generated after run)
│   └── result.json
│
├── src/                  # Core logic
│   ├── extract_outline.py
│   ├── persona_analysis.py
│   ├── rank_sections.py
│   └── main.py
│
├── approach_explanation.md
├── requirements.txt
└── Dockerfile
```
---

## Input Format

### PDF Files
Place 3–10 related PDFs in the input/ folder.

### Persona JSON
Create persona.json inside the input/ folder:
```
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"
}
```
---

## Output Format

The program generates output/result.json containing:

- Metadata: Documents, persona, job, timestamp.
- Extracted Sections: Ranked headings relevant to persona.
- Sub-Section Analysis: Contextual snippets for deeper insights.

### Example Output
```
{
  "metadata": {
    "documents": ["sample.pdf", "sample2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks",
    "timestamp": "2025-07-25T12:30:00"
  },
  "extracted_sections": [
    {
      "document": "sample.pdf",
      "page_number": 2,
      "section_title": "Introduction to Graph Neural Networks",
      "importance_rank": 1
    }
  ],
  "sub_section_analysis": [
    {
      "document": "sample.pdf",
      "page_number": 2,
      "refined_text": "This section describes methodologies such as message passing and pooling layers used in GNNs..."
    }
  ]
}
```
---

## Running Locally
```
cd round1b
pip install -r requirements.txt
cd src
python main.py
```
Output is saved to round1b/output/result.json.

---

## Running with Docker

### Build Image
```
docker build --platform linux/amd64 -t pdf-intelligence-1b .
```
### Run Container
```
docker run --rm -v "${PWD}/input:/app/input" -v "${PWD}/output:/app/output" pdf-intelligence-1b
```
Result is saved to round1b/output/result.json.

---

## Key Features

- Extracts structured outlines (H1–H3) and contextual snippets.
- Persona-driven ranking of relevant sections.
- Lightweight and offline (CPU-only).
- Fully containerized for consistent execution.

