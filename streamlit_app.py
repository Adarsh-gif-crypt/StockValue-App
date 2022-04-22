import streamlit as st
import yfinance as yf
from datetime import date
from prophet import Prophet
from plotly import graph_objs as go
from prophet.plot import plot_plotly

st.set_page_config(layout='wide')

images0,image1,images1 = st.columns((2.5,6,2))
image1.image('https://miro.medium.com/max/620/0*dunTLlei47QWR7NR.gif')
alpha, beta, gamma = st.columns((4,5,3))
beta.title('Stock Price Prediction')


alpha1, gamma1 = st.columns(2)

alpha1.markdown('Hello and Welcome to Stock Price Predictor. This WebApp is designed to predict the price of select stocks. To get started, Select a stock from the given list and select the starting date and ending date for the same to view its information.')
gamma1.markdown('Stock price prediction is a very researched entity in the modern day world. It helps companies to raise capital, it helps people generate passive income, stock markets represent the state of the economy of the country and it is widely used soutce for people to invest money in companies with high growth potential')
list=['Select Stock','AAPL','AMZN','GOOGL','GOOG','TSLA','FB'
,'NVDA','V']

sbs,sb,sbs1 = st.columns(3)
tickerSymbol = sb.selectbox('Select Stock', list)
tickerData = yf.Ticker(tickerSymbol)

st.markdown("""=======================================================================================================================================================""")


alpha2,gamma2 = st.columns(2)
starting = alpha2.date_input('Pick a starting Date')
ending = gamma2.date_input('Pick an ending date')


rhs, rh, rhs1 = st.columns((2.5,3,2))
rh.markdown("""### Let's have a look at some raw data""")
#period = st.radio('Choose the Duration of Schemantics',('1d','1mo','1y'))

def load_data(ticker):
    data = yf.download(ticker, starting, ending)
    data.reset_index(inplace=True)
    return data
data = load_data(tickerSymbol)
rds, rd, rds1 = st.columns((1,5,1))
rd.write(data)

tickerDF=tickerData.history(period='1d', start=starting, end=ending)


graphs1, graphs3 = st.columns(2)
graphs1.markdown("""### Opening Price """)
graphs1.line_chart(tickerDF.Open)
graphs3.markdown("""### Volume Price """)
graphs3.line_chart(tickerDF.Volume)
graphs1.markdown("""### Closing Price """)
graphs1.line_chart(tickerDF.Close)
graphs3.markdown("""### Highest Price """)
graphs3.line_chart(tickerDF.High)
graphs1.markdown("""### Lowest Price""")
graphs1.line_chart(tickerDF.Low)
graphs3.markdown("""### Adjusted Closing Price """)
graphs3.line_chart(data['Adj Close'])


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

@st.cache
def load_data1(ticker):
    data1 = yf.download(ticker, START, TODAY)
    data1.reset_index(inplace=True)
    return data1

data1 = load_data1(tickerSymbol)
#st.write(data1)

df_train = data1[['Date','Close']]
df_train = df_train.rename(columns = {'Date':'ds','Close':'y'})
#st.write(df_train)

predictor = Prophet()
predictor.fit(df_train)

st.markdown("""## Please Select the number of years for the predicted trends""")

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365
future = predictor.make_future_dataframe(periods = period)
forecast = predictor.predict(future)

fcs2 , afc, fcs3 = st.columns(3)
# Show and plot forecast
afc.title('Forecast data')
#st.write(forecast.tail())
    
afc.markdown(f'Forecast plot for {n_years} following years')
fig1 = plot_plotly(predictor, forecast)
st.plotly_chart(fig1)


fcs,fch,fcs1 = st.columns(3)
fch.markdown("""## Forecated Components""")
fig2 = predictor.plot_components(forecast)
st.write(fig2)

st.caption('Made with ❤')