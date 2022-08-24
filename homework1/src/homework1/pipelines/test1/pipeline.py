from kedro.pipeline import Pipeline, node, pipeline
from .nodes import *


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=gen_sample_df,
                inputs="params:cols",
                outputs="raw_df",
                name="generation",
                tags="generation"
            ),
            node(
                func=prepare_df,
                inputs=[
                    "raw_df", 
                    "params:cols",
                    "params:meths"
                    ],
                outputs="prepared_df",
                name="preparation",
                tags="preparation"
            ),
            node(
                func=calcClusterFact,
                inputs="prepared_df",
                outputs=[
                    "predict_labels",
                    "db_metric"
                    ],
                name="clasterization",
                tags="clasterization"
            ),
            node(
                func=pca,
                inputs="prepared_df",
                outputs="result_df",
                name="pca",
                tags="pca"
            )
        ],
        inputs=None,
        outputs=[
            "result_df"
            ]
    )
