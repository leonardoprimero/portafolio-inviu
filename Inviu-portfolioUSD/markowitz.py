#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 05:44:22 2021

@author: leoprimero
"""
import  numpy as np, pandas as pd, matplotlib.pyplot as plt
import importlib




def markowitz(data, q=1000):
    retornos = np.log((data/data.shift(1)).dropna())
    carteras, datosTickers = [] , []
    
    for i in range(q):
        pond = np.array(np.random.random(len(data.columns)))
        pond = pond/np.sum(pond)
        r={}
        r['retorno'] = np.sum( (retornos.mean() * pond * 252))
        r['volatilidad'] = np.sqrt(np.dot(pond, np.dot(retornos.cov()*252, pond)))
        r['sharpe'] = r['retorno'] / r['volatilidad'] 
        r['pesos'] =  pond.round(5)
        carteras.append(r)
    
    for ticker in data.columns:
        d = {}
        d['ticker'] = ticker
        d['retorno'] = retornos[ticker].mean() * 252
        d['volatilidad'] = retornos[ticker].std() * (252**0.5)
        d['sharpe'] = d['retorno'] / d['volatilidad']
        datosTickers.append(d)

    datosTickers = pd.DataFrame(datosTickers).set_index('ticker')    
    carteras = pd.DataFrame(carteras)

    optimo = carteras.loc[carteras.sharpe.idxmax()]
    mejor_port = carteras.iloc[carteras.sharpe.idxmax()]['pesos']
    datosTickers['ponderacion_optima'] = mejor_port
    
    plt.figure(figsize=(9,7.5))
    plt.title("Propuesta Inviu",fontsize = 20)
    plt.grid()
    plt.scatter(carteras.volatilidad, carteras.retorno, c=carteras.sharpe, s=1, cmap='rainbow')
    plt.colorbar(label='Sharpe Ratio', aspect=40)
    plt.xlabel('Volatilidad')
    plt.ylabel('Retorno')
    plt.scatter(optimo.volatilidad, optimo.retorno,c='tab:red', alpha=0.2, s=1000) 
    plt.text(optimo.volatilidad, optimo.retorno, 'Optimo', fontsize=9, c='k', ha='center', va='center') 


       
    for ticker in data.columns:
        vol = datosTickers.loc[ticker,'volatilidad'] 
        ret = datosTickers.loc[ticker,'retorno'] 
        plt.scatter(vol, ret,  c='tab:blue', s=700) 
        plt.text(vol, ret, ticker, c='w', ha='center', va='center') 
    
    return (datosTickers.round(5), optimo)



def markowitzoptimoPandemia(data, q=10000,):
    Retornos = np.log((data/data.shift(1)).dropna())
    Retornos1 = np.log((data/data.shift(1)).dropna())
    carteras,  datosTickers = [] , []
    carteras1, datosTickers1 = [] , []
    
    for i in range(q):
        pond = np.array(np.random.random(len(data.columns)))
        pond = pond/np.sum(pond)
        r={}
        r['Retorno'] = np.sum( (Retornos.mean() * pond * 252))
        r['Volatilidad'] = np.sqrt(np.dot(pond, np.dot(Retornos.cov()*252, pond)))
        r['Sharpe'] = r['Retorno'] / r['Volatilidad'] 
        r['pesos'] =  pond.round(3)
        carteras.append(r)
         
        pond1 = np.array(exis) ####      WheighsSimon   WheighsSimonBest  WheighsViejosSimon
        r1={}
        r1['Retorno1'] = np.sum( (Retornos1.mean() * pond1 * 252))
        r1['Volatilidad1'] = np.sqrt(np.dot(pond1, np.dot(Retornos1.cov()*252, pond1)))
        r1['Sharpe1'] = r1['Retorno1'] / r1['Volatilidad1'] 
        r1['pesos1'] =  pond1.round(2)
        carteras1.append(r1)

      
        
    
    for Ticker in data.columns:
        d = {}
        d['Ticker'] = Ticker
        d['Retorno'] = Retornos[Ticker].mean() * 252
        d['Volatilidad'] = Retornos[Ticker].std() * (252**0.5)
        d['Sharpe'] = d['Retorno'] / d['Volatilidad']
        datosTickers.append(d)
        
    for Ticker1 in data.columns:
        d1 = {}
        d1['Ticker'] = Ticker
        d1['Retorno1'] = Retornos1[Ticker].mean() * 252
        d1['Volatilidad1'] = Retornos1[Ticker].std() * (252**0.5)
        d1['Sharpe1'] = d1['Retorno1'] / d1['Volatilidad1']
        datosTickers1.append(d1)

    datosTickers = pd.DataFrame(datosTickers).set_index('Ticker')
    datosTickers1 = pd.DataFrame(datosTickers1).set_index('Ticker')     
    carteras = pd.DataFrame(carteras)
    carteras1 = pd.DataFrame(carteras1)

    optimo = carteras.loc[carteras.Sharpe.idxmax()]
    real = carteras1.loc[carteras1.Sharpe1.idxmax()]
    mejor_port = carteras.iloc[carteras.Sharpe.idxmax()]['pesos']
    real_port = carteras1.iloc[carteras1.Sharpe1.idxmax()]['pesos1']
    datosTickers['Ponderacion_optima'] = mejor_port
    datosTickers1['Ponderacion_real'] = real_port

#####    OSCURA   #EF6C35  tab:green'

    plt.style.use('dark_background')
    plt.figure(figsize=(9,7.5))
    plt.title("Propuesta Markowits",fontsize = 20, color="#ffe536")
    plt.scatter(carteras.Volatilidad, carteras.Retorno, c=carteras.Sharpe, s=1, cmap='ocean')  # 
    plt.colorbar(label='Sharpe Ratio', aspect=40)
    plt.xlabel('Volatility', color="#ffe536")
    plt.ylabel('Annual Return USD', color="#ffe536")
    plt.grid()
    plt.scatter(optimo.Volatilidad, optimo.Retorno,c='tab:red', alpha=0.5, s=900)    
    plt.text(optimo.Volatilidad, optimo.Retorno, 'Eqis', fontsize=9, c='y', ha='center', va='center') 
    plt.scatter(real.Volatilidad1, real.Retorno1,c='tab:green', alpha=0.5, s=900)
    plt.text(real.Volatilidad1, real.Retorno1, 'Real', fontsize=9, c='y', ha='center', va='center')
    # plt.scatter(real.Volatilidad1, real.Retorno1,c='#EF6C35', alpha=0.5, s=900)
    # plt.text(real.Volatilidad1, real.Retorno1, 'Best', fontsize=9, c='y', ha='center', va='center')

######   CLARA

    # plt.figure(figsize=(9,7.5))
    # plt.title("Portafolio FinnAr ",fontsize = 20)
    # plt.scatter(carteras.Volatilidad, carteras.Retorno, c=carteras.Sharpe, s=1, cmap='rainbow')
    # plt.colorbar(label='Sharpe Ratio', aspect=40)
    # plt.xlabel('Volatilidad')
    # plt.ylabel('Retorno Anual')
    # plt.grid()
    # plt.scatter(optimo.Volatilidad, optimo.Retorno,c='tab:red', alpha=0.2, s=900)    
    # plt.text(optimo.Volatilidad, optimo.Retorno, 'Optimo', fontsize=9, c='k', ha='center', va='center') 
    # plt.scatter(real.Volatilidad1, real.Retorno1,c='tab:green', alpha=0.3, s=900)
    # plt.text(real.Volatilidad1, real.Retorno1, 'equis', fontsize=9, c='k', ha='center', va='center')

    
    for Ticker in data.columns:
        vol = datosTickers.loc[Ticker,'Volatilidad'] 
        ret = datosTickers.loc[Ticker,'Retorno'] 
        plt.scatter(vol, ret,  c='tab:blue', s=500) 
        plt.text(vol, ret, Ticker, c='w', ha='center', va='center') 
    
    return(datosTickers.round(3), optimo)
    return(datosTickers1.round(2), real)

