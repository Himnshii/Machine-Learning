import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

#  Load dataset
df = pd.read_excel("gallstone.xlsx")  # Adjust path if needed
df.columns = df.columns.str.strip()
# Select features used by your app
features = [
    "Age",
    "Body Mass Index (BMI)",
    "High Density Lipoprotein (HDL)",
    "Triglyceride",
    "Glucose",
    "C-Reactive Protein (CRP)"
]

target = "Gallstone Status"

x = df[features]
y = df[target]

# Train-test split
X_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42)

#  Build pipeline (scaling + model)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression(solver="liblinear", class_weight="balanced"))
])

#  Fit pipeline
pipe.fit(X_train, y_train)

#  Save fitted pipeline
joblib.dump(pipe, "model.pkl")
print("Model retrained and saved as model.pkl")