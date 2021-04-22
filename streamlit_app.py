import yfinance as yf
import streamlit as st


Start = '2006-12-31'

End = "2020-1-1"


st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google and Apple!
""")


st.write("""
### Google Stock Price
""")


Stock_Symbol = 'GOOGL'

Stock_Data = yf.Ticker(Stock_Symbol)

Stock_Df = Stock_Data.history(period='1d', start=Start, end=End)

st.write("""
#### Closing Price
""")
st.line_chart(Stock_Df.Close)
st.write("""
#### Volume Price
""")
st.line_chart(Stock_Df.Volume)


st.write("""
### Apple Stock Price
""")

Stock_Symbol_1 = 'AAPL'

Stock_Data_1 = yf.Ticker(Stock_Symbol)

Stock_Df_1 = Stock_Data_1.history(period='1d', start=Start, end=End)

st.write("""
#### Closing Price
""")
st.line_chart(Stock_Df_1.Close)
st.write("""
#### Volume Price
""")
st.line_chart(Stock_Df_1.Volume)


Facebook = "FB"

st.write("""
### Faebook.Inc Stock Price
""")

Stock_Symbol_2 = Facebook

Stock_Data_2 = yf.Ticker(Stock_Symbol_2)

Stock_Df_2 = Stock_Data_2.history(period='1d', start=Start, end=End)


st.write("""
#### Closing Price
""")
st.line_chart(Stock_Df_2.Close)
st.write("""
#### Volume Price
""")
st.line_chart(Stock_Df_2.Volume)

Amazon = "AMZN"
st.write("""
### Amazon Stock Price
""")

Stock_Symbol_3 = Amazon

Stock_Data_3 = yf.Ticker(Stock_Symbol_3)

Stock_Df_3 = Stock_Data_3.history(period='1d', start=Start, end=End)


st.write("""
#### Closing Price
""")
st.line_chart(Stock_Df_3.Close)
st.write("""
#### Volume Price
""")
st.line_chart(Stock_Df_3.Volume)
