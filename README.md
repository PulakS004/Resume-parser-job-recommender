



## 📄 Resume Parser & Job Recommender

A machine learning–based system to automate resume screening and provide personalized job recommendations.
This project uses TF–IDF Vectorization for text feature extraction and a Logistic Regression classifier for resume categorization.
## Features

- **Resume Categorization** → Classifies resumes into predefined categories (e.g., Data Science, Java Developer, HR).
- **Skill Extraction** → Extracts skills from resumes using simple NLP and regex-based matching.
- **Job Recommendation** → Suggests relevant job roles based on extracted skills and predicted category.



## Installation & Set-up

Clone the repository

```bash
  git clone https://github.com/PulakS004/Resume-parser-job-recommender.git
  cd Resume-parser-job-recommender
```

Install dependencies

```bash
    pip install -r requirements.txt
```  

Add dataset

Download the [Resume dataset from Kaggle ↗](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)
Place it in the data/ folder as resume_dataset.csv.

**Train the model**

```bash
    python -m src.main
```  









## Notes

- `jobs.csv` is required for job recommendations and is **not included** in the repo to keep it lightweight.  
- Users should create this CSV themselves with two columns: `Job Title` and `Required Skills` (comma-separated).  
- Make sure all categories from your `resume_dataset.csv` exist in `jobs.csv` for proper recommendations.

## Testing with a resume

In src/test_resume.py :

```bash
    from src.analyze import analyze_resume

    test_resume = """
    Software Engineer with 5+ years     of experience in Java, Spring     Boot,
    MySQL, and AWS. Skilled in REST     API development and Docker.
    """

    result = analyze_resume (test_resume)
    print("Predicted Category:", result["category"])
    print("Extracted Skills:", result ["skills"])
    print("Recommended Jobs:", result ["recommended_jobs"])

```  

Run

```bash
    python -m src.main
``` 

**Example output**:
```bash
  Predicted Category: Java Developer
  Extracted Skills: ['Java',  'Spring Boot', 'MySQL', 'AWS', 'Docker']
  Recommended Jobs: ['Java Developer', 'Database', 'DevOps Engineer']
``` 

## Demo

**Input Resume text**:

![Resume Parser Job Recommender Input](https://github.com/user-attachments/assets/283cdc6a-6d8c-42a2-9d12-ffbb79db098d)



**Output**:

![Resume Parser Job Recommender Output](https://github.com/user-attachments/assets/a6cdabc9-3a45-4682-85ec-ce1c1d9baa4c)





## Tech Stack

Python 3.8+

- **TF–IDF Vectorizer** → Text feature extraction

- **Logistic Regression** → Classification model

- **NLTK / Regex** → Preprocessing & skill extraction

- **Pandas, NumPy** → Data handling

