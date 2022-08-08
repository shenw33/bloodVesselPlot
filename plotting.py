import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter
import matplotlib.ticker as mticker

df = pd.read_excel("Vessel_Diameter.xlsx")

df.rename(columns = { 'Vessel Diameter/(µm)':'Vessel'}, inplace = True)

font = {'family' : 'Arial',
        'size'   : 24}
plt.rc('axes', linewidth=2)
plt.rc('font', **font)

fig, ax = plt.subplots( figsize = (12, 12))

sns.boxplot(data = df, x = "HUVEC Concentration", y = "Vessel", ax = ax)

# ax = sns.stripplot(data = df, x = "HUVEC Concentration", y = "Vessel" )

# ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
# plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
# ax.xaxis.get_major_formatter().set_scientific(True)
# plt.ticklabel_format(style='sci')

# Previous way
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
fmt = mticker.FuncFormatter(g)

# fmt(val) gives the format of power of 10 where val is a float in e format
labels = [format(fmt(float(label.get_text()))) for label in ax.get_xticklabels()]
ax.set_xticklabels(labels)




# fmt_new = mticker.ScalarFormatter(useMathText=True)
# ax.set_xticklabels.set_major_formatter(mticker.ScalarFormatter(useMathText=True))


ax.set( ylabel = "Vessel Diameter $\mu m$" ) 

# ax.set(xlabel="Fluorescence Intensity")
fig.tight_layout() 
plt.show()
# fig.savefig("boxplot.svg", dpi = 200)
pass