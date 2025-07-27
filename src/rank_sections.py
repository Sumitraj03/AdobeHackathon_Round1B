def score_section(section_text, keywords):
    score = 0
    text_lower = section_text.lower()
    for word in keywords:
        if word.strip(",.") in text_lower:
            score += 1
    return score

def rank_sections(sections, keywords):
    ranked = []
    for sec in sections:
        text_to_score = sec["text"] + " " + sec["content"]
        sec_score = score_section(text_to_score, keywords)

        ranked.append({
            "document": sec.get("filename", ""),
            "page_number": sec["page"],
            "section_title": sec["text"],
            "importance_rank": sec_score,
            "content": sec["content"]
        })

    ranked_sorted = sorted(ranked, key=lambda x: x["importance_rank"], reverse=True)

    for i, sec in enumerate(ranked_sorted, start=1):
        sec["importance_rank"] = i

    return ranked_sorted

if __name__ == "__main__":
    dummy_sections = [
        {"text": "Graph Neural Networks", "page": 2, "content": "Used for drug discovery"},
        {"text": "Introduction", "page": 1, "content": "Basics of AI"},
    ]
    keywords = ["graph", "drug", "networks"]

    result = rank_sections(dummy_sections, keywords)
    print(result)
