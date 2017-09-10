"""
Created on Sun Aug 27 12:13:25 2017

@author: Naqib
"""
import logging
import pandas as pd
from  bitrexUtils import Bittrex

# creates a Bittrex Object that allows us to pull data from the bitrex api
BITFEE = .0025

bitDB = Bittrex( '', '' )
def getCurrencyDf():
    ''' returns a dataframe of active crypto currency objects indexed by currency'''
    df      = None
    ccyData = bitDB.get_currencies()
    if ccyData['success'] == True:
        df = pd.DataFrame( ccyData['result'] )
        df = df[df.IsActive == True]
        df = df.set_index(['Currency'])
    else:
        logging.info("Bittrex.get_currencies() function was not succesful")
    return df
    
def getCurrencyList():
    '''returns a list of active currencies'''
    return list ( getCurrencyDf().index.values )

def getTxFee( ccy ):
    df = getCurrencyDf()
    return df.TxFee[ccy]

def getMarketDf():
    '''returns a dataframe of acive crypto markets'''
    df         = None
    marketData = bitDB.get_markets()
    if marketData['success'] == True :
        df = pd.DataFrame( marketData['result'] )
        df = df[df.IsActive == True]
        df = df.set_index( ['MarketName'] )
    else:
        logging.info("Bittrex.getMarketDf() function was not succesful")
    return df

def getMarketList():
    '''returns a list of active markets'''
    ret = list ( getMarketDf().index.values )
    return ret

def flip(market):
    '''flips market, ie BTC-LTC to LTC-BTC 
    '''
    markets = market.split('-')
    flipped = markets[1]+'-' +markets[0]
    return flipped
    
def getTradePrice( baseCcy, marketCcy ):
    '''gets the last sold tick based off too markets
       example params BTC and LTC
       returns the current spot price in baseCCY to purchase 1 market ccy
       '''
    price    = None
    market   = baseCcy + '-' + marketCcy
    tickData = bitDB.get_ticker(market) 
    if tickData['success'] == True :
        price = tickData['result']['Last']
    else:
        tickData = bitDB.get_ticker( flip ( market ) ) 
        if tickData['success'] == True :
            price = 1 / tickData['result']['Last']
        else:
            logging.info("Bittrex.get_ticker() function was not succesful")
    return price
    
def getUsdPrice(ccy):
    '''gets the value in usd'''
    return getTradePrice('USDT', ccy)
    
def init_holdings():
    ''' ''' 
    df              = pd.DataFrame( index = getCurrencyList() )
    df.index.name   = 'CCY'
    df['Quantity']  = 0.0
    df.Quantity['BTC']    = 1.0
    return df
    


