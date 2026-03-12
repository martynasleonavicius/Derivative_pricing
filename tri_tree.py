# -*- coding: utf-8 -*-
"""
Here we will try to price European and American options using recombining tri-trees.
For simplicity, we are working with constant volatilities
"""

import numpy as np


#Calculates the time step
def timeStep(T, layers):
    return T/layers
    

#Calculate the size of the up move
#We construct the up and down moves so that up*down = 1 as per Cox, Ross and Rubinstein method
def upMoves(T, sigma, layers):
    dt = timeStep(T, layers)
    return np.exp(sigma * np.sqrt(dt/2))

#See https://en.wikipedia.org/wiki/Trinomial_tree
def upMoveProbability(T, r, d, sigma, layers):
    dt = timeStep(T, layers)
    return ( (np.exp(dt * (r - d)/2) - np.exp(-sigma * np.sqrt(dt / 2)))/(np.exp(sigma * np.sqrt(dt / 2)) - np.exp(-sigma * np.sqrt(dt / 2))) )**2

#See https://en.wikipedia.org/wiki/Trinomial_tree
def downMoveProbability(T, r, d, sigma, layers):
    dt = timeStep(T, layers)
    return ( (-np.exp(dt * (r - d)/2) + np.exp(sigma * np.sqrt(dt / 2)))/(np.exp(sigma * np.sqrt(dt / 2)) - np.exp(-sigma * np.sqrt(dt / 2))) )**2


def triTree(T, r, d, S, sigma, layers):
    up = upMoves(T, sigma, layers)
    S_fin = []      #For recording stock prices at option's maturity
    #This is a very similar algorithm to the binary tree algorithm, except with every additional layer 2 new nodes exist, as opposed to 1 in a binary model
    for i in range(2 * layers + 1):
        S_fin.append(S * (up ** (2*i - 2 * layers)))
        
    return S_fin
    
#Let us use backward iduction process to find European call prices
def callOptionPriceCalculator(T, r, d, K, S, sigma, layers):
    payouts = np.maximum(np.array(triTree(T, r, d, S, sigma, layers)) - K, 0)
    p_up = upMoveProbability(T, r, d, sigma, layers)        #Probability that stock price goes up
    p_down = downMoveProbability(T, r, d, sigma, layers)    #Probability that stock price goes down
    p_nothing = 1 - p_up - p_down                           #Probability of staying the same
    dt = timeStep(T, layers)
    for _ in range(layers):
        payouts = np.exp(- r * dt) * (p_up * payouts[2:] + p_down * payouts[:-2] + p_nothing * payouts[1:-1])
    
    return payouts[0]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    