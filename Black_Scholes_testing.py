# -*- coding: utf-8 -*-
"""
File used to test functions from black_scholes_option_pricing.py.
"""
import matplotlib.pyplot as plt
import numpy as np
from black_scholes_option_pricing import *

T = 0.5      #Time-to-maturity
r = 0.03    #Continuously compounding rate
d = 0    #Dividend rate
K = 100     #Strike
S = 100     #Spot
sigma = 0.3 #volatility

#%%Compare call's analytical price to Monte Carlo generated ones
callArray = []
monteCarloCallArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    callArray.append(call(T, r, d, K, S, sigma))
    monteCarloCallArray.append(mCCall(T, r, d, K, S, sigma))
    
callArray = np.array(callArray)
monteCarloCallArray = np.array(monteCarloCallArray)
plt.plot(range_object, callArray, label = "Analytical Call value")
plt.plot(range_object, monteCarloCallArray, label = "Monte Carlo generated call")
plt.plot(range_object, callArray - monteCarloCallArray, label = "Analytical Call value - Monte Carlo generated call value")
plt.ylabel("Difference")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()


#%%Compare put's analytical price to Monte Carlo generated ones
putArray = []
monteCarloPutArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    putArray.append(put(T, r, d, K, S, sigma))
    monteCarloPutArray.append(mCPut(T, r, d, K, S, sigma))
    
putArray = np.array(putArray)
monteCarloPutArray = np.array(monteCarloPutArray)
plt.plot(range_object, putArray, label = "Analytical put value")
plt.plot(range_object, monteCarloPutArray, label = "Monte Carlo generated put")
plt.plot(range_object, putArray - monteCarloPutArray, label = "Analytical Put value - Monte Carlo generated put value")
plt.ylabel("Difference")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()


#%%Put-Call parity. This shows that Put-Call parity works well with created functions.
callArray = []
putArray = []
forwardArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    callArray.append(call(T, r, d, K, S, sigma))
    putArray.append(put(T, r, d, K, S, sigma))
    forwardArray.append(forward(T, r, S, K))

#Convert to numpy array
callArray = np.array(callArray)
putArray = np.array(putArray)
forwardArray = np.array(forwardArray)

plt.plot(range_object, callArray - putArray, label = "Call - Put")
plt.plot(range_object, forwardArray, label = "Forward price")
plt.ylabel("Instrument price")
plt.xlabel("Underlying price")
plt.legend()
plt.show()

#%%Covered calls and protective puts

callArray = []
putArray = []
range_object = np.array(range(70, 130))
for S in range_object:
    callArray.append(call(T, r, d, K, S, sigma) + 100*zero(T, r))
    putArray.append(put(T, r, d, K, S, sigma) + S)

plt.plot(range_object, callArray, label = "Covered call")
plt.plot(range_object, putArray, label = "Protective put")
plt.ylabel("Instrument payoff")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()


#%%Prices of calls and puts struck at K with maturity of T and at various spot prices S
callArray = []
putArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    
    callArray.append(call(T, r, d, K, S, sigma))
    putArray.append(put(T, r, d, K, S, sigma))
plt.plot(range_object, callArray, label = "call")
plt.plot(range_object, putArray, label = "put")
plt.ylabel("Instrument payoff")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()