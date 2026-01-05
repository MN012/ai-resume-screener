from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_docx(path):
    doc = Document(path)
    text = []
    for para in doc.paragraphs:
        if para.text:
            text.append(para.text)
    return " ".join(text)



resume_text = extract_text_docx(
    "pdf/Resumes/Achyuth Resume_8.docx"
)

job_text = extract_text_docx(
    "pdf/Resumes/Ashwini J2EE Developer.docx"
)


# TF-IDF
corpus = [resume_text.lower(), job_text.lower()]
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(corpus)



similarity = cosine_similarity(X[0:1], X[1:2])[0][0]
score = round(float(similarity) * 100, 2)

print(f"Resume match score: {score}%")


if score >= 80.0:
    print("Fit.")
elif score >= 50.0:
    print("Maybe.")
else:
    print("Reject")


features = vectorizer.get_feature_names_out()
resume_vec = X.toarray()[0]
job_vec = X.toarray()[1]

common = []

for i in range(len(features)):
    if resume_vec[i] > 0 and job_vec[i] > 0:
        common.append((features[i], resume_vec[i] + job_vec[i]))

common.sort(key=lambda x: x[1], reverse=True)

print("\nTop matched skills:")
for word, _ in common[:10]:
    print("-", word)
