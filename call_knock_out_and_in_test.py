# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from call_knock_in_and_out_european_option import *
import black_scholes_option_pricing

T = 2      # time-to-maturity
r = 0.03    # continuously compounding rate
d = 0    # dividend rate
K = 105     # Strike
S = 100     # Spot
H = 95     # Barrier level
sigma = 0.3 # volatility

#%%Compare simulated down-and-in and down-and-out call prices with the ones from analytical formula.
# Include Monte Carlo prices to show that it has similar behaviour.
DownAndIn_callArray = []
MCcallArray_in = []
DownAndOut_callArray = []
MCcallArray_out = []
call_price = []
range_object = np.array(range(115, 80, -1))
for S in range_object:
    DownAndIn_callArray.append(downAndIn_call(T, r, d, K, S, H, sigma))
    MCcallArray_in.append(callPricer(T, r, d, K, S, H, sigma, downAndInMC))
    DownAndOut_callArray.append(downAndOut_call(T, r, d, K, S, H, sigma))
    MCcallArray_out.append(callPricer(T, r, d, K, S, H, sigma, downAndOutMC))
    call_price.append(call(T, r, d, K, S, H, sigma))
    
    
plt.plot(range_object, DownAndIn_callArray, label = "Down-and-in analytical")
plt.plot(range_object, MCcallArray_in, linestyle='--', label = "Down-and-in Monte Carlo simulated")
plt.plot(range_object, DownAndOut_callArray, label = "Down-and-out analytical")
plt.plot(range_object, MCcallArray_out, linestyle='--', label = "Down-and-out Monte Carlo simulated")
plt.plot(range_object, call_price, linestyle=':', label = "Vanilla")

plt.ylabel("Option price")
plt.xlabel("Underlying price")
plt.title(f"Call prices\nMaturity of {T}, Strike {K}, Barrier {H}")
plt.legend()
plt.show()


#%% See how knocking call prices change as the Barrier changes
# Monte Carlo results included to show that simulations show similar behaviour
DownAndIn_callArray = []
DownAndOut_callArray = []
MCcallArray_in = []
MCcallArray_out = []
range_object = np.array(range(110, 75, -1))
for H in range_object:
    DownAndIn_callArray.append(downAndIn_call(T, r, d, K, S, H, sigma))
    MCcallArray_in.append(callPricer(T, r, d, K, S, H, sigma, downAndInMC))
    DownAndOut_callArray.append(downAndOut_call(T, r, d, K, S, H, sigma))
    MCcallArray_out.append(callPricer(T, r, d, K, S, H, sigma, downAndOutMC))
    
    
plt.plot(range_object, DownAndIn_callArray, label = "Down-and-in analytical")
plt.plot(range_object, MCcallArray_in, linestyle='--', label = "Down-and-in Monte Carlo")
plt.plot(range_object, DownAndOut_callArray, label = "Down-and-out analytical")
plt.plot(range_object, MCcallArray_out, linestyle='--', label = "Down-and-out Monte Carlo")

plt.ylabel("Option price")
plt.xlabel("Barrier level")
plt.title(f"Call prices\nMaturity of {T}, Strike {K}, Spot {S}")
plt.legend()
plt.show()



    
#%% Verify knock-in + knock-out = vanilla parity 
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
plt.plot(range_object, DownAndOut_callArray + DownAndIn_callArray - callArray, label = "Down-and-out + Down-and-in - knockless")
# plt.plot(range_object, callArray, label = "Call price")
# plt.plot(range_object, DownAndIn_callArray, label = "Down-and-in call price")
plt.title(f"Testing if knock-in + knock-out = vanilla")

plt.ylabel("Price")
plt.xlabel("Underlying price")
plt.legend()
plt.show()

#We can see that knock-in + knock-out = vanilla concept holds. The differences observed are on the order of 1e-6 order, which could be explained by floating point error.

#NOTE! knock-in + knock-out = vanilla parity for down calls holds only when H<K, otherwise call's formula uses a modified dHelper function => slight inconsistency with black-scholes calls.
#See "The Concepts and Practice of Mathematical Finance" by Mark S. Joshi pg.217-219 (theorems 8.3 and 8.4)

