import os
from behave import *
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from constant import (
    ARTIFACT_DIR,
    TRAIN_DATA_OUTPUT_NAME,
    MODEL_OUTPUT_NAME
)

@given('A trained model with training data')
def step_impl(context):
    """Load the trained model and dataset and add to the context for
    later use.

    """
    # load the data
    df = pd.read_csv(os.path.join(ARTIFACT_DIR, TRAIN_DATA_OUTPUT_NAME))

    # load the model
    model = CatBoostRegressor()
    model.load_model(os.path.join(ARTIFACT_DIR, MODEL_OUTPUT_NAME))

    # add to context
    context.model = model
    context.df = df



@when('We perturbate the room number per dwelling')
def step_impl(context):
    """Add one to 'rm', the perturbation can be random but the test
    would have to be changed.

    """
    perturbated_df = context.df.copy()
    perturbated_df['rm'] += 1

    context.perturbated_df = perturbated_df


@then('The change in predicted median value should be positively correlated with the change.')
def step_impl(context):
    """Since we have added 1 to 'rm', then in large, most of the
    predicted median value should have increased.

    Given there may be cases where increase in 'rm' may not increaes
    median value, we will set the test to pass if 90% of the predicted
    value have increased.

    """
    original_prediction = context.model.predict(context.df)
    perturbated_prediction = context.model.predict(context.perturbated_df)
    pct_median_value_increased = np.mean(perturbated_prediction >= original_prediction)
    assert pct_median_value_increased >= 0.9
