import pandas as pd
from src import preprocess, features, classifier, recommend

# -----------------------
# 1. Load the Excel dataset
# -----------------------

import pandas as pd

data_path = "data/resume_dataset.csv"
data = pd.read_csv(data_path)

print(data.head())  # Check the first few rows


print("Dataset Sample:\n", data.head())

# -----------------------
# 2. Preprocess resume texts
# -----------------------
resume_texts = [preprocess.clean_text(text) for text in data['Resume']]

# -----------------------
# 3. Feature extraction
# -----------------------
X, vectorizer = features.create_tfidf_features(resume_texts, save_path="models/vectorizer.pkl")

# -----------------------
# 4. Train classifier
# -----------------------
y = data['Category']
model = classifier.train_classifier(X, y, save_path="models/resume_classifier.pkl")

# -----------------------
# 5. Example: Predict a new resume
# -----------------------
new_resume_text = "Experienced in Python, SQL, and Machine Learning with 2 years in Data Science"
new_text = preprocess.clean_text(new_resume_text)
new_vector = vectorizer.transform([new_text])
pred_category = model.predict(new_vector)[0]

# Example skills extraction and job recommendation
skills_list = ['Python', 'Java', 'SQL', 'Machine Learning', 'AWS', 'Data Analysis', 'Excel']
from src import skill_parser  # For extract_skills function
candidate_skills = skill_parser.extract_skills(new_text, skills_list)
recommended_jobs = recommend.recommend_jobs(candidate_skills)

print("\n--- New Resume Analysis ---")
print("Predicted Category:", pred_category)
print("Candidate Skills:", candidate_skills)
print("Recommended Jobs:", recommended_jobs)
