from pydantic import BaseModel, Field
from typing import Literal, Dict, Any, Optional
from enum import Enum


IncomeCategory = Literal["<=50K", ">50K"]
EmploymentStatus = Literal[
    "State-gov",
    "Self-emp-not-inc",
    "Private",
    "Federal-gov",
    "Local-gov",
    "?",
    "Self-emp-inc",
    "Without-pay",
    "Never-worked",
]
EducationLevel = Literal[
    "Bachelors",
    "HS-grad",
    "11th",
    "Masters",
    "9th",
    "Some-college",
    "Assoc-acdm",
    "Assoc-voc",
    "7th-8th",
    "Doctorate",
    "Prof-school",
    "5th-6th",
    "10th",
    "1st-4th",
    "Preschool",
    "12th",
]
MaritalStatus = Literal[
    "Never-married",
    "Married-civ-spouse",
    "Divorced",
    "Married-spouse-absent",
    "Separated",
    "Married-AF-spouse",
    "Widowed",
]
Occupation = Literal[
    "Adm-clerical",
    "Exec-managerial",
    "Handlers-cleaners",
    "Prof-specialty",
    "Other-service",
    "Sales",
    "Craft-repair",
    "Transport-moving",
    "Farming-fishing",
    "Machine-op-inspct",
    "Tech-support",
    "?",
    "Protective-serv",
    "Armed-Forces",
    "Priv-house-serv",
]


class ModelType(str, Enum):
    RANDOM_FOREST = "random_forest"
    LOGISTIC_REGRESSION = "logistic_regression"


class PredictionRequest(BaseModel):
    age: int = Field(..., ge=16, le=100)
    workclass: EmploymentStatus
    education: EducationLevel
    marital_status: MaritalStatus
    occupation: Occupation
    capital_gain: float = Field(..., ge=0)
    capital_loss: float = Field(..., ge=0)
    hours_per_week: int = Field(..., ge=1, le=100)


class TrainingConfig(BaseModel):
    model_type: ModelType
    hyperparameters: Dict[str, Any]
    data_path: str
    experiment_name: str = "revenue_prediction"


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    model_version: str
    confidence_interval: Optional[Dict[str, float]] = None
