from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def train_classifier(X, y, save_path="models/resume_classifier.pkl"):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Classifier Accuracy:", accuracy_score(y_test, y_pred))
    with open(save_path, 'wb') as f:
        pickle.dump(model, f)
    return model

def load_classifier(path="models/resume_classifier.pkl"):
    with open(path, 'rb') as f:
        return pickle.load(f)
