import os
import json
from datetime import datetime

from extract_outline import extract_outline_from_pdf
from persona_analysis import load_persona_keywords
from rank_sections import rank_sections

def main():
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../input"))
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../output"))
    persona_file = os.path.join(input_dir, "persona.json")

    keywords, persona_text, job_text = load_persona_keywords(persona_file)

    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    all_ranked_sections = []

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)

        outline_data = extract_outline_from_pdf(pdf_path)

        for sec in outline_data["sections"]:
            sec["filename"] = pdf_file

        ranked = rank_sections(outline_data["sections"], keywords)
        all_ranked_sections.extend(ranked)

    metadata = {
        "documents": pdf_files,
        "persona": persona_text,
        "job_to_be_done": job_text,
        "timestamp": datetime.now().isoformat()
    }

    extracted_sections = [
        {
            "document": sec["document"],
            "page_number": sec["page_number"],
            "section_title": sec["section_title"],
            "importance_rank": sec["importance_rank"]
        }
        for sec in all_ranked_sections
    ]

    sub_section_analysis = [
        {
            "document": sec["document"],
            "page_number": sec["page_number"],
            "refined_text": sec["content"]
        }
        for sec in all_ranked_sections
    ]

    result = {
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    }

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "result.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"Output saved to {output_path}")

if __name__ == "__main__":
    main()
