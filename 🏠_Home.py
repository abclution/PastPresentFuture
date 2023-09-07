import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Home - The Past, The Present & The Future of Bitcoin.", page_icon="🏠",layout="wide")

colorBTC = "#F2A900"
colorBCH = "#0AC18E"
seconds_per_day = 86400


###############################################################################
st.sidebar.write(
    '<font size="+5">Max. TPS',
    "</font>",
    "</br>",
    "(Maximum Transactions per Second, Full Blocks)",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BTC_TPS = ":orange[BTC Network] *(Default: 7)*"
slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS, 1, 7, 7, 1, format_slider_TPS)

max_daily_transactions_BTC = seconds_per_day * slider_BTC_TPS

#### BCH TPS SLIDER  ##########################################################
format_slider_TPS = "%d"
label_BCH_TPS = ":green[BCH Network] *(Default: 224)*"
slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS, 1, 10000, 224, 1, format_slider_TPS)

max_daily_transactions_BCH = seconds_per_day * slider_BCH_TPS
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Hashrate',
    "</font>",
    "</br>",
    "(Current hashrate in exa-hashes, 7 Day AVG.)",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BTC = ":orange[BTC Network] *(Default: 402.2)*"
slider_exaHashes_BTC = st.sidebar.slider(
    label_exaHashes_BTC, 1.0, 1000.0, 402.2, 0.1, format_slider_exaHashes
)

#### BCH HASHRATE SLIDER  #####################################################
format_slider_exaHashes = "%d"
label_exaHashes_BCH = ":green[BCH Network] *(Default: 2.67)*"
slider_exaHashes_BCH = st.sidebar.slider(
    label_exaHashes_BCH, 1.0, 1000.0, 2.67, 0.1, format_slider_exaHashes
)
###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Energy Usage in TwH',
    "</font>",
    "</br>",
    "(Yearly energy usage of entire network in Terrawatt Hours, found here, https://ccaf.io/cbnsi/cbeci )",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC ENERGY USAGE SLIDER  #################################################
format_slider_energyUsageYearlyTwH = "%d"
label_energyUsageYearlyTwH_BTC = ":orange[BTC Network] *(Default: 145.02)*"
slider_energyUsageYearlyTwH_BTC = st.sidebar.slider(
    label_energyUsageYearlyTwH_BTC,
    1.0,
    1000.0,
    145.02,
    0.1,
    format_slider_energyUsageYearlyTwH,
)

#### BCH ENERGY USAGE SLIDER  #################################################
# ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.

# Convert BTC Yearly TwH to KwH, this is because most other calculations are
# done based on the cost of each KwH.
energyUsageYearlyKwH_BTC = slider_energyUsageYearlyTwH_BTC * 1000000000

# Get an energy usage ratio by getting the BTC hashrate and its yearly KwH
exaHashToYearlyKwHRatio = energyUsageYearlyKwH_BTC / slider_exaHashes_BTC

# Multiply the BCH exahashes by the energy usage ratio, this assumes equivalent
# efficiency between the chains equipment. This is a fair comparison.
energyUsageYearlyKwH_BCH = slider_exaHashes_BCH * exaHashToYearlyKwHRatio

# Get BCH yearly TwH used
energyUsageYearlyTwH_BCH = energyUsageYearlyKwH_BCH / 1000000000

st.sidebar.write(
    "The energy usage of the BCH network is proportional based on its hashrate in comparison to BTC's energy usage and hashrate."
)

###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Prices in USD',
    "</font>",
    "</br>",
    "(Not yet updated dynamically )",
    unsafe_allow_html=True,
)
###############################################################################
#### BTC PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBTC = ":orange[BTC Network] *(Default: 26091.70)*"

slider_PriceBTC = st.sidebar.slider(
    label_priceBTC, 1.0, 100000.0, 26091.70, 0.1, format_slider_Price
)

#### BCH PRICING SLIDER  ######################################################
format_slider_Price = "%d"
label_priceBCH = ":green[BCH Network] *(Default: 190.02)*"

slider_PriceBCH = st.sidebar.slider(
    label_priceBCH, 1.0, 100000.0, 190.02, 0.1, format_slider_Price
)

###############################################################################
st.sidebar.divider()
###############################################################################


###############################################################################
st.sidebar.write(
    '<font size="+5">Block Reward',
    "</font>",
    "</br>",
    "(Amount of Bitcoins awarded as prize for mining.)",
    unsafe_allow_html=True,
)
###############################################################################
#### BLOCK REWARD SELECTOR (BOTH)  ############################################

blockReward = st.sidebar.selectbox(
    "Choose block reward *(Default: 6.25)*",
    (50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.195325, 0.09765625, 0),
    3,
)

# (6 blocks per hour * 24 hours) * (block reward)
totalDailyBlockRewards = (6 * 24) * blockReward
###############################################################################

###############################################################################
st.sidebar.divider()
###############################################################################
###############################################################################
st.sidebar.write(
    '<font size="+5">Chart Settings',
    "</font>",
    "</br>",
    "(Settings that control the scale of the chart. Helpful for zooming in.)",
    unsafe_allow_html=True,
)
###############################################################################


# st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
start_value = st.sidebar.number_input(
    "Lowest Electricity Price, KwH (Default: .007)",
    0.001,
    0.50,
    0.007,
    0.001,
    "%f",
    help="Lowest KwH value for charts. Min. .001",
)
end_value = st.sidebar.number_input(
    "Highest Electricity Price, KwH (Default: .25)",
    0.001,
    0.50,
    0.25,
    0.001,
    "%f",
    help="Highest cost per KwH for charts. Max. .50",
)
step = st.sidebar.number_input(
    "Stepping for Charts (Default: .001)",
    0.001,
    0.50,
    0.001,
    0.001,
    "%f",
    help="Stepping for chart generation.",
)


# start_value = 0.007
# end_value = 0.35
# step = 0.001
#### MAIN START  #############################################################

col1, col2 = st.columns(2)
with col1:
    """# The Past, The Present, & The Future of Bitcoin. """

with col2:
    """ col2 """


"""
#### A presentation & simulation of the economics and usability of Bitcoin as it was, as it is today, and as may be in the future.

This is meant as a tool for anyone who wants to simulate the economic & end user reality of Bitcoin(s) with an (somewhat) rigorous analysis of the most important aspects of Bitcoin. 

As this application is both a presentation as well as a tool, the intended way to progress is by going through each section of the presentation, and then going through the suggested exercises.
If you are both math inclined or know your Bitcoin history, some of the excersices may be redundant or pointless for you.
The intent of the excersizes is to slowly build a picture and a complete understanding behind the math and economics which is presented via the charts.

### How to use this tool

#### Settings & Options Sidebar
- On first open of this tool you should be reading this text as well as a visible sidebar menu on the left hand of your screen with various sliders and options.
- If this sidebar is missing, please press the button at the uppermost top left that should look like ">". 
    - On mobile this menu is collapsed on start due to space constraints.
- Any changes made to the settings in the sidebar menu will immediately take effect on both the numbers and charts throughout the presentation.
- The sidebar has more than a full screen worth of options, please make sure to scroll fully down to validate you have seen all availiable settings.
- It is suggested before adjusting any options, to go on to each section carefully and read the information and perform any of the "Suggested Excercises"
- To reset all options to defaults, please refresh the page. All default options are set to the actual current numbers of each network, August 2023.

#### Charts
- Charts can be clicked on to full screen them, mouse wheel to zoom in/out. You can also hover over each line/point to see more detailed information. They can also be exported to various formats.
- Additionally the data used to derive the charts should be availiable in the tab next to each chart, as well as the formula used to derive the datasets.
- The entirety of the source code used to generate this page is also available.

#### Definitions

In order to be effectively terse in the display of information and data, it is necessary to define some terms and some ideas.
Please take a minute to read through the definitions in this section.
If you are already highly familiar with Bitcoin, blockchain and related technologies, you can skip this section.

"""