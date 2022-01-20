import streamlit as st
import yfinance as yf

st.header('Stock Price Data')

st.subheader('This page shows the prices of stocks')

list=['Select Stock','AAPL','AMZN','GOOGL','GOOG','TSLA','FB'
,'NVDA','V']

tickerSymbol = st.selectbox('Select Stock', list)
tickerData = yf.Ticker(tickerSymbol)
starting = st.date_input('Pick a starting Date')
ending = st.date_input('Pick an ending date')
#period = st.radio('Choose the Duration of Schemantics',('1d','1mo','1y'))
tickerDF=tickerData.history(period='1d', start=starting, end=ending)

st.markdown("""### Closing Data """)
st.line_chart(tickerDF.Close)
st.markdown("""### Volume Data """)
st.line_chart(tickerDF.Volume)