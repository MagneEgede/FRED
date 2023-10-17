import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_extras.app_logo import add_logo
import seaborn as sns


# add kitten logo

def logo():
    add_logo(fr"gallery\FredV2.png", height=300)


# add sidebar buttons
logo_url = "gallery/FredV2.png"
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
            return 0.69 * cum_returns.loc[start:].div(cum_returns.loc[start])


        index = pd.DatetimeIndex(pd.date_range('20230707', '20250707', freq='W'))
        np.random.seed(5)

        returns = pd.Series(np.exp(np.random.normal(loc=0, scale=0.05, size=len(index))), index=index)
        cum_returns = returns.cumprod()
        df = pd.DataFrame(index=index)

        for date in index:
            df[date] = partial_cum_returns(date, cum_returns)
        fig = df.plot(legend=False, colormap='viridis').figure
        plt.ylabel('Failure Rate Estimations')
        fig.patch.set_facecolor('#5D5DB1')
        st.pyplot(fig)
    with col2:
        st.subheader('Storage Supply')
        col21, col22 = st.columns(2)
        numberofunits = 15
        col21.metric("FC Units Available", fr"#{numberofunits}", "-#8")
        col22.metric("FC Units Required ", "#20", "+#12")
        st.subheader('Maintenance Options')
        col24, col25 = st.columns(2)
        with col24:
            A = st.button('Buy #20 Units')
            if A:
                numberofunits = 15 + 20

        with col25:
            st.button('Vessels Available')

if user_menu == 'FQ Performance - Turbine Level':
    st.title("'Fnattenfall' Turbine Level Results")
    coll1, coll2 = st.columns(2)
    with coll1:
        st.image("gallery/wind.webp")
    with coll2:
        farm = st.selectbox("Select Wind Farm", ('WH003', 'WH001', 'SH505', 'KL403'), index=None,
                     placeholder="Fred is Awaiting Your Answer")

        turbine_number = st.number_input('Turbine Number', min_value=0, max_value=100)

        st.markdown("""---""")

        if farm and turbine_number:
            coll21, coll22 = st.columns(2)
            coll21.metric("AC/DC Failure Rate", "0.4", "-0.1")
            coll22.metric("DC/AC Failure Rate ", "0.8", "+0.3")

            coll23, coll24 = st.columns(2)
            coll23.metric("AC/DC Variance", "0.2", "-0.2")
            coll24.metric("DC/AC Variance", "1.2", "+0.8")

            st.write('The 2. unit located in the first series of the DC/AC is about to break. '
                    'The most likely cause is humitidy. \n '
                     'Please input feedback if applicable.')


            response = st.text_input('Feedback')
            if response:
                st.write(fr"Thank you for your feedback on turbine {turbine_number} - {farm}. It is now stored on FRED's server!")




