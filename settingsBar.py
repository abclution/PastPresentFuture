import streamlit as st
import pandas as pd
import numpy as np

colorBTC = "#F2A900"
colorBCH = "#0AC18E"
seconds_per_day = 86400


def slider_tps_label():
    st.sidebar.write(
        '<font size="+5">Max. TPS',
        "</font>",
        "</br>",
        "(Maximum Transactions per Second, Full Blocks)",
        unsafe_allow_html=True,
    )

    # * USAGE: settingsBar.slider_tps_label()

def slider_tps_btc():
    #### BTC TPS SLIDER  ##########################################################
    format_slider_TPS = "%d"
    label_BTC_TPS = ":orange[BTC Network] *(Default: 7)*"
    slider_BTC_TPS = st.sidebar.slider(label_BTC_TPS, 1, 7, 7, 1, format_slider_TPS)

    max_daily_transactions_BTC = seconds_per_day * slider_BTC_TPS
    return slider_BTC_TPS, max_daily_transactions_BTC

    # * USAGE: slider_BTC_TPS, max_daily_transactions_BTC = settingsBar.slider_tps_btc()

def slider_tps_bch():
    #### BCH TPS SLIDER  ##########################################################
    format_slider_TPS = "%d"
    label_BCH_TPS = ":green[BCH Network] *(Default: 224)*"
    slider_BCH_TPS = st.sidebar.slider(label_BCH_TPS, 1, 10000, 224, 1, format_slider_TPS)

    max_daily_transactions_BCH = seconds_per_day * slider_BCH_TPS
    return slider_BCH_TPS, max_daily_transactions_BCH

    # * USAGE: slider_BCH_TPS, max_daily_transactions_BCH = settingsBar.slider_tps_bch()



def slider_hashrate_label():
    st.sidebar.write(
        '<font size="+5">Hashrate',
        "</font>",
        "</br>",
        "(Current hashrate in exa-hashes, 7 Day AVG.)",
        unsafe_allow_html=True,
    )

    # * USAGE: settingsBar.slider_hashrate_label()

def slider_hashrate_btc():
    #### BTC HASHRATE SLIDER  #####################################################
    format_slider_exaHashes = "%d"
    label_exaHashes_BTC = ":orange[BTC Network] *(Default: 402.2)*"
    slider_exaHashes_BTC = st.sidebar.slider(
        label_exaHashes_BTC, 1.0, 1000.0, 402.2, 0.1, format_slider_exaHashes
    )

    return slider_exaHashes_BTC
    # * USAGE: slider_exaHashes_BTC = settingsBar.slider_hashrate_btc()

def slider_hashrate_bch():
    #### BCH HASHRATE SLIDER  #####################################################
    format_slider_exaHashes = "%d"
    label_exaHashes_BCH = ":green[BCH Network] *(Default: 2.67)*"
    slider_exaHashes_BCH = st.sidebar.slider(
        label_exaHashes_BCH, 1.0, 1000.0, 2.67, 0.1, format_slider_exaHashes
    )

    return slider_exaHashes_BCH
    # * USAGE: slider_exaHashes_BCH = settingsBar.slider_hashrate_bch()



def slider_energyUsageYearlyTwH_label():
    st.sidebar.write(
        '<font size="+5">Energy Usage in TwH',
        "</font>",
        "</br>",
        "(Yearly energy usage of entire network in Terrawatt Hours, found here, https://ccaf.io/cbnsi/cbeci )",
        unsafe_allow_html=True,
    )

    # * USAGE: settingsBar.slider_energyUsageYearlyTwH_label()

def slider_energyUsageYearlyTwH_btc():
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

    return slider_energyUsageYearlyTwH_BTC
    # * USAGE: slider_energyUsageYearlyTwH_BTC = settingsBar.slider_energyUsageYearlyTwH_btc()

def slider_energyUsageYearlyTwH_bch(slider_energyUsageYearlyTwH_BTC, slider_exaHashes_BTC,slider_exaHashes_BCH):
    #### BCH ENERGY USAGE SLIDER  #################################################
    # ! No slider for BCH as its energy usage is derived from BTC energy usage per exahash.

    # Convert BTC Yearly TwH to KwH, this is because most other calculations are done based on the cost of each KwH.
    energyUsageYearlyKwH_BTC = slider_energyUsageYearlyTwH_BTC * 1000000000

    # Get an energy usage ratio by getting the BTC hashrate and its yearly KwH
    exaHashToYearlyKwHRatio = energyUsageYearlyKwH_BTC / slider_exaHashes_BTC

    # Multiply the BCH exahashes by the energy usage ratio, this assumes equivalent efficiency between the chains equipment. This is a fair comparison.
    energyUsageYearlyKwH_BCH = slider_exaHashes_BCH * exaHashToYearlyKwHRatio

    # Get BCH yearly TwH used
    energyUsageYearlyTwH_BCH = energyUsageYearlyKwH_BCH / 1000000000
    st.sidebar.write(energyUsageYearlyTwH_BCH,
        "The energy usage of the BCH network is proportional based on its hashrate in comparison to BTC's energy usage and hashrate."
    )
    return energyUsageYearlyTwH_BCH
    # * USAGE: energyUsageYearlyTwH_BCH = settingsBar.slider_energyUsageYearlyTwH_bch(slider_energyUsageYearlyTwH_BTC,slider_exaHashes_BTC,slider_exaHashes_BCH)
    # * Must be called after BTC sliders have been called correctly.



def slider_price_label():
    st.sidebar.write(
        '<font size="+5">Prices in USD',
        "</font>",
        "</br>",
        "(Not yet updated dynamically )",
        unsafe_allow_html=True,
    )
    # * USAGE: settingsBar.slider_price_label()

def slider_price_btc():
    #### BTC PRICING SLIDER  ######################################################
    format_slider_Price = "%d"
    label_priceBTC = ":orange[BTC Network] *(Default: 26091.70)*"

    slider_PriceBTC = st.sidebar.slider(
        label_priceBTC, 1.0, 100000.0, 26091.70, 0.1, format_slider_Price
    )
    return slider_PriceBTC
    # * USAGE: slider_PriceBTC = settingsBar.slider_price_btc()

def slider_price_bch():
    #### BCH PRICING SLIDER  ######################################################
    format_slider_Price = "%d"
    label_priceBCH = ":green[BCH Network] *(Default: 190.02)*"

    slider_PriceBCH = st.sidebar.slider(
        label_priceBCH, 1.0, 100000.0, 190.02, 0.1, format_slider_Price
    )
    return slider_PriceBCH
    # * USAGE: slider_PriceBCH = settingsBar.slider_price_bch()


def select_blockreward_label():
    st.sidebar.write(
        '<font size="+5">Block Reward',
        "</font>",
        "</br>",
        "(Amount of Bitcoins awarded as prize for mining.)",
        unsafe_allow_html=True,
    )
    # * USAGE: settingsBar.select_blockreward_label()

def select_blockreward():
    #### BLOCK REWARD SELECTOR (BOTH)  ############################################

    blockReward = st.sidebar.selectbox(
        "Choose block reward *(Default: 6.25)*",
        (50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.195325, 0.09765625, 0),
        3,
    )
    # (6 blocks per hour * 24 hours) * (block reward)
    totalDailyBlockRewards = (6 * 24) * blockReward
    ###############################################################################
    return totalDailyBlockRewards
    # * USAGE: totalDailyBlockRewards = settingsBar.select_blockreward()


def chart_settings_label():
    ###############################################################################
    st.sidebar.write(
        '<font size="+5">Chart Settings',
        "</font>",
        "</br>",
        "(Settings that control the scale of the chart. Helpful for zooming in.)",
        unsafe_allow_html=True,
    )
    ###############################################################################
    # * USAGE: settingsBar.chart_settings_label()

def input_chart_settings_electricity():
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
    return start_value, end_value, step
    # * USAGE: start_value, end_value, step = settingsBar.input_chart_settings_electricity()