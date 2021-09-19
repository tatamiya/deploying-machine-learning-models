from regression_model import __version__ as _version

from ..api import __version__ as api_version


def test_health_endpoint_returns_200(test_client):
    # When
    response = test_client.get("/health")

    # Then
    assert response.status_code == 200
    assert response.json() == "ok"


def test_version_endpoint_returns_version(test_client):
    # When
    response = test_client.get("/v1/version")

    # Then
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["model_version"] == _version
    assert response_json["api_version"] == api_version


class TestPredictionEndpoint:
    test_data_template = [
        {
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
        },
    ]

    def test_endpoint_returns_prediction_correctly(self, test_client):
        # When
        test_data = self.test_data_template
        # When
        response = test_client.post("/v1/predict/regression", json=test_data)

        # Then
        assert response.status_code == 200
        response_json = response.json()
        prediction = response_json["predictions"]
        response_version = response_json["version"]
        assert prediction[0]
        assert response_version == _version

    def test_endpoint_returns_422_for_invalid_typed_data(self, test_client):
        # When
        test_data = [self.test_data_template[0].copy()]
        test_data[0]["OverallQual"] = "Invalid Input"  # must be int

        # When
        response = test_client.post("/v1/predict/regression", json=test_data)

        # Then
        assert response.status_code == 422
