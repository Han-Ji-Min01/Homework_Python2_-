#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Law of large numbers
## Estimate pi from Monte Carlo simuation with increasing number of N from 0 to 1000000
## Then, visualize the errors between the estimates and the real value of pi


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


def MCM(i):
    inside = []
    for _ in range(i):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if np.sqrt(x**2 + y**2) < 1:
            inside.append((x, y))
    P_E= 4 * len(inside)/float(i)    
    return P_E

list_of_trial=[]

for x in range (1, 10000):
    trial=MCM(x)
    list_of_trial.append(trial)

plt.figure(figsize=(10, 10))
plt.ylim(2,4)
plt.plot(range(1,10000), list_of_trial)
plt.axhline(np.pi, color="b", alpha=0.5)   


# Exercise: let’s check that the error decreases proportionally to  1𝑁√ .

# In[ ]:


list_Err=[]
def Err(i):
    list_Err.append(MCM(i)-math.pi)
    
    
for x in range(1,10000):
    Err(x)


# In[ ]:


plt.loglog(np.arange(1,10000), np.abs(list_Err))
plt.loglog(1/np.sqrt(np.arange(10000)+1), color="r", alpha=0.5)
plt.xlabel("Number of iterations")
plt.ylabel("Estimation error");


# **Exercise**: use a similar Monte Carlo procedure in dimension 3 to estimate $\pi$ (your analysis will be based on the volume of a sphere of radius 1, instead of the area of a circle of radius 1). Recall that the volume of a sphere of radius $r$ is $\frac{4}{3}\pi r^3$.

# In[ ]:


N = 10_000
inside = []
for _ in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    z = np.random.uniform(-1, 1)
    if np.sqrt(x**2 + y**2 + z**2) < 1:
        inside.append((x, y, z))


# In[ ]:


estimated_pi3 = 4/3 * len(inside)/float(N)


# In[ ]:


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter([xyz[0] for xyz in inside], [xyz[1] for xyz in inside], [xyz[2] for xyz in inside], marker=".", alpha=0.5);

