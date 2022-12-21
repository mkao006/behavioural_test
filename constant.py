CATBOOST_PARAMS = {
    'iterations': 500,
    'thread_count': 10,
    'depth': 5,
    'learning_rate': 0.5,
    'loss_function': 'RMSE',
}
TARGET_NAME = 'medv'
ARTIFACT_DIR = 'artifacts'
TRAIN_DATA_OUTPUT_NAME = 'boston.csv'
MODEL_OUTPUT_NAME = 'model.cbm'
