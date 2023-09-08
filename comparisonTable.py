import streamlit as st
import pandas as pd
import numpy as np
import settingsBar


def fullTable(slider_BTC_TPS, max_daily_transactions_BTC, slider_BCH_TPS, max_daily_transactions_BCH, slider_exaHashes_BTC, slider_exaHashes_BCH, energyUsageYearlyKwH_BTC, slider_energyUsageYearlyTwH_BTC, energyUsageYearlyKwH_BCH, energyUsageYearlyTwH_BCH, slider_PriceBTC, slider_PriceBCH, blockReward, totalDailyBlockRewards):
    col_font_statistic = '<center> <font size="+8">'
    end_col_font_statistic = "</font> </center> </br>"

    col_font_label = '<center> <font size="+4">'
    end_col_font_label = "</font> </center>"

    col1, col2, col3 = st.columns(3)


    col1, col2 = st.columns(2)
    with col1:
        st.header(":orange[Bitcoin]")
        st.header(":orange[BTC]", divider="orange")
        st.divider()
        st.write(
        col_font_statistic,
        str(round(slider_BTC_TPS)),
        end_col_font_statistic,
        col_font_label,
        "Max. TPS </br> (Transactions per Second)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(max_daily_transactions_BTC)),
        end_col_font_statistic,
        col_font_label,
        "Max. Daily Transactions </br> (Full Blocks)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        str(round(slider_exaHashes_BTC, 2)),
        end_col_font_statistic,
        col_font_label,
        "Hashrate </br> (in Exahashes/s)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(slider_energyUsageYearlyTwH_BTC, 2)),
        end_col_font_statistic,
        col_font_label,
        "Energy Usage </br> (TwH/Yearly)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        "$",
        str(round(slider_PriceBTC)),
        end_col_font_statistic,
        col_font_label,
        "Price </br> (in USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        str(round(blockReward)),
        end_col_font_statistic,
        col_font_label,
        "Block Reward </br> (in Bitcoins, BTC)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(totalDailyBlockRewards)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (in Bitcoins, BTC)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        "$",
        str(round(totalDailyBlockRewards * slider_PriceBTC)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (if sold to USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )

        st.write(
        col_font_statistic,
        str(round(((energyUsageYearlyKwH_BTC / 365) / max_daily_transactions_BTC), 2)),
        end_col_font_statistic,
        col_font_label,
        "KwH Per Transaction",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    #   st.write(col_font_statistic, str(energyUsageYearlyKwH_BTC/365),end_font,'KwH Per Day', end_col_font_label, unsafe_allow_html=True)

        """ BTC Info here"""


    with col2:
        st.header(":green[Bitcoin Cash]")
        st.header(":green[BCH]", divider="green")

        st.divider()
        st.write(
        col_font_statistic,
        str(round(slider_BCH_TPS)),
        end_col_font_statistic,
        col_font_label,
        "Max. TPS </br> (Transactions per Second)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(max_daily_transactions_BCH)),
        end_col_font_statistic,
        col_font_label,
        "Max. Daily Transactions </br> (Full Blocks)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        str(round(slider_exaHashes_BCH, 2)),
        end_col_font_statistic,
        col_font_label,
        "Hashrate </br> (in Exahashes/s)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(energyUsageYearlyTwH_BCH, 2)),
        end_col_font_statistic,
        col_font_label,
        "Energy Usage </br> (TwH/Yearly)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        "$",
        str(round(slider_PriceBCH)),
        end_col_font_statistic,
        col_font_label,
        "Price </br> (in USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        str(round(blockReward)),
        end_col_font_statistic,
        col_font_label,
        "Block Reward </br> (in Bitcoins, BCH)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.write(
        col_font_statistic,
        str(round(totalDailyBlockRewards)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (in Bitcoins, BCH)",
        end_col_font_label,
        unsafe_allow_html=True,
    )
        st.divider()
        st.write(
        col_font_statistic,
        "$",
        str(round(totalDailyBlockRewards * slider_PriceBCH)),
        end_col_font_statistic,
        col_font_label,
        "Total Daily Block Reward </br> (if sold to USD)",
        end_col_font_label,
        unsafe_allow_html=True,
    )

        st.write(
        col_font_statistic,
        str(round(((energyUsageYearlyKwH_BCH / 365) / max_daily_transactions_BCH), 2)),
        end_col_font_statistic,
        col_font_label,
        "KwH Per Transaction",
        end_col_font_label,
        unsafe_allow_html=True,
    )

    #    st.write(col_font_statistic, str(energyUsageYearlyKwH_BCH / 365),'</font>','KwH Per Day', end_col_font_label, unsafe_allow_html=True)

        """BCH Info Here"""

    # * USAGE:
    # comparisonTable.fullTable(slider_BTC_TPS,
    #                       max_daily_transactions_BTC,
    #                       slider_BCH_TPS,
    #                       max_daily_transactions_BCH,
    #                       slider_exaHashes_BTC,
    #                       slider_exaHashes_BCH,
    #                       energyUsageYearlyKwH_BTC,
    #                       slider_energyUsageYearlyTwH_BTC,
    #                       energyUsageYearlyKwH_BCH,
    #                       energyUsageYearlyTwH_BCH,
    #                       slider_PriceBTC,
    #                       slider_PriceBCH,
    #                       blockReward,
    #                       totalDailyBlockRewards)