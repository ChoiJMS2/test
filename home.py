# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image
import pandas as pd

def run_home():
    img = Image.open("image/mak.png")
    st.image(img, width=500)

    st.markdown("<h1 style='color: red;'>Store Sales - Time Series Forecasting</h1>", unsafe_allow_html=True)
    data = {'members': ['Jeong-An Choi', 'Jae-Myoung Choi', 'Yong-Seok Kwon', 'Yong-Jun Yoon', 'Geon-Yong Lee',
                        'Kyung-Cheol Lee'],
            'Skills': ['Analysis, Planning', 'Analysis, Preprocessing', 'Analysis, Dashboard', 'Dashboard, PPT',
                       'Research,Dashboard', '', ],
            'Git or Blog': ['', '[GitHub](https://james-choi88.tistory.com/)\n[Tistory](https://github.com/ChoiJMS2)', '', '', '', '']}
    df = pd.DataFrame(data).set_index("members")
    st.table(df)

    st.markdown("### Analytic Language Tools")
    col1, col2, col3 = st.columns(3)
    with col1:
        img1 = Image.open("image/st1.png")
        st.image(img1, width=200)

    with col2:
        img2 = Image.open("image/py1.png")
        st.image(img2, width=200)

    with col3:
        img3 = Image.open("image/py2.png")
        st.image(img3, width=200)

    st.markdown("### Project Overview\n\n"
                "- Use time series forecasting to predict store sales based on data from Corporación Favorita, a large grocery retailer based in Ecuador \n\n"
                "- Built a model to more accurately predict selling unit costs for thousands of items sold in multiple Favorita stores \n\n"
                "- To practice machine learning skills with an easy-to-access training dataset consisting of dates, store and item information, promotions, and sales unit prices.")

    st.markdown("### Duration \n"
                "- 2023.04.20~05.17")

    st.markdown("### Purpose of analysis")
    st.markdown(
        " - To gain insight into the store's historical sales data and use that information to predict future sales trends\n\n"
        " - Stores make more informed decisions about inventory management, marketing strategies, and overall business planning\n\n"
        " - By analyzing patterns and trends in sales data, project teams identify factors that may be contributing to changes in sales, such as seasonality or external events\n\n"
        " - Ultimately providing actionable insights to help stores optimize operations and improve financial performance.")

    st.markdown("### Identify and forecast sales changes")

    st.markdown("### Model the final forecast")
    col1, col2 = st.columns(2)
    pass


