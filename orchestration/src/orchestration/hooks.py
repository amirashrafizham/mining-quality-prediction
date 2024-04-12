from kedro.framework.hooks import hook_impl
from pyspark import SparkConf
from pyspark.sql import SparkSession
import time
import os
import mlflow


class SparkHooks:
    @hook_impl
    def after_context_created(self, context) -> None:
        """Initialises a SparkSession using the config
        defined in project's conf folder.
        """

        # Load the spark configuration in spark.yaml using the config loader
        parameters = context.config_loader["spark"]
        spark_conf = SparkConf().setAll(parameters.items())

        # Initialise the spark session
        spark_session_conf = (
            SparkSession.builder.appName(context.project_path.name)
            .enableHiveSupport()
            .config(conf=spark_conf)
        )
        _spark_session = spark_session_conf.getOrCreate()
        _spark_session.sparkContext.setLogLevel("WARN")


class ModelTrackingHooks:
    """Namespace for grouping all model-tracking hooks with MLflow together."""

    @hook_impl
    def before_pipeline_run(self) -> None:
        """Hook implementation to start an MLflow run
        with the session_id of the Kedro pipeline run.
        """
        mlflow.set_tracking_uri("http://localhost:8080")
        mlflow.set_experiment("mining-quality-model")
        mlflow.start_run()

    @hook_impl
    def after_pipeline_run(self) -> None:
        """Hook implementation to end the MLflow run
        after the Kedro pipeline finishes.
        """
        # Wait for 30 seconds to make sure all the metrics are logged
        time.sleep(30)
        mlflow.end_run()
