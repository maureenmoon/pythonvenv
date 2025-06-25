from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()
#실행명령어 

class AdRequest(BaseModel):
    product_name:str
    feature:str
    keyword:str
    brand_name:str
    tonnmanner:str
    value:str
    api_key:str
    
@app.get("/") #end point
def test_get():
    return {'message':'fast API test!!!'}

def ask_gpt(prompt,apikey):
    try:
        client = openai.OpenAI(api_key=apikey)
        response = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages= [
                {'role':'user','content':prompt}
            ])
        gptRes = response.choices[0].message.content
        return gptRes

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ad")
def generate_ad(req:AdRequest):
    # return {"result":req.name}
    # prompt
    prompt = f'''
        아래 내용을 참고해서 1~2줄자리 광고문구 5개 작성해줘
        - product name :{req.product_name}
        - features :{req.feature}
        - requried keywords :{req.keyword}
        - brand name : {req.brand_name}
        - ton&manner : {req.tonnmanner}
        - core values : {req.value}
        '''
    ads = ask_gpt(prompt, req.api_key)
    return {
        # "result":{
        #     "value":req.value,
        #     "name":req.name
        "result":ads
        }
    