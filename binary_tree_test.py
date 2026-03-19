# -*- coding: utf-8 -*-

import binary_trees as bt
import numpy as np
import matplotlib.pyplot as plt
import black_scholes_option_pricing


T = 1      # time-to-maturity
r = 0.05    # continuously compounding rate
d = 0    # dividend rate
K = 100     # Strike
S = 100     # Spot
sigma = 0.3 # volatility
layers = 1000  # Layers of the binary tree. Could be interpreted as the number of time steps

#%%Here we compare American call option prices with the European one. We hope to see American prices to be higher than the European ones ONLY WHEN d > 0.
european0 = []
american0 = []
european2 = []
american2 = []
european4 = []
american4 = []
range_object = np.array(range(85, 110))
for S in range_object:
    
    european0.append(bt.callOptionPriceCalculator(T, r, 0, K, S, sigma, layers))
    american0.append(bt.callAmerican(T, r, 0, K, S, sigma, layers))
    european2.append(bt.callOptionPriceCalculator(T, r, 0.05, K, S, sigma, layers))
    american2.append(bt.callAmerican(T, r, 0.05, K, S, sigma, layers))
    european4.append(bt.callOptionPriceCalculator(T, r, 0.1, K, S, sigma, layers))
    american4.append(bt.callAmerican(T, r, 0.1, K, S, sigma, layers))
    
european0 = np.array(european0)
american0 = np.array(american0)
european2 = np.array(european2)
american2 = np.array(american2)
european4 = np.array(european4)
american4 = np.array(american4)
plt.plot(range_object, american0 - european0, label = "dividend yield = 0")
plt.plot(range_object, american2 - european2, label = "dividend yield = 0.05")
plt.plot(range_object, american4 - european4, label = "dividend yield = 0.1")

plt.ylabel("American - European call")
plt.xlabel("Underlying price")
plt.title(f"Comparison of American and European call options priced\nusing binomial trees with different dividend yields\nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

# From these graphs we can see that American call options are in fact more expensive than European ones <=> d>0.
# And the American premium increases more and more with higher dividend yields

#%%Here we compare American put option prices with the European one. We hope to see American prices to be higher than the European one
european0 = []
american0 = []
european2 = []
american2 = []
european4 = []
american4 = []

range_object = np.array(range(110, 85, -1))
for S in range_object:
    european0.append(bt.putOptionPriceCalculator(T, r, 0, K, S, sigma, layers))
    american0.append(bt.putAmerican(T, r, 0, K, S, sigma, layers))
    european2.append(bt.putOptionPriceCalculator(T, r, 0.01, K, S, sigma, layers))
    american2.append(bt.putAmerican(T, r, 0.01, K, S, sigma, layers))
    european4.append(bt.putOptionPriceCalculator(T, r, 0.05, K, S, sigma, layers))
    american4.append(bt.putAmerican(T, r, 0.05, K, S, sigma, layers))
    
european0 = np.array(european0)
american0 = np.array(american0)
european2 = np.array(european2)
american2 = np.array(american2)
european4 = np.array(european4)
american4 = np.array(american4)
plt.plot(range_object, american0 - european0, label = "dividend yield = 0")
plt.plot(range_object, american2 - european2, label = "dividend yield = 0.01")
plt.plot(range_object, american4 - european4, label = "dividend yield = 0.05")


plt.ylabel("American - European put")
plt.xlabel("Underlying price")
plt.title(f"Comparison of American and European put options priced\nusing binomial trees with different dividend yields\nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

#We can notice that the higher the dividend yield, the smaller the american option's premium
# => if there is a high dividend yield on a stock, an American put option offers no advantage for early excercise

#%% Demonstrate how fast binary put prices converge with analytical prices
putArray = []
binaryPutArray1000 = []
binaryPutArray100 = []
binaryPutArray10 = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    putArray.append(black_scholes_option_pricing.put(T, r, d, K, S, sigma))
    binaryPutArray1000.append(bt.putOptionPriceCalculator(T, r, d, K, S, sigma, 1000))
    binaryPutArray100.append(bt.putOptionPriceCalculator(T, r, d, K, S, sigma, 100))
    binaryPutArray10.append(bt.putOptionPriceCalculator(T, r, d, K, S, sigma, 10))
    
putArray = np.array(putArray)
binaryPutArray1000 = np.array(binaryPutArray1000)
binaryPutArray100 = np.array(binaryPutArray100)
binaryPutArray10 = np.array(binaryPutArray10)
plt.plot(range_object, putArray - binaryPutArray1000, label = "1000 layers")
plt.plot(range_object, putArray - binaryPutArray100, label = "100 layers")
plt.plot(range_object, putArray - binaryPutArray10, label = "10 layers")

plt.ylabel("Analytical - binary tree put price")
plt.xlabel("Underlying price")
plt.title(f"Binomial tree put price convergence to Black-Scholes\nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

# Fewer layers lead oscillatory periodic error.




#%% Demonstrate how fast binary call prices converge with analytical prices
callArray = []
binaryCallArray1000 = []
binaryCallArray100 = []
binaryCallArray10 = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    callArray.append(black_scholes_option_pricing.call(T, r, d, K, S, sigma))
    binaryCallArray1000.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, 1000))
    binaryCallArray100.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, 100))
    binaryCallArray10.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, 10))
    
callArray = np.array(callArray)
binaryCallArray1000 = np.array(binaryCallArray1000)
binaryCallArray100 = np.array(binaryCallArray100)
binaryCallArray10 = np.array(binaryCallArray10)
plt.plot(range_object, callArray - binaryCallArray1000, label = "1000 layers")
plt.plot(range_object, callArray - binaryCallArray100, label = "100 layers")
plt.plot(range_object, callArray - binaryCallArray10, label = "10 layers")

plt.ylabel("Analytical - binary tree call price")
plt.xlabel("Underlying price")
plt.title(f"Binomial tree call price convergence to Black-Scholes\nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

# NOTE: OverflowError when layers = 1000.
# Fewer layers lead oscillatory periodic error. Also, the results are identical to the put option calculation






