import streamlit as st
import pandas as pd
import numpy as np
import settingsBar
import comparisonTable

st.set_page_config(page_title="The Playground - The Past, The Present & The Future of Bitcoin.", page_icon="🚸",layout="wide")
# st.write(st.session_state["shared"])

# ! SETTINGS SIDEBAR #########################################################
with st.sidebar.expander("#### TPS Settings"):
    settingsBar.slider_tps_label()
    slider_BTC_TPS, max_daily_transactions_BTC = settingsBar.slider_tps_btc()
    slider_BCH_TPS, max_daily_transactions_BCH = settingsBar.slider_tps_bch()

with st.sidebar.expander("#### Hashrate Settings"):
    settingsBar.slider_hashrate_label()
    slider_exaHashes_BTC = settingsBar.slider_hashrate_btc()
    slider_exaHashes_BCH = settingsBar.slider_hashrate_bch()

with st.sidebar.expander("#### Energy Usage Settings"):
    settingsBar.slider_energyUsageYearlyTwH_label()
    energyUsageYearlyKwH_BTC, slider_energyUsageYearlyTwH_BTC = settingsBar.slider_energyUsageYearlyTwH_btc()
    energyUsageYearlyKwH_BCH, energyUsageYearlyTwH_BCH = settingsBar.slider_energyUsageYearlyTwH_bch(slider_energyUsageYearlyTwH_BTC,slider_exaHashes_BTC,slider_exaHashes_BCH)

with st.sidebar.expander("#### Price Settings"):
    settingsBar.slider_price_label()
    slider_PriceBTC = settingsBar.slider_price_btc(69.0, 69696969.0, 420.0, 10.0)
    slider_PriceBCH = settingsBar.slider_price_bch()


with st.sidebar.expander("#### Block Reward Settings"):
    settingsBar.select_blockreward_label()
    blockReward, totalDailyBlockRewards = settingsBar.select_blockreward(index=4)

with st.sidebar.expander("#### Chart Settings"):
    settingsBar.chart_settings_label()
    start_value, end_value, step = settingsBar.input_chart_settings_electricity()

# ! SETTINGS SIDEBAR #########################################################


comparisonTable.fullTable(slider_BTC_TPS,
                          max_daily_transactions_BTC,
                          slider_BCH_TPS,
                          max_daily_transactions_BCH,
                          slider_exaHashes_BTC,
                          slider_exaHashes_BCH,
                          energyUsageYearlyKwH_BTC,
                          slider_energyUsageYearlyTwH_BTC,
                          energyUsageYearlyKwH_BCH,
                          energyUsageYearlyTwH_BCH,
                          slider_PriceBTC,
                          slider_PriceBCH,
                          blockReward,
                          totalDailyBlockRewards)
