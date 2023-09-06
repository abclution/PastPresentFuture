import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="The Playground - The Past, The Present & The Future of Bitcoin.", page_icon="🚸",layout="wide")
st.write(st.session_state["shared"])
