import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import lightgbm as lgb
import optuna
import mlflow
from mlflow.models.signature import infer_signature
import logging
import shap


def split_data(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    X = df.drop(["% Iron Concentrate", "% Silica Concentrate"], axis=1)
    y = df["% Silica Concentrate"]

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test


def train_evaluate_model(
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> lgb.LGBMRegressor:

    # Define parameters for lightgbm
    params = {
        "learning_rate": 0.04789370740272594,
        "num_leaves": 650,
        "subsample": 0.5828415933146901,
        "colsample_bytree": 0.8910869618475113,
        "min_data_in_leaf": 72,
    }

    # Train model
    model = lgb.LGBMRegressor(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluate model
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Training without Optuna")

    # Log the accuracy
    mlflow.log_metric("rmse", rmse)

    # Log the hyperparameters
    mlflow.log_params(params)

    # Infer the model signature
    signature = infer_signature(X_train, model.predict(X_train))

    # Log the model
    model_info = mlflow.lightgbm.log_model(
        lgb_model=model,
        artifact_path="mining-quality-model",
        signature=signature,
        input_example=X_train,
        registered_model_name="silica_model",
    )

    print("---------------------------")
    print(f"RMSE: {rmse}")
    print("---------------------------")
    return model


def train_tune_model(
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> lgb.LGBMRegressor:

    def objective(trial):
        params = {
            "objective": "regression",
            "metric": "rmse",
            "n_estimators": 1000,
            "verbosity": -1,
            "bagging_freq": 1,
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.1, log=True),
            "num_leaves": trial.suggest_int("num_leaves", 2, 2**10),
            "subsample": trial.suggest_float("subsample", 0.05, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.05, 1.0),
            "min_data_in_leaf": trial.suggest_int("min_data_in_leaf", 1, 100),
        }

        model = lgb.LGBMRegressor(**params)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        return rmse

    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=5)
    print("---------------------------")
    print("Best hyperparameters:", study.best_params)
    print("Best RMSE:", study.best_value)
    print("---------------------------")

    # Train with the best hyperparameters
    best_params = study.best_params

    # best_params = {'learning_rate': 0.04789370740272594, 'num_leaves': 650, 'subsample': 0.5828415933146901, 'colsample_bytree': 0.8910869618475113, 'min_data_in_leaf': 72}

    model = lgb.LGBMRegressor(**best_params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Training with Optuna")

    # Log the accuracy
    mlflow.log_metric("rmse", rmse)

    # Log the hyperparameters
    mlflow.log_params(best_params)

    # Infer the model signature
    signature = infer_signature(X_train, model.predict(X_train))

    # Log the model
    model_info = mlflow.lightgbm.log_model(
        lgb_model=model,
        artifact_path="mining-quality-model",
        signature=signature,
        input_example=X_train,
        registered_model_name="silica_model",
    )

    print("---------------------------")
    print("RMSE with Tuning:", rmse)
    print("---------------------------")

    return model


def explain_model(
    model: lgb.LGBMRegressor,
    X_train: pd.DataFrame,
    y_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_test: pd.DataFrame,
):
    shap.initjs()
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)

    # Store the SHAP values in a HTML file
    shap.save_html(
        "shap_values.html",
    )

    # Log the SHAP values as an artifact
    mlflow.log_artifact("shap_values.html")

    pass
