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
user_menu = st.sidebar.radio("User Menu", ('FQ Performance - Turbine Level',
    'FQ Performance - Farm Overview', 'Parameter Sharing', 'Meet FRED'))

if user_menu == 'FQ Performance - Farm Overview':
    st.title("'Fnattenfall' Wind Farm Overview")

    data = {'WT SITE': ['WH003', 'WH001', 'SH505', 'KL403'],
            'DoB': ['07/07/2023', '01/01/2005', '01/05/2018', '15/12/2014'], 'Turbines': [60.0, 107.0, 25.0, 38.0],
            'Average WT Failure Rate': np.random.uniform(0.3, 0.7, 4), 'Variance in Failure Rates': np.random.uniform(
            0.10, 0.90, 4), 'Certainty level': [1, 3, 4, 6]}

    df = pd.DataFrame(data)
    st.dataframe(df)

    farm1 = st.selectbox("Select Wind Farm", ('WH003', 'WH001', 'SH505', 'KL403'), index=None,
                        placeholder="Fred is Awaiting Your Answer")

    st.markdown('---')
    if farm1:
        fail_value = df[df['WT SITE']==farm1]['Average WT Failure Rate'].values

        col1, col2 = st.columns(2)
        with col1:
            st.subheader('FR Estimates')
            sns.set()


            def partial_cum_returns(start, cum_returns, fail_value):
                return fail_value * cum_returns.loc[start:].div(cum_returns.loc[start])


            index = pd.DatetimeIndex(pd.date_range('20230707', '20250707', freq='W'))
            np.random.seed(5)

            returns = pd.Series(np.exp(np.random.normal(loc=0, scale=0.05, size=len(index))), index=index)
            cum_returns = returns.cumprod()
            df = pd.DataFrame(index=index)

            for date in index:
                df[date] = partial_cum_returns(date, cum_returns, fail_value)
            fig = df.plot(legend=False, colormap='viridis').figure
            plt.ylabel('Failure Rate Estimations')
            fig.patch.set_facecolor('#5D5DB1')
            st.pyplot(fig)
        with col2:
            st.subheader('Storage Supply')
            col21, col22 = st.columns(2)
            numberofunits = st.empty()
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
    with coll2:
        st.image("gallery/wind.webp")
    with coll1:
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


if user_menu == "Parameter Sharing":
    st.subheader("Summary on the Latest Set of Parameters Shared")
    st.code("""{
  "encrypted_data": "8j2N#L!eAtfKmY2Qw8*7Uz1sBpXvIeFg$",
  "cipher": "AES-256",
  "iv": "oP9aEh7KmL3zQw7s",
  "key": "a0b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7",
  "timestamp": "2023-10-17T12:34:56",
  "user_id": "123456",
  "file_name": "document.pdf",
  "permissions": {
    "read": true,
    "write": false,
    "delete": false
  },
  "metadata": {
    "author": "Automatic",
    "creation_date": "2023-10-15",
    "size": "2.5 MB"
  }
}""", language='python')

    st.subheader("Upload Manual Revisited Parameters")
    uploaded_file = st.file_uploader("Choose a file")

if user_menu == 'Meet FRED':
    st.image(fr'gallery/pink-logo.png')

    st.subheader("Core Company Values")
    st.markdown(
        """
        FRED one-liner. The core company values lie in:
        - Put competitive advantage first. Start with a winning, scalable formula.
        - Be a local hero. Commit to winning on the home front.
        - Look beyond the core. Nurture growth in adjacent business areas.
        """
    )

    st.subheader("View All FRED's Partners")
    collu1, collu2, collu3 = st.columns(3)

    with collu1:
        st.image(fr'gallery/strath.png')
    with collu2:
        st.image(fr'gallery/se.jpg')
    with collu3:
        st.image(fr'gallery/your_logo_here.png')


