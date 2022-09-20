from chips import *
import numpy as np
import matplotlib.pyplot as plt

not1 = Not('_')

x = np.linspace(0, 100, 1000)
y = np.sin(x)
z = np.cos(x)
# s = np.sign(np.sin(x))
s = [1 if a>0 else 0 for a in y]
def ceval(a):
    not1.inputs['a']=a
    return eval(not1)

ns = [ceval(a) for a in s]

#plt.plot(x,y,label="$sin(x)$", color="red", linewidth=2)
#plt.plot(x,z,label="$cos(x)$", color="blue", linewidth=1)
plt.plot(x,s,label="$sign(sin(x))$", color="green", linewidth=1)
plt.plot(x,ns,label="$ns$", color="gray", linewidth=1)

plt.show()
