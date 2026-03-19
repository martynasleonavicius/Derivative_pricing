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

#Let us investigate the convergence between the tri- and binomial models to Black-Scholes
trinomial = []
binomial= []

bsPrice = bsop.call(T, r, d, K, S, sigma)


range_object = np.array(range(1, 11))
for layer in range_object:
    t = tt.callOptionPriceCalculator(T, r, d, K, S, sigma, layer)
    b = bt.callOptionPriceCalculator(T, r, d, K, S, sigma, layer)
    
    trinomial.append(t - bsPrice)
    binomial.append(b - bsPrice)
    

trinomial = np.array(trinomial)
binomial = np.array(binomial)


plt.plot(range_object*100, trinomial, label = "trinomial tree difference")
plt.plot(range_object*100, binomial, label = "binomial tree difference")



plt.ylabel("Difference to vanilla call")
plt.xlabel("Number of layers in a tree")
plt.hlines(0, 100, 1000, linestyles=':', color='red')
plt.title(f"Demonstration of binomial and trinomial tree convergence to\nBlack-Scholes expression for at-the-money call option\nS=K=100")
plt.legend()
plt.show()

#NB Trinomial tree method has the lowest error over the whole range of layers and approaches Black-Scholes
# price monotonically from below, whereas the binomial tree oscillates around the Black-Scholes price.
# Thus trinomial tree approximates Black-Scholes prices better than binomial tree at the same layer count.






















