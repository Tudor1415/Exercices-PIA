import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x,sin, cos)
plt.show()