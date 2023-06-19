import streamlit as st
import pandas as pd
import time 
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

now = datetime.now()
time = now.strftime('%I:%M:%S:%p')
date = now.strftime('%d-%B-%Y')

# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# The function returns a counter for number of refreshes. This allows the
# ability to make special requests at different intervals based on the count
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")


df=pd.read_csv("Attendance-inout.csv", header=None)
df.columns=['Name','Check-in','Check-out','Date']


st.dataframe(df.style.highlight_max(axis=0, color='lightyellow'), hide_index=None, column_order=('Date', 'Name','Check-in','Check-out'))