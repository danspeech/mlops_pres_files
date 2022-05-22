from pydantic import BaseModel


class PredictInput(BaseModel):
    sentence: str
