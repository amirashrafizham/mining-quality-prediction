from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, train_evaluate_model, train_tune_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=split_data,
                inputs="df_cleaned_table",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            # node(
            #    func=train_evaluate_model,
            #    inputs=["X_train", "y_train", "X_test", "y_test"],
            #    outputs="model_no_tuning",
            #    name="train_evaluate_model_node",
            # ),
            node(
                func=train_tune_model,
                inputs=["X_train", "y_train", "X_test", "y_test"],
                outputs="model_with_tuning",
                name="train_tune_model_node",
            ),
        ]
    )
