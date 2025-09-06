# src/analyze.py
from src import preprocess, features, classifier, skill_parser, recommend

# Load models once
model = classifier.load_classifier("models/resume_classifier.pkl")
vectorizer = features.load_vectorizer("models/vectorizer.pkl")

# Define skills list used in training
skills_list = ['Python', 'Java', 'SQL', 'Machine Learning', 'AWS', 'Data Analysis', 'Excel']

def analyze_resume(resume_text, top_n_jobs=5):
    """
    Input: resume_text (str)
    Output: dictionary with predicted category, skills, recommended jobs
    """
    # 1. Preprocess
    clean_text = preprocess.clean_text(resume_text)
    
    # 2. Vectorize and predict category
    vector = vectorizer.transform([clean_text])
    predicted_category = model.predict(vector)[0]
    
    # 3. Extract skills
    candidate_skills = skill_parser.extract_skills(clean_text, skills_list)
    
    # 4. Recommend jobs
    recommended_jobs = recommend.recommend_jobs(candidate_skills, top_n=top_n_jobs)
    
    return {
        "Predicted Category": predicted_category,
        "Candidate Skills": candidate_skills,
        "Recommended Jobs": recommended_jobs
    }
