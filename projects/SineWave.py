import numpy as np
import matplotlib.pyplot as plot


x=np.arange(0,10,0.1) # time
y=np.sin(x) # amplitude ##### sin fn -> calculate trignmetric sine for all x (arr)
plot.plot(x,y)
plot.title("Sine Wave")
plot.xlabel("Time")
plot.ylabel("Amplitude")

plot.show()

