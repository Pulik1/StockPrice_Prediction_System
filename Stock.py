import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import pandas_datareader as data
# from keras.models import load_model
import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
def app():
    #st.set_page_config(page_title="Stocker.com", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None,)

    st.write("Welcome to Stocker")
    
    end='2019-12-31'

    start='2010-01-01'
    today=date.today().strftime("%Y-%m-%d")

    #st.title("Stock Trend App")
    ticker=st.text_input('Search',value="AAPL")
    start_date=st.date_input('Start Date')
    end_date=st.date_input('End Date')
    # stocks=("AAPL","GOOG","MSFT","TATAPOWER.NS")
    # selected_stocks=st.selectbox("Select dataset for prediction",stocks)

    n_years=st.slider("Year of prediction:",1,4)
    period=n_years*365
    def load_data(ticker):
       data=yf.download(ticker,start=start_date,end=end_date)
       data.reset_index(inplace=True)
       return data
    data_load_state = st.text("load data...")
    data=load_data(ticker)
    data_load_state.text("Loading data...done!")

    st.subheader("Raw Data")
    st.write(data.tail())

    def plot_raw_data():
        fig=go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name='stock_close'))
        fig.layout.update(title_text="Time Serious Data",xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    plot_raw_data()

    df_train=data[['Date','Close']]
    df_train=df_train.rename(columns={"Date":"ds","Close": "y"})

    m=Prophet()
    m.fit(df_train)
    future=m.make_future_dataframe(periods=period)
    forecast=m.predict(future)

    st.subheader("Forecast Data")
    st.write(forecast.tail())

    st.write('Forecast data')
    fig1=plot_plotly(m,forecast)
    st.plotly_chart(fig1)

    st.write('Forecast Components')
    fig2=m.plot_components(forecast)
    st.write(fig2)

# user_input=st.text_input('Enter Stock Ticker','AAPL')
# df=data.DataReader(user_input,'yahoo',start,end)

# st.subheader('Data from 2010-2019')
# st.write(df.describe())
