# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from call_knock_in_and_out_european_option import *
import black_scholes_option_pricing

T = 2      #time-to-maturity
r = 0.03    #continuously compounding rate
d = 0    #dividend rate
K = 105     #Strike
S = 100     #Spot
H = 95     #Barrier level
sigma = 0.3 #volatility

#%%Compare simulated down-and-in call prices with the ones from analytical formula
DownAndIn_callArray = []
MCcallArray = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    DownAndIn_callArray.append(downAndIn_call(T, r, d, K, S, H, sigma))
    MCcallArray.append(callPricer(T, r, d, K, S, H, sigma, downAndInMC))
    
    
plt.plot(range_object, DownAndIn_callArray, label = "Down-and-in analytical call price")
plt.plot(range_object, MCcallArray, label = "Down-and-in monte carlo simulated call price")

plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T}, Strike {K}, Barrier {H}")
plt.legend()
plt.show()
    

#%%Compare simulated down-and-out call prices with the ones from analytical formula
DownAndOut_callArray = []
MCcallArray = []
DownAndIn_callArray = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    DownAndOut_callArray.append(downAndOut_call(T, r, d, K, S, H, sigma))
    MCcallArray.append(callPricer(T, r, d, K, S, H, sigma, downAndOutMC))
    DownAndIn_callArray.append(downAndIn_call(T, r, d, K, S, H, sigma))
    
DownAndOut_callArray = np.array(DownAndOut_callArray)
MCcallArray = np.array(MCcallArray)
DownAndIn_callArray = np.array(DownAndIn_callArray)
plt.plot(range_object, DownAndOut_callArray, label = "Down-and-out analytical call price")
plt.plot(range_object, MCcallArray, label = "Down-and-out monte carlo simulated call price")

plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T}, Strike {K}, Barrier {H}")
plt.legend()
plt.show()
    
    
#%%Verify knock-in + knock-out = vanilla parity 
DownAndOut_callArray = []
DownAndIn_callArray = []
callArray = []
range_object = np.array(range(110, 85, -1))
for S in range_object:
    DownAndOut_callArray.append(downAndOut_call(T, r, d, K, S, H, sigma))
    callArray.append(black_scholes_option_pricing.call(T, r, d, K, S, sigma))
    DownAndIn_callArray.append(downAndIn_call(T, r, d, K, S, H, sigma))
    
callArray = np.array(callArray)
DownAndOut_callArray = np.array(DownAndOut_callArray)
DownAndIn_callArray = np.array(DownAndIn_callArray)
plt.plot(range_object, DownAndOut_callArray, label = "Down-and-out Call price")
plt.plot(range_object, callArray, label = "Call price")
plt.plot(range_object, DownAndIn_callArray, label = "Down-and-in call price")
plt.title(f"Testing if knock-in + knock-out = vanilla")

plt.ylabel("Price")
plt.xlabel("Underlying price")
plt.legend()
plt.show()


#NOTE! knock-in + knock-out = vanilla parity for down calls holds only when H<K, otherwise call's formula uses a modified dHelper function => slight inconsistency with black-scholes calls.
#See "The Concepts and Practice of Mathematical Finance" by Mark S. Joshi pg.217-219 (theorems 8.3 and 8.4)