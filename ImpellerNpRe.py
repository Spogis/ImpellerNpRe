# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:06:32 2021

@author: Nicolas Spogis
"""

# manage data and fit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# first part with least squares
from scipy.optimize import curve_fit

#Read the data from a excel file with pandas
df = pd.read_excel (r'NpReData.xlsx') 
Reynolds = pd.DataFrame(df, columns= ['Re'])
Np = pd.DataFrame(df, columns= ['Np'])
max_value = Np.max()

#Nagata Model - Np vs Re
def nagata_model(x, a, b, f, alfa, p):
    return a/x + b*((10**3 + 0.6*f*(x**alfa))/(10**3 + 1.6*f*(x**alfa)))**p


#Curve Fit
popt, pcov = curve_fit(
    f=nagata_model,                     # model function
    xdata=df["Re"],                     # x data
    ydata=df["Np"],                     # y data
    p0=(max_value[0], 1, 1, 1, 1),      # initial value of the parameters
)

#Print Adjusted parameters
a_opt, b_opt, f_opt, alfa_opt, p_opt = popt
print("a = ", a_opt)
print("b = ", b_opt)
print("f = ", f_opt)
print("alfa =", alfa_opt)
print("p = ", p_opt)

#Nagata Model - Np vs Re
def nagata_model_Opt(x):
    return a_opt/x + b_opt*((10**3 + 0.6*f_opt*(x**alfa_opt))/(10**3 + 1.6*f_opt*(x**alfa_opt)))**p_opt

rr = np.arange(1, 10**8, 10)
plt.scatter(Reynolds, Np)
plt.plot(rr, nagata_model_Opt(rr), '-', color='red')
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.savefig("NpRe.png", dpi=100)
plt.show()