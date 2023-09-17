import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import stats

st.set_page_config(page_title="The Past - The Past, The Present & The Future of Bitcoin.", page_icon="⌛",layout="wide")
# st.write(st.session_state["shared"])


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


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

BTCyearsTable = [stats.BTC_2009, stats.BTC_2010, stats.BTC_2011, stats.BTC_2012, stats.BTC_2013, stats.BTC_2014, stats.BTC_2015, stats.BTC_2016, stats.BTC_2017, stats.BTC_2018, stats.BTC_2019, stats.BTC_2020, stats.BTC_2021, stats.BTC_2022, stats.BTC_2023]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# for i in table:
#     for key, value in i.items():
#         if value != False:
#           if key == "Total Transactions Per Month":
#             for month, value in zip(months, value):
#               st.write(month, value)
#             # for j in value:
#               # CODE HERE

#           else:     
#             st.write(key, value)
##############################################################################
fontYear = '<font size ="+6">'
fontPrice = '<font size ="+5">$'
fontHashrate = '</br> <font size ="+5">'
endfont = '</font>'
for i in BTCyearsTable:

    col1, col2 = st.columns(2)
    with col1:
        st.write(fontYear, str(i["Year"]), "</font>", unsafe_allow_html=True)

        st.write("Lowest Price of the year", "</br>", fontPrice, str(i["Price Low"]), endfont, unsafe_allow_html=True)
        st.write("Highest Price of the year", "</br>", fontPrice,  str(i["Price High"]), endfont, unsafe_allow_html=True)

    with col2:
        if i["Halving Year"] == True:
            halvingyear = ":green[YES]"
        else:
            halvingyear = ":red[NO]"
    
        # st.write("Halving Occured in this Year? </br>", str(i["Halving Year"]), unsafe_allow_html=True)
        st.write("Halving Occured in this Year? </br>", halvingyear , unsafe_allow_html=True)

        st.write("Lowest Hashrate (In Exahashes)", fontHashrate, format(i["Hashrate Low"], ".16f"), endfont, unsafe_allow_html=True)
        st.write("Highest Hashrate (In Exahashes) ", fontHashrate, format(i["Hashrate High"], ".16f"), endfont, unsafe_allow_html=True)
        

    col1, col2 = st.columns(2)
    with col1:

        data = pd.DataFrame({
            'Month': months,
            'Total Transactions Per Month': i["Total Transactions Per Month"]
        })
        st.write(alt.Chart(data).mark_bar().encode(x=alt.X('Month', sort=None),y='Total Transactions Per Month'))
        # Horizontal :  st.write(alt.Chart(data).mark_bar().encode(y=alt.X('Month', sort=None),x='Total Transactions Per Month'))


    with col2: 
        hashrates = [i["Hashrate Low"], i["Hashrate High"]]
    
        data = pd.DataFrame({
            'Low / High': ["Low", "High"],
            'Hashrate (in Exahashes)': hashrates
        })

        #st.bar_chart(data, x="Low / High", y="Hashrates")
        st.write(alt.Chart(data).mark_bar().encode(x=alt.X('Low / High', sort=None),y='Hashrate (in Exahashes)'))
        #st.write(alt.Chart(data).mark_bar().encode(y=alt.X('Low / High', sort=None),x='Hashrates'))


    

    st.divider()    

##############################################################################

transactions_FullTable = []
date_FullTable = []

for i in BTCyearsTable:
    transactions_FullTable = transactions_FullTable + i["Total Transactions Per Month"]

years = [(str(d["Year"])) for d in BTCyearsTable]
newlist = [f"{month} {year}" for year in years for month in months]

data = pd.DataFrame({
    'Transactions': transactions_FullTable,
    'Date': newlist
})


c = alt.Chart(data).mark_bar().encode(
     x=alt.X('Date', sort=None),
     y='Transactions')

st.write("Bitcoin Years Table, mooo")
st.altair_chart(c, use_container_width=True)

##############################################################################













t = stats.nasdaqDataExtract("data/dl/MIREV_Bitcoin_Miners_Revenue_USD_(DAILY).json")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data = pd.DataFrame({
    'Data': t["2018"],
    'Months': months
})



c = alt.Chart(data).mark_bar().encode(
     x=alt.X('Months', sort=None),
     y='Data')

st.altair_chart(c, use_container_width=True)
# st.write(t["2018"])

###########################################



t = stats.nasdaqDataExtract("data/dl/MIREV_Bitcoin_Miners_Revenue_USD_(DAILY).json")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data = pd.DataFrame({
    'Data': t["2019"],
    'Months': months
})



c = alt.Chart(data).mark_bar().encode(
     x=alt.X('Months', sort=None),
     y='Data')

st.altair_chart(c, use_container_width=True)
#st.write(t["2019"])





# st.write(t["2019"][4])
# st.write(t["2019"])


# for i in t if t[0] == "2009"
#     st.write(i)
# # st.write(stats.nasdaqDataExtract("data/MIREV-Bitcoin Miners Revenue.json"))
