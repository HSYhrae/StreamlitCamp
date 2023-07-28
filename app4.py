import plotly.graph_objects as go 
import pandas as pd 
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
# 레이아웃 참조할 때 좋은 내용들 (사이드바, 날짜 입력, 주식 차트 작성)

# txt 파일 불러오고
# 전체 데이터를 리스토로 변환
# 하나의 리스트를 

def main():
    st.title("주식 데이터")
    st.sidebar.title("Stock Chart")
    ticker = st.sidebar.text_input("Enter a ticker (e. g. AAPL)", value="AAPL") # ticker는 주식 종목이다.
    # 위 코드에서 .sidebar만 빼면 메인화면 같은 내용이 출력된다.
    # ticker = st.text_input("Enter a ticker (e. g. AAPL)", value="AAPL")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')
    start_date = st.sidebar.date_input("시작 날짜: ", value=pd.to_datetime("2019-01-01"))
    end_date = st.sidebar.date_input("종료 날짜: ", value=pd.to_datetime("today"))

    data = yf.download(ticker, start=start_date, end=end_date)
    st.dataframe(data)

    # Line Chart, Candlestick 
    chart_type = st.sidebar.radio("Select Chart Type", ("Candlestick", "Line")) 
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')

    if chart_type == "Candlestick":
        fig = go.Figure(candlestick)
    elif chart_type == "Line":
        fig = go.Figure(line) 
    else:
        st.error("error")
    
    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)
    num_row = st.sidebar.number_input("Number of Rows", min_value=1, max_value=len(data))
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index("Date"))

    value1 = st.sidebar.slider('1숫자 선택', 0, 100)
    st.sidebar.write(value1)

    with st.sidebar:
        value2 = st.slider('2 숫자 선택', 0, 100)
        st.write(value2)

    with st.sidebar:
        st.markdown('### 사이드바에 시각화 코드 추가')
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        st.pyplot(fig)

if __name__ == "__main__":
    main()