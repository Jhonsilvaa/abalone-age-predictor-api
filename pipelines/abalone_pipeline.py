"""Prediction Pipeline for Abalone Age Estimation.

Handles feature processing, volume calculation, and model prediction.
"""

from typing import Dict

import joblib
import numpy as np
import pandas as pd


class AbalonePipeline:
    """Pipeline for predicting abalone age using a machine learning model.

    Loads pre-trained models and preprocessors from joblib files, calculates volume,
    encodes categorical features, scales numerical features, and makes predictions.

    Attributes:
        encoder: OneHotEncoder for 'Sex' feature.
        features: List of expected input features.
        scaler: RobustScaler for numerical features.
        model: Trained LightGBM regressor.
    """

    def __init__(
        self, features: str, encoder: str, scaler: str, model: str
    ) -> None:
        """
        Initialize prediction pipeline components.

        Args:
            features: Path to serialized feature list.
            encoder: Path to serialized OneHotEncoder.
            scaler: Path to serialized RobustScaler.
            model: Path to serialized LightGBM model.
        """
        self.encoder = joblib.load(encoder)
        self.features = joblib.load(features)
        self.scaler = joblib.load(scaler)
        self.model = joblib.load(model)

    def calculate_volume(self, data) -> float:
        """
        Calculate abalone volume using ellipsoid approximation.

        Args:
            data: Dictionary containing abalone measurements.

        Returns:
            float: Calculated volume of the abalone in mm³.
        """
        return (
            (4 / 3)
            * np.pi
            * (data['Length'] / 2)
            * (data['Diameter'] / 2)
            * (data['Height'] / 2)
        )

    def preprocess(self, data: Dict[str, str | float]) -> pd.DataFrame:
        """
        Preprocess input data for model prediction.

        Args:
            data: Raw input features as dictionary.

        Returns:
            pd.DataFrame: Preprocessed DataFrame with encoded and scaled features.
        """
        volume = self.calculate_volume(data)
        feature_values = [data[feature] for feature in self.features]
        df_input = pd.DataFrame([feature_values], columns=self.features)
        df_input['Volume'] = volume
        encoded = self.encoder.transform(df_input[['Sex']].copy())
        df_enc = pd.DataFrame(
            encoded.toarray(),
            columns=self.encoder.get_feature_names_out(['Sex']),
        )
        df_enc.reset_index(drop=True, inplace=True)
        df_scaler = df_input.drop(columns=['Sex']).copy()
        scaled = self.scaler.transform(df_scaler.copy())
        df_transform = pd.DataFrame(scaled, columns=df_scaler.columns)
        df_transform = pd.concat([df_enc, df_transform], axis=1)
        return df_transform

    def predict(self, data: Dict[str, str | float]) -> float:
        """
        Make age prediction from input data.

        Args:
            data: Raw input features as dictionary.

        Returns:
            float: Predicted age of the abalone in rings.
        """
        df_transform = self.preprocess(data)
        prediction = self.model.predict(df_transform)
        return prediction[0]
