# -*- coding: utf-8 -*-
"""
The down-and-out formula used here comes from "The Concepts and Practice of Mathematical Finance" by Mark S. Joshi
"""

import math
import numpy as np
from scipy.stats import norm
from black_scholes_option_pricing import zero

#From here on we will use norm.cdf() function from scipy

def call(T, r, d, K, S, H, sigma) -> float:
    return S * math.exp(-d*T) * norm.cdf( dHelp(1, T, r, d, K, S, H, sigma) ) - K * math.exp(-r * T) * norm.cdf( dHelp(2, T, r, d, K, S, H, sigma) )

def put(T, r, d, K, S, H, sigma) -> float:
    return -S * math.exp(-d*T) * norm.cdf( -dHelp(1, T, r, d, K, S, H, sigma)) + K * math.exp(-r * T) * norm.cdf(-dHelp(2, T, r, d, K, S, H, sigma))

#Calculates down-and-out call value. Applies the principle that down-and-in + down-and-out = knockless.
def downAndOut_call(T, r, d, K, S, H, sigma) -> float:
    #Special case for being knocked-out
    if S <= H:  return 0
    #Use the fact that knock-in + knock-out = vanilla  
    return call(T, r, d, K, S, H,sigma) - downAndIn_call(T, r, d, K, S, H, sigma)

#Calculates down-and-in call value.
def downAndIn_call(T, r, d, K, S, H, sigma) -> float:
    if S <= H: return call(T, r, d, K, S, H, sigma)     #When the option gets knocked-in, it must follow the vanilla call's price since knock-in + knock-out = vanilla
    return ((H/S)**(1 + 2 * (r - d) * (sigma**-2)) * S * np.exp(-d * T) * norm.cdf(helper(1, T, r, d, K, S, H, sigma)) - 
            (H/S)**(-1 + 2 * (r - d) * (sigma**-2)) * K * np.exp(-r * T) * norm.cdf(helper(2, T, r, d, K, S, H, sigma)))


#Helper function from black_scholes_option_pricing file but adapted for continuous barrier case.
#See "The Concepts and Practice of Mathematical Finance" by Mark S. Joshi pg.217-219 (theorems 8.3 and 8.4)
def dHelp(n, T, r, d, K, S, H, sigma) -> float:  
    if not T:
        temp = np.inf * math.log(S/K)   #When T = 0 we only care about if S > K or not. If S>K, then the cumulative normal function needs to be 1 and 0 otherwise.
        # inf*0 is a special case, hence we'll say that cumulative function still needs to be 0.
        if math.isnan(temp):
            temp = -np.inf
        return temp
    
    #If H < K, then we have the same expression as in vanilla options.
    if H < K:
        return (math.log(S/K) + T * (r - d + 0.5 * (sigma**2) * (-1)**(n - 1)))/(sigma * math.sqrt(T))
    else:
        return (math.log(S/H) + T * (r - d + 0.5 * (sigma**2) * (-1)**(n - 1)))/(sigma * math.sqrt(T))


#Helper function similar to dHelp, but adapted for the event of a barrier crossing.
#See "The Concepts and Practice of Mathematical Finance" by Mark S. Joshi pg.217-219 (theorems 8.3 and 8.4)
def helper(n, T, r, d, K, S, H, sigma) -> float:
    if H < K:
        return (np.log((H**2)/(S * K)) + T * (r - d + (-1)**(n-1) * (sigma**2) / 2))/(sigma * np.sqrt(T))
    else:
       return (np.log(H/S) + T * (r - d + (-1)**(n-1) * (sigma**2) / 2))/(sigma * np.sqrt(T))



#Implement Monte Carlo simulation of the stock's price.
def stockPriceGenerator(dt, r, d, K, S, sigma, steps):
    for _ in range(steps):
        S = S * np.exp((r - (sigma**2)/2) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1))
        yield S


#Function to calculate a potential down-and-out option's price using Monte Carlo simulation.
#For this we have to evolve stock's price until option's maturity to see if the option kicks out.
#If it does, option pays out 0.
#Works for calls and puts.
def downAndOutMC(T, r, d, K, S, H, sigma) -> float:
    steps = 1000   #Let evolve stock price in 1000 steps 
    dt = T / steps  #time step
    S_0 = S         #Define the starting stock price
    path = []
    for S_next in stockPriceGenerator(dt, r, d, K, S_0, sigma, steps):
        if S_next <= H:
             return 0    #Return zero as the option was knocked-out
        path.append(S_next)
    return path[-1]      #We are only interested in the last stock price.


#Function to calculate a potential down-and-in option's price using Monte Carlo simulation.
#For this we have to evolve stock's price until option's maturity to see if the option kicks in.
#If it does not, option pays out 0.
#Works for calls and puts.
def downAndInMC(T, r, d, K, S, H, sigma) -> float:
    steps = 1000   #Let evolve stock price in 1000 steps 
    dt = T / steps  #time step
    S_0 = S         #Define the starting stock price
    path = []       #save the stock's path
    knocked_in = False   #Save information if the option has been knocked-in
    for S_next in stockPriceGenerator(dt, r, d, K, S_0, sigma, steps):
        if S_next < H:
             knocked_in = True
        if knocked_in:
            path.append(S_next)
    #There might be times when the option never kicks in, then we must return 0
    if len(path):
        return path[-1]      #We are only interested in the last stock price.
    return 0


#Function that returns option's price after running n Monte Carlo simulations.
def callPricer(T, r, d, K, S, H, sigma, fn) -> float:
    n = 1000    #Assume that for each S, we need to simulate n pathways
    payouts = []
    for _ in range(n):
        #Here we define if we are interested in a call or a put.
        #Currently, the following code calculates payoffs for calls.
        payouts.append(max(fn(T, r, d, K, S, H, sigma) - K, 0) * zero(T, r))    #Calculate payoff for each simulation and discount it to the present
        
    return np.average(payouts)
    













































