import numpy as np
import pipeline
from processing.data_management import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split

from regression_model import __version__ as _version
from regression_model import logger as _logger
from regression_model.config import config


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide training data
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], test_size=0.1, random_state=0
    )

    # transform the target
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipe = pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipe)


if __name__ == "__main__":
    run_training()
