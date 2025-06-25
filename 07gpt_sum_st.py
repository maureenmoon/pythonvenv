#웹 환경에서 gpt 적용

import streamlit as st
from openai import OpenAI

def askGpt(prompt, apiKey):
    client = OpenAI(api_key=apiKey)
    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            # {"role":"system","content":"You are a great assistant in summarizing text in Korean."},
            {"role":"user","content":prompt}
        ]
    )
    summary = response.choices[0].message.content
    return summary

def main():
    st.title('article summarizing program')
    if 'OPENAI_API' not in st.session_state:
       st.session_state['OPENAI_API'] = '' #초기화 

    #side bar
    with st.sidebar:
        open_apikey = st.text_input(
            label = 'openai api key',
            placeholder='inpur your api key',
            value='',
            type='password'
        )

        # gpt에게 새로운 창 열지말고, 계속 같은 새션 유지하게 하기
        if open_apikey:
            st.session_state['OPENAI_API'] = open_apikey

    st.markdown('---')
    text = st.text_area('input the article to summarize')

    if st.button('summarize'):
        prompt = f'''
            You are an assistant who summarizes text in Korean.
            Your task is to summarize text sentences in Korean.
            Your summary should include the following:
            Remove duplicate content. Increase the weight of the summary. Summarize in 3 lines. Write in Markdown.
            Summary guideline:
            Focus on:
            Main topic (Who, What, When, Where)
            Key facts and events
            Consequences or implications
            Output Format:
            Headline: One-sentence title of the news
            Summary (3~5 bullet points): Main facts or updates
            Why it matters: 1~2 sentences explaining the importance
            **finally, provide your full answer in Korea**
            ** text : {text} **
        '''

        st.info(askGpt(prompt, st.session_state['OPENAI_API']))
        

if __name__ == "__main__":
    main()

