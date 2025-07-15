from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional

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


class SocDemProfileBase(BaseModel):
    age: int
    workclass: EmploymentStatus
    education: EducationLevel
    education_num: int
    marital_status: MaritalStatus
    occupation: Occupation
    capital_gain: int
    capital_loss: int
    hours_per_week: int


class SocDemProfileCreate(SocDemProfileBase):
    pass


class SocDemProfileUpdate(BaseModel):
    age: Optional[int] = None
    workclass: Optional[EmploymentStatus] = None
    education: Optional[EducationLevel] = None
    education_num: Optional[int] = None
    marital_status: Optional[MaritalStatus] = None
    occupation: Occupation | None = None
    capital_gain: Optional[int] = None
    capital_loss: Optional[int] = None
    hours_per_week: Optional[int] = None


class SocDemProfileRead(SocDemProfileBase):
    id: int
    income: Optional[IncomeCategory] = None
    was_used_for_training: bool | None = None
    created_at: datetime

    class Config:
        from_attributes = True
