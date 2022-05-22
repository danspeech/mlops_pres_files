from transformers import pipeline

from api_models import PredictInput


def convert_api_input_to_model_input(prediction_input: PredictInput):
    return prediction_input.sentence


class MyModel:

    def __init__(self):
        self.sentiment_pipeline = pipeline("sentiment-analysis")

    def predict(self, data_input: str):
        return self.sentiment_pipeline(data_input)
