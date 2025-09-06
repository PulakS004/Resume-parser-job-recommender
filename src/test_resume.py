from src.analyze import analyze_resume

if __name__ == "__main__":
    test_resume = """
    Experienced data scientist with 3 years in machine learning and Python.
    Skilled in SQL, data analysis, AWS, and creating predictive models.
    """

    result = analyze_resume(test_resume)
    print("Predicted Category:", result["Predicted Category"])
    print("Candidate Skills:", result["Candidate Skills"])
    print("Recommended Jobs:", result["Recommended Jobs"])
