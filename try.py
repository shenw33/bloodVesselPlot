import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1, .01)
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
# fig.text(0.5, 0.975, 'With mathtext',
#          horizontalalignment='center',
#          verticalalignment='top')



ax.plot( np.linspace(1, 1e6, num = 10), np.linspace(1, 1e6, num = 10))
ax.ticklabel_format(useMathText=True)

print("ADDING")

plt.show()