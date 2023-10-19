from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import openai
import os

app = FastAPI()

load_dotenv()

openai.api_key = os.getenv("SECRET_KEY")

class Prompt(BaseModel):
    text: str = Field(min_length=10, max_length=100)
    

@app.post("/Chat", tags=["Chat"])
def Generate_response(prompt: Prompt):
    text_lenght = 1000
    gpt3_model = "davinci"
    responses = openai.Completion.create(
        engine= gpt3_model,
        prompt=prompt.text,
        max_tokens = text_lenght,
        n=1,
        stop=None,
        temperature=0.5
    )
    return responses["choices"][0]["text"]
    
