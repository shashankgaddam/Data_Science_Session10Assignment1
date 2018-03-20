
# coding: utf-8

# In[10]:


import numpy as np
def mov_avg(tlist,n):
    temp = np.cumsum(tlist, dtype = float)
    temp[n:] = temp[n:] - temp[:-n]
    return temp[n-1:]/n
#given sample input is 10,20,30,40,50,60,70,80,90,100 with k = 4
l = [10,20,30,40,50,60,70,80,90,100]
print(mov_avg(l,4))
#given problem input is 3,5,7,2,8,10,11,65,72,81,99,100,150 with k = 3
l = [3,5,7,2,8,10,11,65,72,81,99,100,150]
print(mov_avg(l,3))

