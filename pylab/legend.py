#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
https://matplotlib.org/gallery/api/legend.html
"""

import numpy as np
import matplotlib.pyplot as plt

a = b = np.arange(0, 3, 0.02)
c = np.exp(a)
d = c[::-1]

fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')

legend = ax.legend(loc=0)

plt.show()
