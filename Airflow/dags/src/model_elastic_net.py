from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
import numpy as np
import pandas as pd
from datetime import datetime


# Function to train the model and make predictions
def train_and_predict_elastic_net(augmented_data, test_data, combined_features):
    """
    Trains an Elastic Net Regressor model and predicts on the test set.

    Parameters:
    - augmented_data (pd.DataFrame): Training dataset with features and target.
    - test_data (pd.DataFrame): Test dataset with features.
    - combined_features (list): List of feature columns.

    Returns:
    - np.ndarray: Predicted values for the test set.
    - ElasticNet: Trained Elastic Net model.
    """
    X_train = augmented_data[combined_features]
    y_train = augmented_data['SalePrice']
    X_test = test_data[combined_features]
    y_test = test_data['SalePrice']

    # Set the MLflow experiment
    mlflow.set_experiment("Elastic Net Regressor Experiment")

    # Generate a unique run name with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_name = f"ElasticNet_{len(combined_features)}_features_{timestamp}"

    # Start MLflow run
    with mlflow.start_run(run_name=run_name):
        # Model creation
        model = ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=42)  # Balance of Ridge and Lasso
        model.fit(X_train, y_train)

        # Predictions and metrics
        y_pred = model.predict(X_test)
        signature = infer_signature(X_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        # Log metrics
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        # Log hyperparameters
        mlflow.log_param("model_type", "Elastic Net Regressor")
        mlflow.log_param("alpha", 1.0)
        mlflow.log_param("l1_ratio", 0.5)

        # Log and register the model
        mlflow.sklearn.log_model(model, "model", signature=signature)
        mlflow.register_model("runs:/{}/model".format(mlflow.active_run().info.run_id), "ElasticNetRegressor")

        # Print tracking URI and run details
        print("Tracking URI:", mlflow.get_tracking_uri())
        print("Run Name:", run_name)

        return y_pred, model


# Function to evaluate the model's performance
def evaluate_model(test_data, y_pred):
    """
    Evaluates model performance using various metrics.

    Parameters:
    - test_data (pd.DataFrame): Test dataset with actual target values.
    - y_pred (np.ndarray): Predicted values from the model.

    Returns:
    - dict: A dictionary containing evaluation metrics.
    """
    y_test = test_data['SalePrice']

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}


# Function to compare model performance on original and augmented data
def compare_models_elastic_net(train_data, augmented_data, test_data, combined_features):
    """
    Compares model performance using original and augmented training data.

    Parameters:
    - train_data (pd.DataFrame): Original training dataset with 'SalePrice' target.
    - augmented_data (pd.DataFrame): Augmented training dataset with 'SalePrice' target.
    - test_data (pd.DataFrame): Test dataset with 'SalePrice' target.
    - combined_features (list): List of feature columns.

    Returns:
    - pd.DataFrame: Comparison of evaluation metrics for original and augmented data.
    """
    # Train and evaluate on original training data
    print("Training on Original Data...")
    y_pred_original, _ = train_and_predict_elastic_net(train_data, test_data, combined_features)
    original_metrics = evaluate_model(test_data, y_pred_original)

    # Train and evaluate on augmented training data
    print("Training on Augmented Data...")
    y_pred_augmented, _ = train_and_predict_elastic_net(augmented_data, test_data, combined_features)
    augmented_metrics = evaluate_model(test_data, y_pred_augmented)

    # Compare the metrics in a DataFrame
    comparison_df = pd.DataFrame([original_metrics, augmented_metrics], index=["Original Data", "Augmented Data"])

    return comparison_df
