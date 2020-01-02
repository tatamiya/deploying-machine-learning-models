import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

import pipeline
# from .data_management import load_dataset, save_pipeline
import config


def load_dataset(*, file_name: str
                 ) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data


def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = 'regression_model.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print('saved pipeline')


def run_training() -> None:
    """Train the model."""
    
    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)
    
    # divide training data
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0
    )

    # transform the target
    y_train = np.log(y_train)
    y_test = np.log(y_test)
    
    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)
    
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == '__main__':
    run_training()