import pandas as pd

def recommend_jobs(skills, top_n=5):
    jobs_df = pd.read_csv("data/jobs.csv")
    
    recommendations = []
    for _, row in jobs_df.iterrows():
        job_skills = row['Required Skills'].split(", ")
        score = len(set(skills) & set(job_skills))
        if score > 0:
            recommendations.append((row['Job Title'], score))
    
    # Sort by score
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]