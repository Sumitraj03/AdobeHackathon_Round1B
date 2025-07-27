import json
import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

def load_persona_keywords(persona_file):
    with open(persona_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    persona_text = data.get("persona", "")
    job_text = data.get("job_to_be_done", "")

    combined_text = (persona_text + " " + job_text).lower()

    stop_words = set(stopwords.words('english'))
    keywords = [word for word in combined_text.split() if word not in stop_words]

    return keywords, persona_text, job_text

if __name__ == "__main__":
    test_file = "../input/persona.json"
    keywords, persona, job = load_persona_keywords(test_file)
    print("Persona:", persona)
    print("Job:", job)
    print("Keywords:", keywords)
