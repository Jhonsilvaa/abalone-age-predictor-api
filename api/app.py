"""Flask API for Abalone Age Prediction.

This module creates a Flask application serving machine learning predictions for abalone age."""

from pathlib import Path

from flask import Flask
from flask import Response as FlaskResponse
from flask import jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response

from pipelines.abalone_pipeline import AbalonePipeline
from schemas.abalone_schemas import (
    HealthResponse,
    PredictRequest,
    PredictResponse,
)

app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Abalone Age Prediction')
spec.register(app)

BASE_DIR = Path(__file__).resolve().parent.parent
pipeline = AbalonePipeline(
    str(BASE_DIR / 'models' / 'features.joblib'),
    str(BASE_DIR / 'models' / 'encoder.joblib'),
    str(BASE_DIR / 'models' / 'scaler.joblib'),
    str(BASE_DIR / 'models' / 'model.joblib'),
)


@app.route('/health', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=HealthResponse))
def health() -> FlaskResponse:
    return jsonify({'status': 'ok', 'message': 'API is running.'})


@app.route('/predict', methods=['POST'])
@spec.validate(
    body=Request(PredictRequest), resp=Response(HTTP_200=PredictResponse)
)
def predict() -> FlaskResponse:
    data = request.context.body.model_dump(by_alias=False)  # type: ignore
    prediction = pipeline.predict(data)
    return jsonify({'prediction': int(prediction)})


if __name__ == '__main__':
    app.run()
