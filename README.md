# AI Resume Screener

A CLI-based AI resume screening tool that compares a resume against a job description using NLP.

## Features
- DOCX resume parsing
- TF-IDF vectorization
- Cosine similarity scoring
- Match classification (Fit / Maybe / Reject)
- Top overlapping skill extraction

## Tech Stack
- Python
- scikit-learn
- python-docx

## How it works
1. Resume and job description are converted to text
2. Text is vectorized using TF-IDF
3. Cosine similarity produces a match score
4. Shared high-importance keywords are extracted

## How to run
```bash
pip install -r requirements.txt
python madness.py
