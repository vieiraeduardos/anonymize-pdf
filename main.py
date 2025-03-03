import fitz
import spacy
import re

nlp = spacy.load("pt_core_news_sm")

def clean(text):
    return re.sub(r"[^\w]", "", text)

def anonimizar_pdf(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_instances = page.get_text("words")

        for word in text_instances:
            texto = word[4]
            bbox = fitz.Rect(word[:4])  # Coordenadas da palavra (x0, y0, x1, y1)
            
            texto = clean(texto)

            if texto:
                doc_nlp = nlp(texto)
                for ent in doc_nlp.ents:
                    if ent.label_ == "PER": 
                        page.draw_rect(bbox, color=(0, 0, 0), fill=(0, 0, 0))
        
    doc.save(output_pdf)
    doc.close()

input_pdf = "file.pdf"
output_pdf = "output.pdf"

anonimizar_pdf(input_pdf, output_pdf)
