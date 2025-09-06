from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def create_tfidf_features(texts, max_features=5000, save_path=None):
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(texts)
    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(vectorizer, f)
    return X, vectorizer

def load_vectorizer(path):
    import pickle
    with open(path, 'rb') as f:
        return pickle.load(f)
