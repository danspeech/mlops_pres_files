from fastapi import FastAPI

from api_models import PredictInput
from model import MyModel, convert_api_input_to_model_input

# Instantiating FastAPI
api = FastAPI()

lr_model = MyModel()


# Defining the post prediction endpoint
@api.post('/predict')
async def predict(prediction_input: PredictInput):
    # Convert api input to model input
    model_input = convert_api_input_to_model_input(prediction_input)

    # Get a prediction
    pred = lr_model.predict(model_input)[0]

    return pred
