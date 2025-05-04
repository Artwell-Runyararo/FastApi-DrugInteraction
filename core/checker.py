import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

# Load models and data
action_model = joblib.load(MODEL_DIR / "action_model.pkl")
mechanism_model = joblib.load(MODEL_DIR / "mechanism_model.pkl")
tfidf = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")
drug_to_id = joblib.load(MODEL_DIR / "drug_to_id.pkl")

def encode_drug(drug):
    return drug_to_id.get(drug, -1)

def predict_interaction(drug_a, drug_b):
    drug_a_encoded = encode_drug(drug_a)
    drug_b_encoded = encode_drug(drug_b)

    input_features = pd.DataFrame({
        "drugA_encoded": [drug_a_encoded],
        "drugB_encoded": [drug_b_encoded]
    })

    default_interaction = "the anticoagulant activities"
    tfidf_features = tfidf.transform([default_interaction]).toarray()
    tfidf_df = pd.DataFrame(tfidf_features, columns=[f"Mechanism_{i}" for i in range(tfidf_features.shape[1])])

    input_features = pd.concat([input_features, tfidf_df], axis=1)

    action_mapping = {0: 'Low', 1: 'Moderate', 2: 'High'}
    action = action_mapping.get(action_model.predict(input_features)[0], "Unknown")
    mechanism = mechanism_model.predict(input_features)[0]

    return {"action": action, "mechanism": mechanism}
