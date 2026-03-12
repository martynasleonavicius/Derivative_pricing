# -*- coding: utf-8 -*-

"""
Script for pricing various options using a binary tree. We shall consider only constant volatility
"""

import numpy as np
import math
from scipy.special import binom


#Calculates the time step
def timeStep(T, layers):
    return T/layers
    

#Calculate the size of the up move
#We construct the up and down moves so that up*down = 1 as per Cox, Ross and Rubinstein method
def upMoves(T, r, d, sigma, layers):
    dt = timeStep(T, layers)
    return np.exp(sigma * np.sqrt(dt))


#create a function to find risk neutral probability of stock price going up
def riskNeutralProbability(T, r, d, K, S, sigma, layers):
    up = upMoves(T, r, d, sigma, layers)   #up-move
    down = 1/up     #down-move    
    #This is the only place where (d) dividend rate was used in calculating stock price.
    #From the expression we see that d > 0 reduces the risk neutral probability of the stock price increasing, which explains why american calls are more expensive than european ones.
    return (np.exp(timeStep(T, layers) * (r - d)) - down)/(up - down)   


def binaryTree(T, r, d, K, S, sigma, layers):   #Used to creat the final layer of potential stock prices
    #Here we will define volatility as stock price's up or down movement
    
    up = upMoves(T, r, d, sigma, layers)
    
    S_val = []
    #We utilize the fact the the number of layers in a binary tree is the same as the number of ending stock price states
    for i in range(layers+1):
        #We calculate ending stock prices by multiply the initial stock prices by i number of up-moves and layer-i number of down moves
        S_val.append(S * (up**(2*i - layers)))
        
    return S_val


#Since all the information is already in the last layer of the stock price binomial distribution
#we can use the binomial distribution's properties to calculate vanilla option payouts
def callOptionPriceCalculator(T, r, d, K, S, sigma, layers):
    payouts = np.maximum(np.array(binaryTree(T, r, d, K, S, sigma, layers)) - K, 0)    #Calculate payoff at each stock price
    payouts = payouts * np.exp(-T * r)  #Discount payouts to present
    p = riskNeutralProbability(T, r, d, K, S, sigma, layers)
    expectation = 0
    for i in range(layers+1):
        expectation += payouts[i] * binom(layers, i) * (p**i) * ((1-p)**(layers - i))    #weigh each payout by the number of possible paths to get to a stock price but divide it by the total number of paths 
    return expectation

#For completeness, let's create binomial tree pricer of European put options
def putOptionPriceCalculator(T, r, d, K, S, sigma, layers):
    payouts = np.maximum(K - np.array(binaryTree(T, r, d, K, S, sigma, layers)), 0)    #Calculate payoff at each stock price
    payouts = payouts * np.exp(-T * r)  #Discount payouts to present
    p = riskNeutralProbability(T, r, d, K, S, sigma, layers)
    expectation = 0
    for i in range(layers+1):
        expectation += payouts[i] * binom(layers, i) * (p**i) * ((1-p)**(layers - i))    #weigh each payout by the number of possible paths to get to a stock price but divide it by the total number of paths 
    return expectation



#American put option price
def putAmerican(T, r, d, K, S, sigma, layers):
    p = riskNeutralProbability(T, r, d, K, S, sigma, layers)
    stockPriceTracker = np.array(binaryTree(T, r, d, K, S, sigma, layers))     #compute final stock prices
    potentialPayouts = np.maximum(K - stockPriceTracker, 0)                       #possible payouts
    up = upMoves(T, r, d, sigma, layers)
    
    #To value continuation and early exercise we'll need to compute those values at each node.
    #If the expected value of continuation if less than the value of exercising at t_i, then we exercise at that node.
    #This means in the array we'll save the exercise value, not the continuation one.
    #The best algorithm to use here is BACKWARD INDUCTION
    for _ in range(layers):     #Each iteration of the loop goes backward in time by a single time step
        potentialPayouts = np.exp(-r * timeStep(T, layers)) * (p * potentialPayouts[1:] + (1-p) * potentialPayouts[:-1])
        #at this point potential payouts only have continuation values.
        #Now we need to compute the stock prices at that time
        stockPriceTracker = stockPriceTracker[1:]/up   #This works because it is equivalent to all stock prices going down. The only one that can't move down gets removed (which is the first one)
        exerciseNowPayout = np.maximum(K - stockPriceTracker, 0)
        #Now we have to replace potentialPayouts with the exerciseNow values if they are bigger
        potentialPayouts = np.maximum(potentialPayouts, exerciseNowPayout)     #Vectorised numpy operation
                
        #after this we get the appropriate payout array for the american option and thus we can repeat until a single value is left in potentialPayouts

    return potentialPayouts[0]



#American call option price
def callAmerican(T, r, d, K, S, sigma, layers):
    p = riskNeutralProbability(T, r, d, K, S, sigma, layers)
    stockPriceTracker = np.array(binaryTree(T, r, d, K, S, sigma, layers))     #compute final stock prices
    potentialPayouts = np.maximum(stockPriceTracker - K, 0)                       #possible payouts
    up = upMoves(T, r, d, sigma, layers)
    
    #To value continuation and early exercise we'll need to compute those values at each node.
    #If the expected value of continuation if less than the value of exercising at t_i, then we exercise at that node.
    #This means in the array we'll save the exercise value, not the continuation one.
    #The best algorithm to use here is BACKWARD INDUCTION
    for _ in range(layers):     #Each iteration of the loop goes backward in time by a single step
        potentialPayouts = np.exp(-r * timeStep(T, layers)) * (p * potentialPayouts[1:] + (1-p) * potentialPayouts[:-1])
        #at this point potential payouts only have continuation values.
        #Now we need to compute the stock prices at that time
        stockPriceTracker = stockPriceTracker[1:]/up   #This works because it is equivalent to all stock prices going down. The only one that can't move down gets removed (which is the first one)
        exerciseNowPayout = np.maximum(stockPriceTracker - K, 0)
        #Now we have to replace potentialPayouts with the exerciseNow values if they are bigger
        potentialPayouts = np.maximum(potentialPayouts, exerciseNowPayout)     #Vectorised numpy operation
                
        #after this we get the appropriate payout array for the american option and thus we can repeat until a single value is left in potentialPayouts

    return potentialPayouts[0]
























