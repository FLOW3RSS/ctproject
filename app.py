import streamlit as st
import streamlit.components.v1 as components #htmlviewer로 대체해도 된다
st.set_page_config(layout='wide', page_title = 'Double secret rule!!!')
# Title Msg#1
st.title("This is JS Webapp!!")

# html = '''
# <html>
#     <head>
#         <title> this is my html </title>
#     </head>
    
#     <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#     </body>
# </html>
# '''
with open('./index.html', 'r', encoding = 'utf-8') as f:
    html = f.read()
    f.close()

with open('./index2.html', 'r', encoding = 'utf-8') as f2:
    html2 = f2.read()
    f2.close()    


# Box#1(4), Box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content#1..'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content...')
        st.video(url)

    with st.expander('Image Content..'):
        Imagefilepath = 'gpt.jpg'
        st.image(Imagefilepath)

    with st.expander('카피바라의 이중암호 규칙'):
        components.html(html, height=1000, scrolling=True)
        #htmlviewer.html(html, height=600)

    with st.expander('카피바라의 경로탐색'):
        components.html(html2, height=1000, scrolling=True)
        #htmlviewer.html(html, height=600)    

    with st.expander('AI+X'):
        components.html(html2, height=1000, scrolling=True)
        #htmlviewer.html(html, height=600)            
    
with col2:
    with st.expander('Tips...'):
        st.info('Tips...')

st.markdown('<hr>', unsafe_allow_html=True) # html 여기에 넣는 것!
st.write('<font color="BLUE">(c)copyright. all rights reserved by JS', unsafe_allow_html=True)