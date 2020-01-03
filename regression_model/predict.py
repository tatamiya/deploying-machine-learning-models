import numpy as np
import pandas as pd

from config import config
from processing.data_management import load_pipeline


pipeline_file_name = 'regression_model.pkl'
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a predction using the saved model pipeline."""
    
    data = pd.read_json(input_data)
    prediction = _price_pipe.predict(data[config.FEATURES])
    output = np.exp(prediction)
    response = {'predictions': output}
    
    return response
