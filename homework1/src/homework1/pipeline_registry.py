"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from .pipelines.test1 import pipeline as test1


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    test1_pipe = test1.create_pipeline()

    return {"test1" : test1_pipe,
            "__default__": pipeline([]) + test1_pipe + pipeline([])}
