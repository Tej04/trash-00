
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


points = {
    (2,4):'y',
    (4,2):'y',
    (4,4):'b',
    (4,6):'y',
    (6,2):'b',
    (6,4):'y'
}
   
K = 3 #given


# In[3]:


POINTS = points.keys()


# In[4]:


array = np.array(list(POINTS))


# In[5]:


print(array)


# In[6]:


new_point = np.array([6,6])


# In[7]:


import math
neighbours =np.argsort(np.sqrt(np.sum((array - new_point)**2,axis=1)))[:K]
print(neighbours)


# In[8]:


classVotes= {'b':0,'y':0}
for n in neighbours:
    classVotes[list(points.values())[n]]+=1


# In[9]:


print(classVotes)


# In[10]:


import operator
print(max(classVotes.items(), key=operator.itemgetter(1))[0])


# In[11]:


points[tuple(new_point)] = str(max(classVotes.items(), key=operator.itemgetter(1))[0])


# In[12]:


print(points)


# In[13]:


POINTS = points.keys()
array = np.array(list(POINTS))


# In[14]:


print(array)


# In[16]:


import matplotlib.pyplot as plt
for point in POINTS:
    plt.plot(point[0],point[1],color = points[tuple(point)],marker='*',markersize=15)
plt.grid()
plt.show()

