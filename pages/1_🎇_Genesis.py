import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Genesis - The Past, The Present & The Future of Bitcoin.", page_icon="🎇",layout="wide")
# st.write(st.session_state["shared"])
"""# Darkness"""

"""
In the inception of our tale, the stage was set with the existence of Fiat currencies, colloquially known as "Money by Decree." Near worthless value metal coins & paper, serving as mere symbols of wealth and value, mandated for use by the populace in their everyday transactions.

For those who grasped the profound realities surrounding Fiat currencies, they wisely allocated their wealth into tangible assets such as land and precious metals like gold. Yet, the inconvenience of lugging around sacks of gold ranged from bothersome when purchasing a simple coffee to utterly impractical when buying from Amazon or paying for Netflix subscriptions.

It became evident that a slew of issues plagued these Fiat-based economies. From the deliberate and planned inflation embedded within Fiat systems to the blatant manipulation of the money supply, the common individual found themselves grappling with a profound lack of trust in the very currency they relied upon. Wave after wave of recession, and even full-blown economic collapses in the dominion of centralized Fiat currencies, left the ordinary person at the mercy of the whims of irresponsible bankers and fraudulent governments. 

Nonetheless, amidst this quagmire of doubt and inconvenience, there remained no alternative that could be deemed both trustworthy and practical.


"""


"""# Genesis"""
col1, col2 = st.columns(2)

with col1:
    """
    ## October 31, 2008
    
    - The Bitcoin whitepaper was released by Satoshi Nakamoto in a cryptography mailing list.
    
    - The title of the paper was "Bitcoin: A Peer-to-Peer Electronic Cash System
    
    - In 9 short pages, this paper written by Satoshi Nakamoto:
        - Solved a long standing mathematical problem, The Byzantine General problem.
        - Outlined the technology and structure for an entirely new digital currency that defied the idea of Fiat currencies.
        - And defined this new currency Bitcoin, to be free of centralized authorities and to be free and permission-less for the whole world to use."""

with col2:
    st.image("images/Bitcoin_Whitepaper.png")

col1, col2 = st.columns(2)

with col1:
    """
    ### January 3, 2009
    
    - Satoshi Nakamoto released the first version of Bitcoin software and invited others to start participating.
    - The Genesis block for the Bitcoin network was created including a message: \
    
    
    **The Times 03/Jan/2009 Chancellor on brink of second bailout for banks**


    - This message forever cementing the position that the realm of currencies are no longer soley at the whims of irresponsible bankers and fraudulent governments. 
    - Bitcoin is a currency for the people, by the people and we don't need their permission! (Also we pass on built in inflation, thanks.)"""

with col2:
    st.image("images/TheTimes03-Jan-2009-Chancellor-on-brink-of-second-bailout-for-banks.jpg")