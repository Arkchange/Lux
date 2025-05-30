from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Charger le modèle
model = joblib.load("iris_model.pkl")

# Créer l'app FastAPI
app = FastAPI()

# Définir le format des données
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
def predict(data: IrisData):
    input_data = [[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]]
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}