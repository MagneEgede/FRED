import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_extras.app_logo import add_logo
import seaborn as sns


# add kitten logo

def logo():
    add_logo(fr"gallery\fred.png", height=300)


# add sidebar buttons
logo_url = "gallery/fred.png"
st.sidebar.image(logo_url)
user_menu = st.sidebar.radio("User Menu", (
    'FQ Performance - Farm Overview', 'FQ Performance - Turbine Level', 'Parameter Sharing', 'FRED Partners Overview'))
if user_menu == 'FQ Performance - Farm Overview':
    st.title("'Fnattenfall' Wind Farm Overview")

    data = {'WT SITE': ['WH003', 'WH001', 'SH505', 'KL403'],
            'DoB': ['07/07/2023', '01/01/2005', '01/05/2018', '15/12/2014'], 'Turbines': [60.0, 107.0, 25.0, 38.0],
            'Average WT Failure Rate': np.random.uniform(0.3, 0.7, 4), 'Variance in Failure Rates': np.random.uniform(
            0.10, 0.90, 4), 'Certainty level': [1, 3, 4, 6]}

    df = pd.DataFrame(data)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('FR Estimates')
        sns.set()


        def partial_cum_returns(start, cum_returns):
            return cum_returns.loc[start:].div(cum_returns.loc[start])


        index = pd.DatetimeIndex(pd.date_range('20230707', '20250707', freq='W'))
        np.random.seed(5)

        returns = pd.Series(np.exp(np.random.normal(loc=0, scale=0.05, size=len(index))), index=index)
        cum_returns = returns.cumprod()
        df = pd.DataFrame(index=index)

        for date in index:
            df[date] = partial_cum_returns(date, cum_returns)
        fig = df.plot(legend=False, colormap='viridis').figure
        plt.ylabel('Failure Rate Estimations')
        fig.patch.set_facecolor('#7A63AF')
        st.pyplot(fig)
    with col2:
        st.subheader('Storage Supply')
        col21, col22 = st.columns(2)
        col21.metric("FC Units Available", "#15", "-#8")
        col22.metric("FC Units Required ", "#20", "+#12")
        st.subheader('Maintenance Options')
        col24, col25 = st.columns(2)
        with col24:
            st.button('Buy #20 Units')
        with col25:
            st.button('Vessels Available')

if user_menu == 'Page 2':
    pass