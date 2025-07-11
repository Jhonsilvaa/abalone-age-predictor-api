"""Schemas for Abalone API.

Defines request/response structures and validation rules.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field


class PredictRequest(BaseModel):
     
    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            'example': {
                'Sex': 'M',
                'Length': 0.455,
                'Diameter': 0.365,
                'Height': 0.095,
                'Whole weight': 0.5140,
                'Shucked weight': 0.2245,
                'Viscera weight': 0.1010,
                'Shell weight': 0.150,
            }
        },
    )

    Sex: Literal['M', 'F', 'I'] = Field(
        description='Abalone sex (M: Male, F: Female, I: Infant).'
    )
    Length: Annotated[
        float, Field(gt=0.0, alias='Length', description='Length in mm.')
    ]
    Diameter: Annotated[
        float, Field(gt=0.0, alias='Diameter', description='Diameter in mm.')
    ]
    Height: Annotated[
        float, Field(gt=0.0, alias='Height', description='Height in mm.')
    ]
    Whole_weight: Annotated[
        float,
        Field(
            gt=0.0, alias='Whole weight', description='Total weight in grams.'
        ),
    ]
    Shucked_weight: Annotated[
        float,
        Field(
            gt=0.0, alias='Shucked weight', description='Meat weight in grams.'
        ),
    ]
    Viscera_weight: Annotated[
        float,
        Field(
            gt=0.0,
            alias='Viscera weight',
            description='Viscera weight in grams.',
        ),
    ]
    Shell_weight: Annotated[
        float,
        Field(
            gt=0.0, alias='Shell weight', description='Shell weight in grams.'
        ),
    ]


class PredictResponse(BaseModel):
   
    model_config = ConfigDict(json_schema_extra={'example': {'prediction': 7}})
    prediction: int = Field(description='Predicted age in rings.')


class HealthResponse(BaseModel):

    status: str
    message: str