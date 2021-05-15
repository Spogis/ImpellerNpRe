# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:47:15 2021

@author: nicol
"""

from pnglatex import pnglatex

output = pnglatex(r'\[\displaystyle{\sum_{i=0}^{10} 3i}\]', 'output.png')


# Np = \frac{A}{Re} + B*\left ( \frac{10^{3}*0.6*f*Re^{\alpha}}{10^{3}*1.6*f*Re^{\alpha}} \right )^{p}