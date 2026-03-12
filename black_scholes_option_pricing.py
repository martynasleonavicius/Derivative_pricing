# -*- coding: utf-8 -*-


"""
This script is used purely for creating Black-Scholes option pricing functions.
This will be used later on to compare prices with other pricing methods.
A lot of the functions here are used from Mark S. Joshi's book 'The Concepts and Practice of Mathematical Finance'
"""

import math
import numpy as np

#First, let us approximate cumulative normal function N(x)
def cNormalFunction(x) -> float:
    if (x < 0):
        return 1 - cNormalFunction(-x)  #Special case for negative x.
    else:
        k = 1/(1 + 0.2316419 * x)   #see section B.2.2 (pg.437)
        return 1 - math.exp(-(x**2)/2)*( k * (0.319381530 + k * (-0.356563782 + k * (1.781477937 + k * (-1.821255978 + 1.330274429 * k)))))/math.sqrt(2*math.pi)
    
    

#forward price
def forward(T, r, S, K) -> float:
    return S - K * math.exp(-T*r)

#Zero-coupon bond price
def zero(T, r):
    return math.exp(-r * T )

# Z-score of the relative distance between the stock price and strike. "How far away is the stock price from strike?"
def dHelp(n, T, r, d, K, S, sigma) -> float:  
    if not T:
        temp = np.inf * math.log(S/K)   #When T = 0 we only care about if S > K or not. If S>K, then the cumulative normal function needs to be 1 and 0 otherwise.
        # inf*0 is a special case, hence we'll say that cumulative function still needs to be 0.
        if math.isnan(temp):
            temp = -np.inf
        return temp
    return (math.log(S/K) + (r - d + 0.5 * (sigma**2) * T * (-1)**(n - 1)))/(sigma * math.sqrt(T))  #Formula 3.23, pg. 65

def call(T, r, d, K, S, sigma) -> float:
    return S * math.exp(-d*T) * cNormalFunction( dHelp(1, T, r, d, K, S, sigma) ) - K * math.exp(-r * T) * cNormalFunction( dHelp(2, T, r, d, K, S, sigma) )

def put(T, r, d, K, S, sigma) -> float:
    return -S * math.exp(-d*T) * cNormalFunction(-dHelp(1, T, r, d, K, S, sigma)) + K * math.exp(-r * T) * cNormalFunction(-dHelp(2, T, r, d, K, S, sigma))

def digitalCall(T, r, d, K, S, sigma) -> float:
    return math.exp(-r * T) * cNormalFunction( dHelp(2, T, r, d, K, S, sigma) )

def digitalPut(T, r, d, K, S, sigma) -> float:
    return math.exp(-r * T) * cNormalFunction( -dHelp(2, T, r, d, K, S, sigma) )



def monteCarloStock(T, r, d, K, S, sigma): #Simulates stock price at the option's maturity
    rand_numb = np.random.normal(0, 1, 100000)
    S_T = (S * np.exp(T * (r - d - 0.5 * (sigma**2)) + sigma * np.sqrt(T) * rand_numb)) #Simulates stock price at the option's maturity
    return np.array(S_T)

def mCCall(T, r, d, K, S, sigma):   #European call valued using Monte Carlo Method
    payoff = np.maximum(monteCarloStock(T, r, d, K, S, sigma) - K, 0)  #Calculates payoff at maturity for each generated stock price.
    return np.average(payoff) * zero(T, r)                   #Calculate the average payoff and discounts it to the present
        
    
def mCPut(T, r, d, K, S, sigma):   #European put valued using Monte Carlo Method
    payoff = np.maximum(K - monteCarloStock(T, r, d, K, S, sigma), 0)  #Calculates payoff at maturity
    return np.average(payoff) * zero(T, r)             #Calculate the average payoff and discount to present























