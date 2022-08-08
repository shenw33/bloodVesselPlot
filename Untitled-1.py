import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

fig, ax = plt.subplots()

x = np.linspace(0, 300, 20)
y = np.linspace(0,300, 20)
y = y*1e16

ax.plot(x,y)

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

plt.show()


vals = [0.000001,0.00001,0.0001,0.01,1.0]

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
fmt = mticker.FuncFormatter(g)

fig, ax = plt.subplots()
for i,val in enumerate(vals):
    ax.plot([0,1],[i,i], label="val = {}".format(fmt(val)))

ax.legend()    
plt.show()
