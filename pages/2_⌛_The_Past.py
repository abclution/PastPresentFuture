import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="The Past - The Past, The Present & The Future of Bitcoin.", page_icon="⌛",layout="wide")
# st.write(st.session_state["shared"])

# SOURCE: https://www.zenledger.io/blog/bitcoin-halving/
"""
Bitcoin Halving Dates So Far
Let’s quickly take a look at the previous Bitcoin halving events and patterns.

2012 Bitcoin Halving
The first halving happened on November 28th, 2012.

New Bitcoin per block (Before): 50 BTC per block
New Bitcoin per block (After): 25 BTC per block
Price on Halving Day: $12.35
Price 150 Days Later: $127.00
2016 Bitcoin Halving
The second halving occurred on July 9th, 2016.

New Bitcoin per block (Before): 25 BTC per block
New Bitcoin per block (After): 12.5 BTC per block
Price on Halving Day: $650.63
Price 150 Days Later: $758.81
2020 Bitcoin Halving
The third halving occurred on May 11, 2020.

New Bitcoin per block (Before): 12.5 BTC per block
New Bitcoin per block (After): 6.25 BTC per block
Price on Halving Day: $8821.42
Price 150 Days Later: $10,943.00
"""
"""https://www.sofi.com/learn/content/bitcoin-price-history/"""

"""Since Genesis, the birth of Bitcoin, a lot of time has passed. But some interesting history is contained in our past. Lets take a look at some of the most significant events in Bitcoin's history."""

Hash = 1000000000000000000
KiloHash = 1000000000000000
MegaHash = 1000000000000
GigaHash = 1000000000
TeraHash = 1000000
PetaHash = 1000
ExaHash = 1
ZettaHash = 0.001

BTC_2016 = {
  "Year": 2016,
  "Halving Year": True,
  "Halving Date": "2016/07/09",
  "Price Low": 354.91,
  "Price High": 979.40,
  "Hashrate Low": 704.5287/PetaHash,
  "Hashrate High": 901.8396/PetaHash,
  "Price Halving Day": 1,
  "Price 150 Days after Halving ": 1,
  "Electricity Cost Low": .002,
  "Electricity Cost High":.002,
  "Total Transactions Per Month": [3222667815.0, 3197059649.0, 3614175762.0, 3679821049.0, 4010506108.0, 4085450658.0, 4427875464.0, 4639959698.0, 4692856221.0, 5068934668.0, 5134596926.0, 5568056206.0]
  }

for key, value in BTC_2016.items():
    st.write(key, value)

BTC_2009 = {
  "Year": 2009,
  "Halving Year": False,
  "Halving Date": False,
  "Price Low": 0.0,
  "Price High": 0.0,
  "Hashrate Low": 462.433/KiloHash,
  "Hashrate High": format(12.5763/MegaHash,".20f"),
  "Price Halving Day": False,
  "Price 150 Days after Halving ": False,
  "Electricity Cost Low": .002,
  "Electricity Cost High":.002,
  "Total Transactions Per Month": [29068.0, 123819.0, 241866.0, 338216.0, 458489.0, 524159.0, 611848.0, 662271.0, 695197.0, 786238.0, 824272.0, 945146.0]
  }

# format(BTC_MaxBillableBytes * BTC_SatoshisPerByte, ".8f")

for key, value in BTC_2009.items():
    st.write(key, value)