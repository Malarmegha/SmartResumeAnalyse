from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    """Extract keywords from text using spaCy."""
    doc = nlp(text)
    keywords = set(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)
    return keywords

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = request.form['resume']
    job_description_text = request.form['job_description']
    
    resume_keywords = extract_keywords(resume_text)
    job_description_keywords = extract_keywords(job_description_text)
    
    matches = resume_keywords.intersection(job_description_keywords)
    
    return render_template('index.html', matches=matches, resume_keywords=resume_keywords, job_description_keywords=job_description_keywords)

if __name__ == '__main__':
    app.run(debug=True)
