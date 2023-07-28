import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
# 함수 만들고 docstring 필수!
def calculate_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

iris = sns.load_dataset('iris')

def plot_matplotlib(): # 산점도 코드
    st.title('Scatter Plot with Matplotlib')
    fig1, ax = plt.subplots()
    ax.scatter(x = iris['sepal_length'], y = iris['sepal_width'])
    st.pyplot(fig1)


def plot_seaborn(): # 산점도 코드
    st.title('Scatter Plot with Seaborn')
    fig2, ax = plt.subplots()
    sns.scatterplot(data = iris, x = 'sepal_length', y = 'sepal_width', ax=ax)
    st.pyplot(fig2)



def plot_plotly():
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = iris['sepal_length'],
                   y = iris['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)

def main():
    st.title("오후 수업")

    price = st.slider('단가: ', 1000, 10000, value = 5000)
    total_sales = st.slider('전체 판매 갯수', 1, 1000, value = 500)

    st.write(price, total_sales)

    if st.button('매출액 계산'):
        result = calculate_sales_revenue(price, total_sales)
        st.write(f'전체 매출액은 {result:,} 원(KRW)') # 1000단위 쉼표 출력해보기

    
    # 체크박스
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox('시각화 보여주기') # True/False 값을 출력하는 문장
    st.write(show_plot)
    fig, ax = plt.subplots()
    ax.plot(x, y)

    if show_plot:
        st.pyplot(fig)

    st.write('-' * 50)
    plot_type = st.radio(
        '어떤 스타일의 산점도를 보고 싶으세요?',
        ('matplotlib', 'seaborn', 'plotly')
    )
    st.write(plot_type)
    if plot_type == 'matplotlib':
        plot_matplotlib()
    elif plot_type == 'seaborn':
        plot_seaborn()
    elif plot_type == 'plotly':
        plot_plotly()
    else:
        st.error('에러')

    st.write('-' * 50)
    
    # selectbox
    st.markdown('## Raw Data')
    st.dataframe(iris)

    st.markdown('<hr>', unsafe_allow_html=True) # <hr> html 문법에서 수평 가로선을 의미
    st.markdown('### Selectbox')
    col_name = st.selectbox('1개의 종을 선택하세요!', iris['species'].unique())
    st.write(col_name)

    result = iris.loc[iris['species'] == col_name].reset_index(drop=True)
    st.dataframe(result)

    fig2, ax = plt.subplots()
    sns.scatterplot(data = result, x = 'sepal_length', y = 'sepal_width', ax=ax)
    ax.set_title(col_name)
    st.pyplot(fig2)

    # MultiSelect
    cols = st.multiselect('복수의 컬럼 선택', iris.columns)
    st.write(cols)
    filter_iris = iris.loc[:, cols]
    st.dataframe(filter_iris)



if __name__ == '__main__':
    main()
