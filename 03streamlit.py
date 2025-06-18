import streamlit as st
import pandas as pd
import numpy as np

# st.text('hello streamlit')

# st.title('my 1st streamlit')
# st.write('this is DataFrame example')

# df = pd.DataFrame(
#     np.random.randn(10,2),
#     columns = ['x','y']
# )

# # st.write(np.random(10,2))

# st.dataframe(df)

# st.line_chart(df)

st.title('it is a title')
st.header('header')
st.subheader('subheader')
st.caption('caption')

# ''' 문서로 쓸때(coding info) 사용 '''
sample_code = '''
def function():
    print('test')
'''
st.code(sample_code,language='python')

st.markdown('### hi world')
st.markdown('##### hi world')
st.markdown('hi ***hongGD*** :blue[aoi]')

sample_table = '''
### Member list

|name|age|occupancy|
|----|---|---------|
|hansy|20|office+++++++++++++++++++++++++-------------------------------------------------------------------------------worker|

link[naver](https://www.naver.com)

* name

1. hongGD
2. leeSS
3. maureen

'''
st.markdown('---')
st.markdown(sample_table)
st.markdown('___')

button = st.button('click here')
if button:
    st.write('hi, nice to meet you')

title = st.text_input(
    label = 'input area',
    placeholder='travel site'
)

st.write(f'your selected site : {title}')

