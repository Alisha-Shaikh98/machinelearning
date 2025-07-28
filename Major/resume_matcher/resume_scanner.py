from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open (pdf_path,'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ' '
        for page in reader.pages:
            text += page.extract_text()
    return text

model = SentenceTransformer('all-MiniLM-L6-V2')

def get_embeddings(text):
    return model.encode(text,convert_to_tensor = True)

def get_similarity(resume_text, job_desc_text):
    resume_embedding = get_embeddings(resume_text)
    job_desc_embedding = get_embeddings(job_desc_text)
    score = util.pytorch_cos_sim(resume_embedding, job_desc_embedding).item()
    return score


resume = """
I hate working with python.
"""

job_desc = """
Required strong python skills.
"""

print("Similarity Score: ",get_similarity(resume,job_desc))