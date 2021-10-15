#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 05:40:35 2021

@author: leoprimero
"""

import yfinance as yf, numpy as np, pandas as pd, matplotlib.pyplot as plt, markowitz as mk



df = yf.download(['AMZN','JNJ','PFE','WMT','PG','PKX','SQ','DE','BG','FCX'],
                 start='2021-07-01', end='2021-08-20')['Adj Close']
df = df.loc[~(df==0).any(axis=1)] 


pond1, real, = mk.markowitzrealMono ( df, q=1)
pond, optimo, = mk.markowitzoptimoMONO ( df, q=10000)

print(pond, '\n\nPortafolio Optimo:\n',optimo, sep='')
print(pond1, '\n\nPortafolio Real:\n',real, sep='')


pondtoExcel = pond,optimo.to_excel('Optimo.xlsx')
pond1toExcel = pond1,real.to_excel('Real.xlsx')