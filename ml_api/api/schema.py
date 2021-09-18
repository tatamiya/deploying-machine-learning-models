from typing import List, Optional

from pydantic import BaseModel, Field


class Version(BaseModel):
    model_version: str
    api_version: str


class HouseData(BaseModel):
    Alley: Optional[str]
    BedroomAbvGr: Optional[int]
    BldgType: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinSF1: Optional[float]
    BsmtFinSF2: Optional[float]
    BsmtFinType1: Optional[str]
    BsmtFinType2: Optional[str]
    BsmtFullBath: Optional[float]
    BsmtHalfBath: Optional[float]
    BsmtQual: Optional[str]
    BsmtUnfSF: Optional[float]
    CentralAir: Optional[str]
    Condition1: Optional[str]
    Condition2: Optional[str]
    Electrical: Optional[str]
    EnclosedPorch: Optional[int]
    ExterCond: Optional[str]
    ExterQual: Optional[str]
    Exterior1st: Optional[str]
    Exterior2nd: Optional[str]
    Fence: Optional[str]
    FireplaceQu: Optional[str]
    Fireplaces: Optional[int]
    Foundation: Optional[str]
    FullBath: Optional[int]
    Functional: Optional[str]
    GarageArea: Optional[float]
    GarageCars: Optional[float]
    GarageCond: Optional[str]
    GarageFinish: Optional[str]
    GarageQual: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GrLivArea: Optional[int]
    HalfBath: Optional[int]
    Heating: Optional[str]
    HeatingQC: Optional[str]
    HouseStyle: Optional[str]
    Id: Optional[int]
    KitchenAbvGr: Optional[int]
    KitchenQual: Optional[str]
    LandContour: Optional[str]
    LandSlope: Optional[str]
    LotArea: Optional[int]
    LotConfig: Optional[str]
    LotFrontage: Optional[float]
    LotShape: Optional[str]
    LowQualFinSF: Optional[int]
    MSSubClass: Optional[int]
    MSZoning: Optional[str]
    MasVnrArea: Optional[float]
    MasVnrType: Optional[str]
    MiscFeature: Optional[str]
    MiscVal: Optional[int]
    MoSold: Optional[int]
    Neighborhood: Optional[str]
    OpenPorchSF: Optional[int]
    OverallCond: Optional[int]
    OverallQual: Optional[int]
    PavedDrive: Optional[str]
    PoolArea: Optional[int]
    PoolQC: Optional[str]
    RoofMatl: Optional[str]
    RoofStyle: Optional[str]
    SaleCondition: Optional[str]
    SaleType: Optional[str]
    ScreenPorch: Optional[int]
    Street: Optional[str]
    TotRmsAbvGrd: Optional[int]
    TotalBsmtSF: Optional[float]
    Utilities: Optional[str]
    WoodDeckSF: Optional[int]
    YearBuilt: Optional[int]
    YearRemodAdd: Optional[int]
    YrSold: Optional[int] = Field()
    FirstFlrSF: Optional[int] = Field(alias="1stFlrSF")
    SecondFlrSF: Optional[int] = Field(alias="2ndFlrSF")
    ThreeSsnPortch: Optional[int] = Field(alias="3SsnPorch")

    class Config:
        schema_extra = {
            "example": {
                "Id": 1461,
                "MSSubClass": 20,
                "MSZoning": "RH",
                "LotFrontage": 80.0,
                "LotArea": 11622,
                "Street": "Pave",
                "Alley": None,
                "LotShape": "Reg",
                "LandContour": "Lvl",
                "Utilities": "AllPub",
                "LotConfig": "Inside",
                "LandSlope": "Gtl",
                "Neighborhood": "NAmes",
                "Condition1": "Feedr",
                "Condition2": "Norm",
                "BldgType": "1Fam",
                "HouseStyle": "1Story",
                "OverallQual": 5,
                "OverallCond": 6,
                "YearBuilt": 1961,
                "YearRemodAdd": 1961,
                "RoofStyle": "Gable",
                "RoofMatl": "CompShg",
                "Exterior1st": "VinylSd",
                "Exterior2nd": "VinylSd",
                "MasVnrType": "None",
                "MasVnrArea": 0.0,
                "ExterQual": "TA",
                "ExterCond": "TA",
                "Foundation": "CBlock",
                "BsmtQual": "TA",
                "BsmtCond": "TA",
                "BsmtExposure": "No",
                "BsmtFinType1": "Rec",
                "BsmtFinSF1": 468.0,
                "BsmtFinType2": "LwQ",
                "BsmtFinSF2": 144.0,
                "BsmtUnfSF": 270.0,
                "TotalBsmtSF": 882.0,
                "Heating": "GasA",
                "HeatingQC": "TA",
                "CentralAir": "Y",
                "Electrical": "SBrkr",
                "1stFlrSF": 896,
                "2ndFlrSF": 0,
                "LowQualFinSF": 0,
                "GrLivArea": 896,
                "BsmtFullBath": 0.0,
                "BsmtHalfBath": 0.0,
                "FullBath": 1,
                "HalfBath": 0,
                "BedroomAbvGr": 2,
                "KitchenAbvGr": 1,
                "KitchenQual": "TA",
                "TotRmsAbvGrd": 5,
                "Functional": "Typ",
                "Fireplaces": 0,
                "FireplaceQu": None,
                "GarageType": "Attchd",
                "GarageYrBlt": 1961.0,
                "GarageFinish": "Unf",
                "GarageCars": 1.0,
                "GarageArea": 730.0,
                "GarageQual": "TA",
                "GarageCond": "TA",
                "PavedDrive": "Y",
                "WoodDeckSF": 140,
                "OpenPorchSF": 0,
                "EnclosedPorch": 0,
                "3SsnPorch": 0,
                "ScreenPorch": 120,
                "PoolArea": 0,
                "PoolQC": None,
                "Fence": "MnPrv",
                "MiscFeature": None,
                "MiscVal": 0,
                "MoSold": 6,
                "YrSold": 2010,
                "SaleType": "WD",
                "SaleCondition": "Normal",
            }
        }


class PredictionResults(BaseModel):
    predictions: List[float]
    version: str
