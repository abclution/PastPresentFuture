import streamlit as st
import pandas as pd
import numpy as np
import settingsBar

st.set_page_config(page_title="The Playground - The Past, The Present & The Future of Bitcoin.", page_icon="🚸",layout="wide")
# st.write(st.session_state["shared"])

settingsBar.slider_tps_label()
slider_BTC_TPS, max_daily_transactions_BTC = settingsBar.slider_tps_btc()
slider_BCH_TPS, max_daily_transactions_BCH = settingsBar.slider_tps_bch()
st.write(slider_BTC_TPS, max_daily_transactions_BTC)
st.write(slider_BCH_TPS, max_daily_transactions_BCH)


settingsBar.slider_hashrate_label()
slider_exaHashes_BTC = settingsBar.slider_hashrate_btc()
slider_exaHashes_BCH = settingsBar.slider_hashrate_bch()
st.write(slider_exaHashes_BTC, slider_exaHashes_BCH)

settingsBar.slider_energyUsageYearlyTwH_label()
slider_energyUsageYearlyTwH_BTC = settingsBar.slider_energyUsageYearlyTwH_btc()
energyUsageYearlyTwH_BCH = settingsBar.slider_energyUsageYearlyTwH_bch(slider_energyUsageYearlyTwH_BTC,slider_exaHashes_BTC,slider_exaHashes_BCH)
st.write(slider_energyUsageYearlyTwH_BTC, energyUsageYearlyTwH_BCH)


settingsBar.slider_price_label()
slider_PriceBTC = settingsBar.slider_price_btc()
slider_PriceBCH = settingsBar.slider_price_bch()
st.write(slider_PriceBTC, slider_PriceBCH)



settingsBar.select_blockreward_label()
totalDailyBlockRewards = settingsBar.select_blockreward()
st.write(totalDailyBlockRewards)


settingsBar.chart_settings_label()
start_value, end_value, step = settingsBar.input_chart_settings_electricity()
st.write(start_value, end_value, step)

