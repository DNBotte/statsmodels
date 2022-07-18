# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(lambda)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

# -*- coding: utf-8 -*-
"""
^Info above from PowerBI
"""

import statsmodels.api as sm
import pandas as pd
dta = sm.datasets.macrodata.load_pandas().data
index = pd.period_range('1959Q1', '2009Q3', freq = 'Q')
dta.set_index(index, inplace=True)

cycle, trend = sm.tsa.filters.hpfilter(dta.realgdp, 1600)
gdp_decomp = dta[['realgdp']]
gdp_decomp["cycle"] = cycle
gdp_decomp["trend"] = trend

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
gdp_decomp[["realgdp", "trend"]]["2000-03-31":].plot(ax=ax, fontsize = 16)

plt.show()
