# -*- coding: utf-8 -*-
"""
This script is used purely for creating Black-Scholes option pricing functions.
This will be used later on to compare prices with other pricing methods.
A lot of the functions here are used from Mark S. Joshi's book 'The Concepts and Practices of Mathematical Finance'
"""

import numpy as np
from scipy.stats import norm

def cumulativeNormalFunctionDerivative(x):
    return np.exp(-(x**2)/2)/np.sqrt(2*np.pi)

# Z-score of the relative distance between the stock price and strike. "How far away is the stock price from strike?"
def dHelp(n, T, r, d, K, S, sigma) -> float:  
    if not T:
        temp = np.inf * np.log(S/K)   #When T = 0 we only care about if S > K or not. If S>K, then the cumulative normal function needs to be 1 and 0 otherwise.
        # inf*0 is a special case, hence we'll say that cumulative function still needs to be 0.
        if np.isnan(temp):
            temp = -np.inf
        return temp
    return (np.log(S/K) + (r - d + 0.5 * (sigma**2) * T * (-1)**(n - 1)))/(sigma * np.sqrt(T))  #Formula 3.23, pg. 65

def call_delta(T, r, d, K, S, sigma) -> float:
    return np.exp(-d * T) * norm.cdf(dHelp(1, T, r, d, K, S, sigma))

def put_delta(T, r, d, K, S, sigma) -> float:
    return - np.exp(-d * T) * norm.cdf(- dHelp(1, T, r, d, K, S, sigma))

def call_gamma(T, r, d, K, S, sigma) -> float:
    return np.exp(-d * T) * cumulativeNormalFunctionDerivative( dHelp(1, T, r, d, K, S, sigma) )/(sigma * S * np.sqrt(T))

def put_gamma(T, r, d, K, S, sigma) -> float:
    return np.exp(-d * T) * cumulativeNormalFunctionDerivative( dHelp(1, T, r, d, K, S, sigma) )/(sigma * S * np.sqrt(T))


def call_vega(T, r, d, K, S, sigma):
    return np.exp(-d * T) * S * cumulativeNormalFunctionDerivative( dHelp(1, T, r, d, K, S, sigma) ) * np.sqrt(T)


def put_vega(T, r, d, K, S, sigma):
    return np.exp(-d * T) * S * cumulativeNormalFunctionDerivative( -dHelp(1, T, r, d, K, S, sigma) ) * np.sqrt(T)
     

