import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def main():
    st.title('확인')
    with st.sidebar:
        st.header('Sidebar')
        day = st.selectbox('요일 선택', ['Thur', 'Fri', 'Sat', 'Sun'])

    tips = sns.load_dataset('tips')
    filtered_tips = tips.loc[tips['day'] == day]
    top_bill = filtered_tips['total_bill'].max()
    top_tip = filtered_tips['tip'].max()

    # tab1, tab2, tab3 = st.sidebar.tabs(['Total Bill', 'Tip', 'Size'])
    tab1, tab2, tab3 = st.tabs(['Total Bill', 'Tip', 'Size'])
    with tab1:
        fig, ax = plt.subplots()
        st.header('Total Bill')
        sns.histplot(filtered_tips['total_bill'], kde=False, ax=ax)
        st.pyplot(fig)

    with tab2:
        st.metric('최고 영수증', top_bill)

if __name__ == '__main__':
    main()