from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model/house_price_model.pkl")
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    input_data = [[
        float(data["bedrooms"]),
        float(data["bathrooms"]),
        float(data["living_area"]),
        float(data["floors"]),
        float(data["condition"]),
        float(data["grade"]),
        float(data["built_year"]),
        float(data["zipcode"]),
        float(data["lat"]),
        float(data["long"]),
        float(data["schools"]),
        float(data["airport"])
    ]]

    scaled = scaler.transform(input_data)

    prediction = float(model.predict(scaled)[0])

    return jsonify({
        "price": round(prediction, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)