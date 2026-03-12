# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import tri_tree as tt
import binary_trees as bt
import black_scholes_option_pricing as bsop


T = 1      #time-to-maturity
r = 0.05    #continuously compounding rate
d = 0    #dividend rate
K = 100     #Strike
S = 100     #Spot
sigma = 0.3 #volatility
layers = 1000  #Layers of the binary tree. Could be interpreted as the number of time steps

#Let us investigate the convergence between the tri- and binomial models to black-scholes
trinomial = []
binomial = []
bsPrice = []
range_object = np.array(range(85, 110))
for S in range_object:
    trinomial.append(tt.callOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    binomial.append(bt.callOptionPriceCalculator(T, r, d, K, S, sigma, layers))
    bsPrice.append(bsop.call(T, r, d, K, S, sigma))
    
trinomial = np.array(trinomial)
binomial = np.array(binomial)
bsPrice = np.array(bsPrice)
plt.plot(range_object, trinomial - bsPrice, label = "trinomial call price - analytical call price")
plt.plot(range_object, binomial - bsPrice, label = "binomial call price - analytical call price")

plt.ylabel("Option price difference")
plt.xlabel("Underlying price")
plt.title(f"Trinomial and binomial price convergence\ncomparison to Black-Scholes model \nMaturity of {T}, Strike {K}")
plt.legend()
plt.show()

#NB the graph proves that trinomial model approximates the Black-Scholes model better






















