from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAPI_API_KEY")
)



def main():
    with open('data/news.txt', 'r',encoding='utf-8') as f:
        text = f.read()
    prompt = f'''
        You are an assistant who summarizes text in Korean.
        Your task is to summarize text sentences in Korean.
        Your summary should include the following:
        Remove duplicate content. Increase the weight of the summary. Summarize in 3 lines. Write in Markdown.

        Summary guideline:
        🔹 Focus on:
        Main topic (Who, What, When, Where)
        Key facts and events
        Consequences or implications

        🔹 Output Format:
        Headline: One-sentence title of the news
        Summary (3~5 bullet points): Main facts or updates
        Why it matters: 1~2 sentences explaining the importance

        **finally, provide your full answer in Korea**

        ** text : {text} **

    '''

    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system","content":"You are a great assistant in summarizing text in Korean."},
            {"role":"user","content":prompt}
        ]
    )
    summary = response.choices[0].message.content
    print(summary)

if __name__ == '__main__':
    main()

