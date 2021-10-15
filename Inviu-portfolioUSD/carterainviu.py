#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 02:51:33 2021

@author: leoprimero
"""

import pandas as pd

import matplotlib.pyplot as plt
import pyfolio

path = 'PATH'
GGAL = pd.read_csv(path + 'GGAL.csv')
KO = pd.read_csv(path + 'KO.csv')
LOMA = pd.read_csv(path + 'LOMA.csv')
TX22 = pd.read_csv(path + 'TX22.csv')
TX24 = pd.read_csv(path + 'TX24.csv')
WMT = pd.read_csv(path + 'WMT.csv')

GGAL.set_index('Date',inplace=True)
KO.set_index('Date',inplace=True)
LOMA.set_index('Date',inplace=True)
TX22.set_index('Date',inplace=True)
TX24.set_index('Date',inplace=True)
WMT.set_index('Date',inplace=True)



tickers = (GGAL,KO,LOMA,TX22,TX24,WMT)



reco= [0.1,0.15,0.1,0.25,0.15,0.15]

equi_weighs= [1/(len(tickers))for n in tickers]

for stock in (tickers):
    stock["Returns"]=stock["Close"]/stock["Close"].iloc[0]
    
for stock, allocation in zip((tickers), reco):
                            
    stock["Allocation"]= stock["Returns"]* allocation
    
for stock in (tickers):
    stock["Position"]= stock["Allocation"]*500_000

    
portafolio = pd.concat([x  ['Position'] for x in tickers],axis=1)

portafolio.columns = ['GGAL','KO','LOMA','TX22','TX24','WMT']


portafolio_total = portafolio.sum(axis=1)
 
plt.style.use('dark_background')
portafolio_total.plot(figsize=(9,7.5))
plt.grid(alpha=0.3, color='SteelBlue', linewidth=1)
plt.title ("Portafolio Inviu",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('Precio en ARS')

portafolio_returns = portafolio_total.pct_change().dropna()
portafolio_returns.plot (figsize=(9,7.5))
plt.title ("Retornos diarios Portafolio Inviu",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('Precio')

portafolio.plot(figsize=(12,9))
plt.title ("Evolución de activos individuales",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('Precio')

retornos= portafolio.pct_change().dropna()
retornos.plot(figsize=(19,17))
plt.title ("Rendimiento diario por activos",fontsize = 30)
plt.xlabel('Fecha')
plt.ylabel('Precio')

retornosacumulado= (retornos/100+1).cumprod()
retornosacumulado.plot(figsize=(15,13))
plt.title ("Rendimientos diarios acumulados por activos",fontsize = 30)
plt.xlabel('Fecha')
plt.ylabel('Precio')

# MERVAL['close'].plot(figsize=(9,7.5))
# plt.title ("Indice MERVAL",fontsize = 20)
# plt.xlabel('Fecha')
# plt.ylabel('Precio')

benchmark = BYMA["Adj Close"]
bench = benchmark.pct_change().dropna()
bench.rename("Benchmark SP500")
pyfolio.create_returns_tear_sheet(portafolio_returns)

# portafolio_total.columns = ['Date','Close']
# portafolio_totalcv = portafolio_total.to_excel("portafolio_total_pam.xlsx")


# retornoacum= (retornosacumulado).cumprod()
# retornosaexcel= retornos.to_excel('retornos.xlsx')
# retornoacumuladoexcel= (retornoacum-1).to_excel('retorno_acumulado_por_activo.xlsx')




