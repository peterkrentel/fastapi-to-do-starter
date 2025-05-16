from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    gpt3 = "gpt-3"
    gpt4 = "gpt-4"
    gpt4_32k = "gpt-4-32k"
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.gpt3:
        return {"model_name": model_name, "message": "GPT-3 is a powerful language model."}
    if model_name == ModelName.gpt4:
        return {"model_name": model_name, "message": "GPT-4 is the latest version with improved capabilities."}
    if model_name == ModelName.gpt4_32k:
        return {"model_name": model_name, "message": "GPT-4 32k can handle larger contexts."}
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "AlexNet is a pioneering convolutional neural network."}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "ResNet introduced residual learning for deep networks."}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeNet is one of the earliest convolutional neural networks."}