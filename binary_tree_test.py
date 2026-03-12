# -*- coding: utf-8 -*-

import binary_trees as bt
import numpy as np
import matplotlib.pyplot as plt
import black_scholes_option_pricing


T = 1      #time-to-maturity
r = 0.05    #continuously compounding rate
d = 0.2    #dividend rate
K = 100     #Strike
S = 100     #Spot
H = 110     #Barrier level
sigma = 0.3 #volatility
layers = 1000  #Layers of the binary tree. Could be interpreted as the number of time steps

#%%Here we compare American call option prices with the European ones. We hope to see American prices to be higher than European ones ONLY WHEN d > 0.
european = []
american = []
range_object = np.array(range(85, 110))
for S in range_object:
    european.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    american.append(bt.callAmerican(T, r, d, K, S, sigma, layers))
    
european = np.array(european)
american = np.array(american)
plt.plot(range_object, american - european, label = "American call prices - European call prices")


plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Comparison of American and European call options priced \nusing binomial trees \nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()


#%%Here we compare American put option prices with the European ones. We hope to see American prices to be higher than European ones
european = []
american = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    european.append(bt.putOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    american.append(bt.putAmerican(T, r, d, K, S, sigma, layers))
    
european = np.array(european)
american = np.array(american)
plt.plot(range_object, american - european, label = "American put prices - European put prices")


plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Comparison of American and European put options priced \nusing binomial trees \nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

#From these graphs we can see that American call options are in fact more expensive than European ones <=> d>0.
#%%Compare binary put prices with the ones from analytical formula
putArray = []
binaryPutArray = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    putArray.append(black_scholes_option_pricing.put(T, r, d, K, S, sigma))
    # print(S)
    binaryPutArray.append(bt.putOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    
putArray = np.array(putArray)
binaryPutArray = np.array(binaryPutArray)
plt.plot(range_object, putArray - binaryPutArray, label = "Analytical put price - binary put price")

plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T}, Strike {K}")
plt.legend()
plt.show()


#%%Compare binary call prices with the ones from analytical formula
callArray = []
binaryCallArray = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    callArray.append(black_scholes_option_pricing.call(T, r, d, K, S, sigma))
    # print(S)
    binaryCallArray.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    
callArray = np.array(callArray)
binaryCallArray = np.array(binaryCallArray)
plt.plot(range_object, callArray - binaryCallArray, label = "Analytical call price - binary call price")

plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T}, Strike {K}")
plt.legend()
plt.show()

#NOTE: OvergflowError when layers = 1000.







