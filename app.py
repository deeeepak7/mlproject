import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from source.pipeline.predict_pipeline import CustomData
from source.pipeline.predict_pipeline import PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictData', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race_ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score"))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template("home.html", results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")