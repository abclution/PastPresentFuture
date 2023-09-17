import json

# https://www.statista.com/statistics/730806/daily-number-of-bitcoin-transactions/
# https://data.nasdaq.com/data/BCHAIN/NTRAT-bitcoin-total-number-of-transactions
# https://www.blockchain.com/explorer/charts/n-transactions-total
# 2023 = [24694403121.0, 22550266965.0, 25247902988.0, 24728021996.0, 25986239228.0, 25568584100.0, 26822646365.0, 27270626035.0, 6220729231.0, 0, 0, 0]
# 2022 = [21795562447.0, 19895392857.0, 22256232050.0, 21775590372.0, 22749618877.0, 22248806869.0, 23224984568.0, 23466874818.0, 22940711871.0, 23947847726.0, 23415246705.0, 24440601546.0]
# 2021 = [18803337223.0, 17250301418.0, 19379862098.0, 19022944967.0, 19912641616.0, 19480859891.0, 20331179955.0, 20553011448.0, 20118008114.0, 21036184590.0, 20609954237.0, 21552755265.0]
# 2020 = [15302257492.0, 14592938150.0, 15892518502.0, 15632437505.0, 16437244468.0, 16177092588.0, 17015217542.0, 17325103375.0, 17055843817.0, 17919087003.0, 17612569592.0, 18493555327.0]
# 2019 = [11585113450.0, 10721024144.0, 12156784720.0, 12076031422.0, 12827596706.0, 12739354904.0, 13495043161.0, 13808462308.0, 13662541200.0, 14424401615.0, 14245463784.0, 15010068144.0]
# 2018 = [9075275423.0, 8385985048.0, 9455045448.0, 9315573191.0, 9816465113.0, 9677436458.0, 10184310458.0, 10390366575.0, 10258135317.0, 10823872074.0, 10713183451.0, 11317279787.0]
# 2017 = [5835767770.0, 5505997040.0, 6366436784.0, 6412689644.0, 6913947724.0, 6968236513.0, 7432918384.0, 7661001131.0, 7644975591.0, 8148309715.0, 8155115025.0, 8759743320.0]
# 2016 = [3222667815.0, 3197059649.0, 3614175762.0, 3679821049.0, 4010506108.0, 4085450658.0, 4427875464.0, 4639959698.0, 4692856221.0, 5068934668.0, 5134596926.0, 5568056206.0]
# 2015 = [1766144424.0, 16725105>31.0, 1941193584.0, 1972247828.0, 2136677785.0, 2169289588.0, 2367488288.0, 2484756040.0, 2518932249.0, 2731937642.0, 2781665674.0, 3042131411.0]
# 2014 = [965503993.0, 923351121.0, 1084813907.0, 1109037042.0, 1206161349.0, 1224638367.0, 1323372631.0, 1386187769.0, 1405187903.0, 1521706168.0, 1547231598.0, 1680877576.0]
# 2013 = [349948463.0, 358912895.0, 449733638.0, 486638361.0, 555683473.0, 585521113.0, 643900214.0, 689099999.0, 717395620.0, 791424295.0, 816809857.0, 909918169.0]
# 2012 = [68890325.0, 70463244.0, 81634248.0, 85347359.0, 100803910.0, 124468523.0, 156162918.0, 188142848.0, 213885581.0, 249615115.0, 268612562.0, 309792528.0]
# 2011 = [7287593.0, 7680102.0, 10590404.0, 12509025.0, 16118049.0, 22638242.0, 32707451.0, 40432716.0, 45586683.0, 52675932.0, 56030104.0, 63247569.0]
# 2010 = [1093663.0, 1143178.0, 1432369.0, 1606207.0, 1907464.0, 2043786.0, 2595095.0, 3237468.0, 3476239.0, 4039134.0, 4907794.0, 6492037.0]
# 2009 = [29068.0, 123819.0, 241866.0, 338216.0, 458489.0, 524159.0, 611848.0, 662271.0, 695197.0, 786238.0, 824272.0, 945146.0]
# https://data.nasdaq.com/data/BCHAIN/CPTRA-bitcoin-cost-per-transaction
# https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0810
# https://ec.europa.eu/eurostat/cache/infographs/energy_prices/enprices.html?geos=EU27_2020,EA,BE,BG,CZ,DK,DE,EE,IE,EL,ES,FR,HR,IT,CY,LV,LT,LU,HU,MT,NL,AT,PL,PT,RO,SI,SK,FI,SE,IS,LI,NO,ME,MK,AL,RS,TR,BA,XK,MD,UA,GE&product=6000&consumer=HOUSEHOLD&consoms=KWH_LT1000&unit=KWH&taxs=I_TAX,X_TAX,X_VAT&nrg_prc=NETC,NRG_SUP,OTH,TAX_CAP,TAX_ENV,TAX_NUC,TAX_RNW,VAT&currency=EUR&language=EN&detail=0&component=0&order=DESC&dataset=nrg_pc_204&time=2022-S2&modalOption=0&chartOption=0&precision=1&modalOpen=0&modal=0&modalLineOption=0#2022-S2

#https://www.sofi.com/learn/content/bitcoin-price-history/
# Bitcoin Price History by Year (2014-2022)
# Year	High	Low
# 2014	$457.09	$289.30
# 2015	$495.56	$171.51
# 2016	$979.40	$354.91
# 2017	$20,089.00	$755.76
# 2018	$17,712.40	$3,191.30
# 2019	$13,796.49	$3,391.02
# 2020	$29,244.88	$4,106.98
# 2021	$68,789.63	$28,722.76
# 2022	$48,086.84	$15,599.05
# 2023	$16,674	$24,895

# Hash: 1000000000000000000
# KiloHash: 1000000000000000
# MegaHash: 1000000000000
# GigaHash: 1000000000
# TeraHash: 1000000
# PetaHash: 1000
# ExaHash: 1
# ZettaHash: 0.001

Hash = 1000000000000000000
KiloHash = 1000000000000000
MegaHash = 1000000000000
GigaHash = 1000000000
TeraHash = 1000000
PetaHash = 1000
ExaHash = 1
ZettaHash = 0.001


# https://www.zenledger.io/blog/bitcoin-halving/
# https://bitinfocharts.com/comparison/bitcoin-hashrate.html#alltime
BTC_2009 = {
    "Year": 2009,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 0.0,
    "Price High": 0.0,
    "Hashrate Low": 462.433 / KiloHash,
    "Hashrate High": 12.5763 / MegaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [29068.0, 123819.0, 241866.0, 338216.0, 458489.0, 524159.0, 611848.0, 662271.0, 695197.0, 786238.0, 824272.0, 945146.0]
    }
# https://www.statmuse.com/money/ask/bitcoin+price+2010#:~:text=The%20closing%20price%20for%20Bitcoin,The%20latest%20price%20is%20%2429%2C410.05.
BTC_2010 = {
    "Year": 2010,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 0.0,
    "Price High": 0.39,
    "Hashrate Low": 7.6074 / MegaHash,
    "Hashrate High": 128.626 / GigaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [1093663.0, 1143178.0, 1432369.0, 1606207.0, 1907464.0, 2043786.0, 2595095.0, 3237468.0, 3476239.0, 4039134.0, 4907794.0, 6492037.0]
    }

BTC_2011 = {
    "Year": 2011,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": .30,
    "Price High": 35.0,
    "Hashrate Low": 118.021 / GigaHash,
    "Hashrate High": 15.842 / TeraHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [7287593.0, 7680102.0, 10590404.0, 12509025.0, 16118049.0, 22638242.0, 32707451.0, 40432716.0, 45586683.0, 52675932.0, 56030104.0, 63247569.0]
    }


BTC_2012 = {
    "Year": 2012,
    "Halving Year": True,
    "Halving Date": "2012/11/28",
    "Price Low": 5.50,
    "Price High": 15.37,
    "Hashrate Low": 8.68328 / TeraHash,
    "Hashrate High": 29.1452 / TeraHash,
    "Price Halving Day": 1,
    "Price 150 Days after Halving ": 1,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [68890325.0, 70463244.0, 81634248.0, 85347359.0, 100803910.0, 124468523.0, 156162918.0, 188142848.0, 213885581.0, 249615115.0, 268612562.0, 309792528.0]
    }

#https://www.sofi.com/learn/content/bitcoin-price-history/
BTC_2013 = {
    "Year": 2013,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 13.57,
    "Price High": 1151,
    "Hashrate Low": 18.906 / TeraHash,
    "Hashrate High": 10.619 / PetaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [349948463.0, 358912895.0, 449733638.0, 486638361.0, 555683473.0, 585521113.0, 643900214.0, 689099999.0, 717395620.0, 791424295.0, 816809857.0, 909918169.0]
    }
BTC_2014 = {
    "Year": 2014,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 	289.30,
    "Price High": 934.21,
    "Hashrate Low": 11.345 / PetaHash,
    "Hashrate High": 331.8237 / PetaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [965503993.0, 923351121.0, 1084813907.0, 1109037042.0, 1206161349.0, 1224638367.0, 1323372631.0, 1386187769.0, 1405187903.0, 1521706168.0, 1547231598.0, 1680877576.0]
    }

BTC_2015 = {
    "Year": 2015,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 171.51,
    "Price High": 495.56,	
    "Hashrate Low": 267.3181 / PetaHash,
    "Hashrate High": 891.437 / PetaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [1766144424.0, 1672510531.0, 1941193584.0, 1972247828.0, 2136677785.0, 2169289588.0, 2367488288.0, 2484756040.0, 2518932249.0, 2731937642.0, 2781665674.0, 3042131411.0]
    }


BTC_2016 = {
    "Year": 2016,
    "Halving Year": True,
    "Halving Date": "2016/07/09",
    "Price Low": 354.91,
    "Price High": 979.40,
    "Hashrate Low": 704.5287 / PetaHash,
    "Hashrate High": 901.8396 / PetaHash,
    "Price Halving Day": 1,
    "Price 150 Days after Halving ": 1,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [3222667815.0, 3197059649.0, 3614175762.0, 3679821049.0, 4010506108.0, 4085450658.0, 4427875464.0, 4639959698.0, 4692856221.0, 5068934668.0, 5134596926.0, 5568056206.0]
    }

BTC_2017 = {
    "Year": 2017,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 755.761,
    "Price High": 20089.00,
    "Hashrate Low": 2.24 / ExaHash,
    "Hashrate High": 15.3171 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month":  [5835767770.0, 5505997040.0, 6366436784.0, 6412689644.0, 6913947724.0, 6968236513.0, 7432918384.0, 7661001131.0, 7644975591.0, 8148309715.0, 8155115025.0, 8759743320.0]
    }

BTC_2018 = {
    "Year": 2018,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 3191.30,
    "Price High": 17712.40,
    "Hashrate Low": 14.8914 / ExaHash,
    "Hashrate High": 60.4225 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [9075275423.0, 8385985048.0, 9455045448.0, 9315573191.0, 9816465113.0, 9677436458.0, 10184310458.0, 10390366575.0, 10258135317.0, 10823872074.0, 10713183451.0, 11317279787.0]
    }

BTC_2019 = {
    "Year": 2019,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 3391.02,
    "Price High": 13796.49,
    "Hashrate Low": 36.9481 / ExaHash,
    "Hashrate High": 111.8487 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [11585113450.0, 10721024144.0, 12156784720.0, 12076031422.0, 12827596706.0, 12739354904.0, 13495043161.0, 13808462308.0, 13662541200.0, 14424401615.0, 14245463784.0, 15010068144.0]
    }


BTC_2020 = {
    "Year": 2020,
    "Halving Year": True,
    "Halving Date": "2020/05/11",
    "Price Low": 4106.98,
    "Price High": 29244.88,
    "Hashrate Low": 84.0881 / ExaHash,
    "Hashrate High": 161.1588 / ExaHash,
    "Price Halving Day": 1,
    "Price 150 Days after Halving ": 1,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [15302257492.0, 14592938150.0, 15892518502.0, 15632437505.0, 16437244468.0, 16177092588.0, 17015217542.0, 17325103375.0, 17055843817.0, 17919087003.0, 17612569592.0, 18493555327.0]
    }

BTC_2021 = {
    "Year": 2021,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 28722.76,
    "Price High": 68789.63,
    "Hashrate Low": 68.0088 / ExaHash,
    "Hashrate High": 197.6095 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [18803337223.0, 17250301418.0, 19379862098.0, 19022944967.0, 19912641616.0, 19480859891.0, 20331179955.0, 20553011448.0, 20118008114.0, 21036184590.0, 20609954237.0, 21552755265.0]
    }

BTC_2022 = {
    "Year": 2022,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 15599.05,
    "Price High": 48086.84,
    "Hashrate Low": 159.6955 / ExaHash,
    "Hashrate High": 298.931 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [21795562447.0, 19895392857.0, 22256232050.0, 21775590372.0, 22749618877.0, 22248806869.0, 23224984568.0, 23466874818.0, 22940711871.0, 23947847726.0, 23415246705.0, 24440601546.0]
    }

# todo get correct price
BTC_2023 = {
    "Year": 2023,
    "Halving Year": False,
    "Halving Date": False,
    "Price Low": 16674,
    "Price High": 29903,
    "Hashrate Low": 241.3487 / ExaHash,
    "Hashrate High": 465.0148 / ExaHash,
    "Price Halving Day": False,
    "Price 150 Days after Halving ": False,
    "Electricity Cost Low": .002,
    "Electricity Cost High":.002,
    "Total Transactions Per Month": [24694403121.0, 22550266965.0, 25247902988.0, 24728021996.0, 25986239228.0, 25568584100.0, 26822646365.0, 27270626035.0, 6220729231.0, 0, 0, 0]
    }



def nasdaqDataExtract(json_file_path):
    '''Returns a dictionary of yearly sums of the NASDAQ data'''
    # Load JSON data from the file
    with open(json_file_path, 'r') as json_file:
        loadedJsonData = json.load(json_file)["dataset"]["data"]

    yearly_sums = {}

    # Iterate through the data and calculate yearly sums
    for entry in loadedJsonData:
        date = entry[0]
        value = entry[1]
        year, month, day = date.split("-")

        if year in yearly_sums:
            yearly_sums[year][int(month) - 1] += value
        else:
            yearly_sums[year] = [0] * 12  #  initialize a list of 12 zeros within the yearly_sums dictionary for a specific year. 
            yearly_sums[year][int(month) - 1] = value  #  lists in Python are zero-indexed, so January is represented as 0, February as 1,

    # Print the yearly sums
    # for year, monthly_values in yearly_sums.items():
        # print(f"{year} = {monthly_values}")
    return yearly_sums

