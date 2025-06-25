from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

class NewsRequest(BaseModel): #BaseModel을 상속받아 사용
    text:str

@app.get('/')
def read_root():
    return {'message':'hello, FastApi$$$'}

# bk-end없이 바로 사용
# excel화일이나, db 만들어 사용가능
@app.post('/summarize')
def summarize_news(request:NewsRequest):
    prompt = f'''
            You are an AI specialized in summarizing news articles.  
            Please summarize the following article in **3 concise sentences**, focusing only on the key points.
            Summary Guidelines:  
            - Include key information such as main figures, events, time, location, cause, and outcome  
            - Avoid repetition; keep it concise  
            - Use an objective and neutral tone
            ** text : {request.text} **
            3-Sentence Summary
            **finally, provide your full answer in korean**           
    '''
    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system","content":"You are a great assistant in summarizing text in Korean."},
            {"role":"user","content":prompt}
        ]
    )
    summary = response.choices[0].message.content
    return {'summary':summary}

