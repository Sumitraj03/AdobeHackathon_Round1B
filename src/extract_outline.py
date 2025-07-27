import fitz  # PyMuPDF
import os
import re

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    filename = os.path.basename(pdf_path)

    title = doc.metadata.get("title")
    if not title:
        first_page_text = doc[0].get_text().split("\n")[0]
        title = first_page_text.strip()

    sections = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        lines = text.split("\n")

        for line in lines:
            line_stripped = line.strip()

            if re.match(r"^[A-Z][A-Za-z\s]{2,}$", line_stripped) and len(line_stripped.split()) <= 10:
                if len(line_stripped.split()) <= 3:
                    level = "H1"
                elif len(line_stripped.split()) <= 6:
                    level = "H2"
                else:
                    level = "H3"

                index = lines.index(line)
                snippet_lines = lines[index + 1:index + 6]
                snippet_text = " ".join(snippet_lines).strip()

                sections.append({
                    "level": level,
                    "text": line_stripped,
                    "page": page_num,
                    "content": snippet_text
                })

    outline_data = {
        "filename": filename,
        "title": title,
        "sections": sections
    }

    return outline_data

if __name__ == "__main__":
    test_pdf = "../input/sample.pdf"
    data = extract_outline_from_pdf(test_pdf)
    print(data)
