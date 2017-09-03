# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:13:25 2017

@author: Naqib
"""
import bookUtils  
import datetime

class Portfolio(object):
    '''Portfolio object to manage your currencies'''
    def __init__( self , name ):
        self.holdings = bookUtils.init_holdings()
        self.tradeLog ='' 
        self.name = name
        
    def __str__( self ):
         return str( self.holdings[ self.holdings.Quantity > 0 ] )

    
    def tradeCoin(self, baseCcy, baseCcyQuantity, marketCcy):
        ''' executes trade from baseCCy to marketCCy
        returns quantity of market CCy
        examples : baseCcy = btc , base ccyQuantity = 
        '''
        tradeTime = datetime.datetime.utcnow()
        tradeStr  ='Trade %i of %s to %s'%( baseCcyQuantity, baseCcy ,marketCcy ) 
        if ( self.holdings.Quantity[baseCcy]>= baseCcyQuantity ) :
            
            rate   = bookUtils.getTradePrice( baseCcy, marketCcy )
            txFee  = bookUtils.getTxFee( baseCcy )
            newCCy = (baseCcyQuantity/rate )*(1 - txFee)*( 1- bookUtils.BITFEE) 
             
             # adjust new values
            self.holdings.Quantity[baseCcy]    -= baseCcyQuantity
            self.holdings.Quantity[marketCcy]  += newCCy
            self.tradeLog += ( str(tradeTime) + ' Succesfully : ' + tradeStr + '\n')
                                               
            
            
        else :
            
            self.tradeLog += ( str(tradeTime) +  '    Failed to: ' + tradeStr + '\n')
            raise ValueError( 'Invalid you do not have %i of %s to trade'
            % (baseCcyQuantity, baseCcy) )
            

    