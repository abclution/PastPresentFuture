import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="References for The Past, The Present & The Future of Bitcoin.", page_icon="📚",layout="wide")
# st.write(st.session_state["shared"])


# https://medium.com/@gianlucamazza/bitcoin-security-budget-halving-and-the-system-mechanics-306ca91c695f
# https://dune.com/niftytable/bitcoin-security-budget
# https://www.btcsecuritybudget.com/
with st.expander("**Security Budget**", expanded=False):
    """
    ## Security Budget

    The term **"Security Budget"** typically refers to the resources and mechanisms allocated and spent to secure the Bitcoin network.

    It can be assessed in the simple economic terms of :green[Income] vs :red[Expenditures].

    ### :green[Income Items]
    - 💰 Block Reward, a reward of newly mined Bitcoin given to the winning miner, per block.
    - 🤑 Transaction Fees, users of Bitcoin pay a fee to send transactions.


    ### :red[Expenditures Items]
    - 🔌 Electricity Cost - the cost of running Bitcoin mining and associated hardware. *
    - 🖧 Hardware Purchases & Failures - ex. Bitcoin Mining Equipment, Air Conditioners, Wiring etc.
    - 💸 Rent, taxes, licenses, salaries and other wages for the running of the Bitcoin mining operation.

    ---
    - *In this presentation we will only consider "🔌 Electricity Cost" from the :red[Expenditures Items], as it is the majority costs of Bitcoin Mining operations. 
    
    - We will however consider all :green[Income Items] in the comparisons.


    ### :red[Simply put, if the cost of the Expenditures is greater than the Income, the Miners are running at a loss & not making a profit.]

    """

  