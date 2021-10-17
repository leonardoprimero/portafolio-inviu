#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 05:40:35 2021

@author: leoprimero
"""


import yfinance as yf, numpy as np, pandas as pd, matplotlib.pyplot as plt, markowitz as mk

path = '/home/leoprimero/Documentos/portafolio-inviu-main/Inviu-portfolioUSD/Data/'
GGAL = pd.read_csv(path + 'GGAL.csv')
KO = pd.read_csv(path + 'KO.csv')
LOMA = pd.read_csv(path + 'LOMA.csv')
TX22 = pd.read_csv(path + 'TX22.csv')
TX24 = pd.read_csv(path + 'TX24.csv')
WMT = pd.read_csv(path + 'WMT.csv')
VSC30 = pd.read_csv(path + 'VSC30.csv')

GGAL.set_index('Date',inplace=True)
KO.set_index('Date',inplace=True)
LOMA.set_index('Date',inplace=True)
TX22.set_index('Date',inplace=True)
TX24.set_index('Date',inplace=True)
WMT.set_index('Date',inplace=True)
VSC30.set_index('Date',inplace=True)


tickers = (GGAL,KO,LOMA,TX22,TX24,WMT,VSC30)


    
df1 = pd.concat([x  ['Close'] for x in tickers],axis=1)

df1.columns = ['GGAL','KO','LOMA','TX22','TX24','WMT','VSC30']

df1 = df1.loc[~(df1==0).any(axis=1)]
pond, optimo, = mk.markowitz ( df1, q=100000)



pondtoExcel = pond,optimo.to_excel('Optimo.xlsx')
