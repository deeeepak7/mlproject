# Student Performance Prediction

This project trains regression models to predict student math scores based on demographic and academic features. It includes a full pipeline for data ingestion, preprocessing, model training, and a Flask web app for interactive predictions.

## Project Structure
- `source/components/data_ingestion.py` – downloads/loads the raw dataset, builds train/test splits, and triggers downstream components.
- `source/components/data_transformation.py` – builds a preprocessing pipeline (imputation, scaling, encoding) and serializes it to `artifact/preprocessor.pkl`.
- `source/components/model_trainer.py` – trains multiple regressors with default hyperparameters, selects the best model, and saves it to `artifact/model.pkl`.
- `source/pipeline/predict_pipeline.py` – loads the persisted artifacts and serves predictions.
- `app.py` – Flask application exposing web forms for predictions.
- `artifact/` – generated artifacts (raw/train/test splits, preprocessor, model).

## Prerequisites
- Python 3.10+
- pip or conda for dependency management

Install dependencies:

```bash
pip install -r requirements.txt
```

## Training the Pipeline
Retrain the preprocessing and model artifacts whenever dependencies change or to refresh performance:

```bash
python source/components/data_ingestion.py
```

This script executes the ingestion → transformation → training workflow and produces updated artifacts inside `artifact/`.

## Running the Web App
Launch the Flask server locally:

```bash
python app.py
```

Visit `http://localhost:5000` to access the UI. Submit the student attributes via the form to obtain the predicted math score.

## Making Programmatic Predictions
Use the `PredictPipeline` and `CustomData` classes directly:

```python
from source.pipeline.predict_pipeline import PredictPipeline, CustomData

payload = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72,
    writing_score=74,
)

pipeline = PredictPipeline()
prediction = pipeline.predict(payload.get_data_as_data_frame())
print(prediction[0])
```

## Troubleshooting
- **`ModuleNotFoundError: No module named 'source'`**: run commands from the project root (`C:\project\mlproject`) or add it to your `PYTHONPATH`.
- **`InconsistentVersionWarning` when loading pickles**: delete `artifact/model.pkl` and `artifact/preprocessor.pkl`, then retrain the pipeline to regenerate artifacts with the current library versions.
- **Unknown categories during transform**: ensure categorical inputs match the training categories; `CustomData` fills missing categorical entries with `"unknown"` before transformation.

## Contributing
Feel free to open issues or submit pull requests with improvements or additional features.
