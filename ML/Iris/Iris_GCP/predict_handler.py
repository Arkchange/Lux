import joblib
import numpy as np

def predict(request):
    model = joblib.load('model.joblib')
    instances = request.get_json()['instances']
    predictions = model.predict(np.array(instances))
    return {'predictions': predictions.tolist()}
