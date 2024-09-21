import streamlit as st
import pandas as pd
import numpy as np



# First dataset
df = pd.DataFrame({'first column': [1,2,3,4], 'second colomn': [10,20,30,40]})

st.write("Here's our first attempt at using data to creat a table:")
st.write(pd.DataFrame({'first column': [1,2,3,4], 'second colomn': [10,20,30,40]}))

st.table(df)


# second dataset 
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# plot dataframe
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0).highlight_min(axis=0))

# plot line chart 
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# plot map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# widgets 

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

y = st.button('x')
st.write(y, 'say', 10)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
# with left_column:
#     greet = st.button('Press me!')
#     st.write(greet, 'hello')

left_column.button('Press me!')

    

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
    
    
import time 

latest_iteration  = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
  
""" 
@st.cache_data
def long_running_function(param1, param2):
    return …
"""


"""
Examples of using Session State
Here's a simple app that counts the number of times the page has been run. 
Every time you click the button, the script will rerun.
"""



# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# st.session_state.counter += 1

# st.header(f"This page has run {st.session_state.counter} times.")
# st.button("Run it again")

# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)


"""
Connections
As hinted above, you can use @st.cache_resource to cache connections. This is the most general solution which allows you to use almost any connection from any Python library. 
However, Streamlit also offers a convenient way to handle some of the most popular connections, like SQL! st.connection takes care of the caching for you so you can enjoy fewer lines of code. 
Getting data from your database can be as easy as:

"""



# conn = st.connection("my_database")
# df = conn.query("select * from my_table")
# st.dataframe(df)

"""Of course, you may be wondering where your username and password go. Streamlit has a convenient mechanism for Secrets management. For now, let's just see how st.connection works very nicely with secrets. In your local project directory, you can save a .streamlit/secrets.toml file. You save your secrets in the toml file and st.connection just uses them! For example, if you have an app file streamlit_app.py your project directory may look like this:

your-LOCAL-repository/
├── .streamlit/
│   └── secrets.toml # Make sure to gitignore this!
└── streamlit_app.py
For the above SQL example, your secrets.toml file might look like the following:

[connections.my_database]
    type="sql"
    dialect="mysql"
    username="xxx"
    password="xxx"
    host="example.com" # IP or URL
    port=3306 # Port number
    database="mydb" # Database name
Since you don't want to commit your secrets.toml file to your repository, you'll need to learn how your host handles secrets when you're ready to publish your app. Each host platform may have a different way for you to pass your secrets. If you use Streamlit Community Cloud for example, each deployed app has a settings menu where you can load your secrets. After you've written an app and are ready to deploy, you can read all about how to Deploy your app on Community Cloud.


"""



st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


st.subheader('Raw data')
st.write(df)

st.subheader('Number of pickups by hour')



if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    
"""

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
# with left_column:
#     greet = st.button('Press me!')
#     st.write(greet, 'hello')

left_column.button('Press me!')"""


# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# def click_button():
#     st.session_state.clicked = True

# st.button('Click me', on_click=click_button)

import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)