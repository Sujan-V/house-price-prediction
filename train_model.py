import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

from xgboost import XGBRegressor

# Load dataset
df = pd.read_csv("dataset/House Price India.csv")

# Remove unnecessary columns
drop_cols = ['id', 'Date']
for col in drop_cols:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

# Selected important features only
features = [
    'number of bedrooms',
    'number of bathrooms',
    'living area',
    'number of floors',
    'condition of the house',
    'grade of the house',
    'Built Year',
    'Postal Code',
    'Lattitude',
    'Longitude',
    'Number of schools nearby',
    'Distance from the airport'
]

target = 'Price'

X = df[features]
y = df[target]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# XGBoost Model
model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Score
score = r2_score(y_test, y_pred)

print(f"R2 Score: {score}")

# Save
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/house_price_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(features, "model/columns.pkl")

print("Model saved successfully!")