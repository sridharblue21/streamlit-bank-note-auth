import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

st.title('Hello World! :sunglasses: :blush:')
st.write('My name is Sridhar')
st.write(pd.DataFrame({
    'column1' : ['Name', 2, 'Sri'],
    'column2' : [1,2,3],
}))

'''
# Hello World! :blush:
My name is Sridhar :sunglasses:
'''
df = pd.DataFrame({
    'column1' : ['Name', 2, 'Sri'],
    'column2' : [1,2,3],
})
df

x = 21
'x', x  # <-- Draw the string 'x' and then the value of x


st.title('TEST')
st.header('TEST')
st.subheader('TEST')
st.markdown('TEST :flag-in: :+1:')
st.write('TEST')
st.text('TEST :+1:')
st.markdown('Streamlit is **_really_ cool**.')
st.latex(r'\overleftarrow{AB}')

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.title('Chart using Random.randn')
df1 = (pd.DataFrame(
    np.random.randn(10,3),
    columns=['a', 'b', 'c']
))

df1
st.line_chart(df1)

c = alt.Chart(df1).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
     df['column1']
)

'You selected: ', option

# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['column1']
# )

# 'You selected: ', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    st.balloons()

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

txt = st.empty()
bar = st.progress(0)

for i in range(100):
    txt.text(f'{i+1}%')
    bar.progress(i+1)
    time.sleep(.10)

'Task Completed'
st.balloons()

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


# progress_bar = st.progress(0)
# status_text = st.empty()
# chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     # Update progress bar.
#     progress_bar.progress(i + 1)

#     new_rows = np.random.randn(10, 2)

#     # Update status text.
#     status_text.text(
#         'The latest random number is: %s' % new_rows[-1, 1])

#     # Append data to the chart.
#     chart.add_rows(new_rows)

#     # Pretend we're doing some computation that takes time.
#     time.sleep(0.1)

# status_text.text('Done!')
# st.balloons()
