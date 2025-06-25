import streamlit as st
# from openai import OpenAI 아래처럼 써도 됨
import openai

#기능구현함수
def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages= [
            {'role':'user','content':prompt}
        ])
    gptRes = response.choices[0].message.content
    return gptRes


#메인함수
def main():
    st.set_page_config(page_title='ad copy generator program')

    # if 'OPENAI_API' not in st.session_state:
    #     st.session_state['OPENAI_API'] = ''
    


    #sidebar
    with st.sidebar:
        open_apikey = st.text_input(
            label='open api key',
            placeholder='input key',
            value='',
            type='password'
        )
        if open_apikey:
            st.session_state['OPENAI_API'] = open_apikey
        st.markdown('---')
    
    st.header('ad copy generator program')
    st.markdown('---')

    col1, col2 = st.columns(2)
    with col1:
        product_name = st.text_input('product name : ',placeholder='input product name')
        #input type=text name = name
        feature = st.text_input('features : ', placeholder='features')
        keyword = st.text_input('required keywords', placeholder='required keywords')
    
    with col2:
        # brand_name = st.text_input('brand name', placeholder='brand name')
        brand_name = st.selectbox(
            'brand name',
            options=['피지오','칼로리홀릭','어반필드'],
            index=None,
            placeholder='select brand name'
        )
        #input type=text name = name
        tonnmanner = st.text_input('ton&manner',placeholder='ton&manner')
        value = st.text_input('core values', placeholder='core values')

    if st.button('ad copy generate'):
        prompt = f'''
        아래 내용을 참고해서 1~2줄자리 광고문구 5개 작성해줘
        - product name :{product_name}
        - features :{feature}
        - requried keywords :{keyword}
        - brand name : {brand_name}
        - ton&manner : {tonnmanner}
        - core values : {value}
        '''

        st.info(askGpt(prompt, st.session_state['OPENAI_API']))

if __name__ == '__main__':
    main()