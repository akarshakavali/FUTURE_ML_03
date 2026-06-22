import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load resumes
with open("../data/resumes.txt", "r") as f:
    resumes = f.readlines()

# Job description
job_desc = ["Python developer with NLP machine learning pandas"]

# Combine
documents = resumes + job_desc

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

# Similarity
similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

scores = similarity[0]

results = pd.DataFrame({
    "Resume": resumes,
    "Score": scores
})

results = results.sort_values(by="Score", ascending=False)

print("\n=== Candidate Ranking ===\n")
print(results)
job_skills = set(job_desc[0].lower().split())

def missing_skills(resume):
    res_skills = set(resume.lower().split())
    return job_skills - res_skills

results["Missing Skills"] = results["Resume"].apply(missing_skills)

print("\n=== Final Output ===\n")
print(results)