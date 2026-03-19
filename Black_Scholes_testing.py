# -*- coding: utf-8 -*-
"""
File used to test functions from black_scholes_option_pricing.py.
"""
import matplotlib.pyplot as plt
import numpy as np
from black_scholes_option_pricing import *
import greek

T = 2      # Time-to-maturity
r = 0.03    # Continuously compounding rate
d = 0    # Dividend rate
K = 100     # Strike
S = 100     # Spot
sigma = 0.3 # volatility


#%% Price of a put struck at K with maturity of T and at various spot prices S. Vega displayed as well
put_vega_array = []
putArray = []
range_object = np.array(range(80, 110))
for S in range_object:
    put_vega_array.append(greek.put_vega(T, r, d, K, S, sigma))
    putArray.append(put(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()

# Right Y-axis: Put payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Put payoff", color='tab:blue')
ax1.plot(range_object, putArray, label="put", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Vega
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Vega", color=color2)
ax2.plot(range_object, put_vega_array, label="put's vega", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()
#%% Price of a call struck at K with maturity of T and at various spot prices S. Vega displayed as well
call_vega_Array = []
callArray = []
range_object = np.array(range(80, 120))
for S in range_object:
    call_vega_Array.append(greek.call_vega(T, r, d, K, S, sigma))
    callArray.append(call(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()
# Right Y-axis: Call payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Call payoff", color=color1)
ax1.plot(range_object, callArray, label="call", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Delta
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Vega", color=color2)
ax2.plot(range_object, call_vega_Array, label="call's vega", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()






#%% Price of a put struck at K with maturity of T and at various spot prices S. Gamma displayed as well
put_gamma_array = []
putArray = []
range_object = np.array(range(80, 110))
for S in range_object:
    put_gamma_array.append(greek.put_gamma(T, r, d, K, S, sigma))
    putArray.append(put(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()

# Right Y-axis: Put payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Put payoff", color='tab:blue')
ax1.plot(range_object, putArray, label="put", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Gamma
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Gamma", color=color2)
ax2.plot(range_object, put_gamma_array, label="put's gamma", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()
#%% Price of a call struck at K with maturity of T and at various spot prices S. Gamma displayed as well
call_gamma_Array = []
callArray = []
range_object = np.array(range(80, 120))
for S in range_object:
    call_gamma_Array.append(greek.call_gamma(T, r, d, K, S, sigma))
    callArray.append(call(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()
# Right Y-axis: Call payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Call payoff", color=color1)
ax1.plot(range_object, callArray, label="call", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Gamma
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Gamma", color=color2)
ax2.plot(range_object, call_gamma_Array, label="call's gamma", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()




#%% Price of a put struck at K with maturity of T and at various spot prices S. Delta displayed as well
putArray = []
greekArray = []
range_object = np.array(range(80, 110))
for S in range_object:
    greekArray.append(greek.put_delta(T, r, d, K, S, sigma))
    putArray.append(put(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()

# Right Y-axis: Put payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Put payoff", color='tab:blue')
ax1.plot(range_object, putArray, label="put", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Delta
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Delta", color=color2)
ax2.plot(range_object, greekArray, label="put's delta", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()
#%% Price of a call struck at K with maturity of T and at various spot prices S. Delta displayed as well
callArray = []
greekArray = []
range_object = np.array(range(80, 120))
for S in range_object:
    greekArray.append(greek.call_delta(T, r, d, K, S, sigma))
    callArray.append(call(T, r, d, K, S, sigma))

fig, ax1 = plt.subplots()
# Right Y-axis: Call payoff
color1 = 'tab:blue'
ax1.set_xlabel("Underlying price")
ax1.set_ylabel("Call payoff", color=color1)
ax1.plot(range_object, callArray, label="call", color=color1)
ax1.tick_params(axis='y', labelcolor=color1)

# Left Y-axis: Delta
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("Delta", color=color2)
ax2.plot(range_object, greekArray, label="call's delta", color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2)

plt.title(f"Maturity of {T} years, strike {K}")
plt.tight_layout()
plt.show()












#%% Visualisation of Monte Carlo generated call price convergence to the analytical call value.
# We can demonstrate this by changing the number of simulated stock prices
callArray = []
monteCarloCallArray100000 = []
monteCarloCallArray1000 = []
monteCarloCallArray10 = []
range_object = np.array(range(90, 110))
for S in range_object:
    callArray.append(call(T, r, d, K, S, sigma))
    monteCarloCallArray100000.append(mCCall(T, r, d, K, S, sigma, 100000))
    monteCarloCallArray1000.append(mCCall(T, r, d, K, S, sigma, 1000))
    monteCarloCallArray10.append(mCCall(T, r, d, K, S, sigma, 10))
    
callArray = np.array(callArray)
plt.plot(range_object, callArray - monteCarloCallArray100000, label = "100000 simulated stock prices")
plt.plot(range_object, callArray - monteCarloCallArray1000, label = "1000 simulated stock prices")
plt.plot(range_object, callArray - monteCarloCallArray10, label = "10 simulated stock prices")
             
plt.ylabel("Analytical - Monte Carlo call prices")
plt.xlabel("Underlying price")
plt.title(f"Differences between the analytical and Monte Carlo generated call prices\nwith different number of simulated stock prices\nMaturity of {T} years, strike {K}")
plt.legend()
plt.show()

# We see a clear convergence between the Monte Carlo option calculation method and the Black-Scholes derived prices with an increasing number of stock price simulation.



#%% Compare call's analytical price to Monte Carlo generated ones
callArray = []
monteCarloCallArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    callArray.append(call(T, r, d, K, S, sigma))
    monteCarloCallArray.append(mCCall(T, r, d, K, S, sigma))
    
callArray = np.array(callArray)
monteCarloCallArray = np.array(monteCarloCallArray)
plt.plot(range_object, callArray - monteCarloCallArray, label = "Analytical call value - monte carlo generated call value")
plt.ylabel("Difference")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()

 






#%% Visualisation of Monte Carlo generated put price convergence to the analytical put value.
# We can demonstrate this by changing the number of simulated stock prices
putArray = []
monteCarloPutArray100000 = []
monteCarloPutArray1000 = []
monteCarloPutArray10 = []
range_object = np.array(range(90, 110))
for S in range_object:
    putArray.append(put(T, r, d, K, S, sigma))
    monteCarloPutArray100000.append(mCPut(T, r, d, K, S, sigma, 100000))
    monteCarloPutArray1000.append(mCPut(T, r, d, K, S, sigma, 1000))
    monteCarloPutArray10.append(mCPut(T, r, d, K, S, sigma, 10))
    
putArray = np.array(putArray)
plt.plot(range_object, putArray - monteCarloPutArray100000, label = "100000 simulated stock prices")
plt.plot(range_object, putArray - monteCarloPutArray1000, label = "1000 simulated stock prices")
plt.plot(range_object, putArray - monteCarloPutArray10, label = "10 simulated stock prices")
             
plt.ylabel("Analytical - Monte Carlo put prices")
plt.xlabel("Underlying price")
plt.title(f"Differences between the analytical and Monte Carlo generated put prices\nwith different number of simulated stock prices\nMaturity of {T} years, strike {K}")
plt.legend()
plt.show()

# We see a clear convergence between the Monte Carlo option calculation method and the Black-Scholes derived prices with an increasing number of stock price simulation.


#%% Compare put's analytical price to Monte Carlo generated ones
putArray = []
monteCarloPutArray = []
range_object = np.array(range(90, 110))
for S in range_object:
    putArray.append(put(T, r, d, K, S, sigma))
    monteCarloPutArray.append(mCPut(T, r, d, K, S, sigma))
    
putArray = np.array(putArray)
monteCarloPutArray = np.array(monteCarloPutArray)
plt.plot(range_object, putArray - monteCarloPutArray, label = "Analytical put value - monte carlo generated put value")
plt.ylabel("Difference")
plt.xlabel("Underlying price")
plt.title(f"Maturity of {T} years, strike {K}")
plt.legend()
plt.show()


#%% Put-Call parity. This shows that Put-Call parity works well with created functions.
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


#%% Prices of calls and puts struck at K with maturity of T and at various spot prices S
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