import os
from pydataset import data
import pandas as pd
from sklearn.model_selection import train_test_split

from catboost import (
    Pool,
    CatBoostRegressor
)

from constant import (
    CATBOOST_PARAMS,
    TARGET_NAME,
    ARTIFACT_DIR,
    TRAIN_DATA_OUTPUT_NAME,
    MODEL_OUTPUT_NAME
)


def load_data() -> pd.DataFrame:
    """Load the boston housing data set and then save the data as
    artifact for testing.

    """
    boston_df = data('Boston')

    # save the data for testing
    boston_df.to_csv(os.path.join(ARTIFACT_DIR, TRAIN_DATA_OUTPUT_NAME), index=False)

    return boston_df


def train(df: pd.DataFrame) -> None:
    """Train a model and then save the model as an artifact.

    """

    # split the data for training
    data_x = df.drop(TARGET_NAME, axis=1)
    data_y = df[[TARGET_NAME]]
    train_x, test_x, train_y, test_y = train_test_split(data_x, data_y)
    train_pool = Pool(train_x, train_y)
    test_pool = Pool(test_x, test_y)

    # train the model
    model = CatBoostRegressor(**CATBOOST_PARAMS)
    model.fit(train_pool, eval_set=test_pool)

    # save the artifacts
    model.save_model(os.path.join(ARTIFACT_DIR, MODEL_OUTPUT_NAME))


if __name__ == '__main__':
    df = load_data()
    train(df)
