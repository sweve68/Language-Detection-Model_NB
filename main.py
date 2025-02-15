from fastapi import FastAPI
from pydantic import BaseModel
# from model.model import predictor
import pickle
import uvicorn
import re
import pytest
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

app = FastAPI()

# file1 = open('Multi_NB.pkl','rb')
# model = pickle.load(file1)

with open('Multi_NB.pkl','rb') as file1:
    model = pickle.load(file1)

with open('vectorizer.pkl','rb') as file2:
    vectorizer = pickle.load(file2)




classes = ['Arabic', 'Chinese', 'Dutch', 'English', 'Estonian', 'French',
       'Hindi', 'Indonesian', 'Japanese', 'Korean', 'Latin', 'Persian',
       'Portugese', 'Pushto', 'Romanian', 'Russian', 'Spanish', 'Swedish',
       'Tamil', 'Thai', 'Turkish', 'Urdu']



class TextInput(BaseModel):
    text: str


class PredictOut(BaseModel):
    language: str


@app.get('/')
async def home():
    return {"health_check": "OK"}

@app.post('/predict')
async def predict_language(text: TextInput):
    transformed_text = vectorizer.transform([text.text]).toarray()
    prediction = model.predict(transformed_text)
    return classes[prediction[0]]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)





