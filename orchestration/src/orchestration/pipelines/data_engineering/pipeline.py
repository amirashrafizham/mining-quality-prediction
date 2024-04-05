"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import convert_to_datetime, convert_to_float


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=convert_to_datetime,
                inputs="mining_data",
                outputs="df_converted_to_datetime",
                name="convert_date_to_datetime_node",
            ),
            node(
                func=convert_to_float,
                inputs="df_converted_to_datetime",
                outputs="df_converted_to_float",
                name="convert_to_float",
            ),
        ]
    )
