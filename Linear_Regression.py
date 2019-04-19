
# coding: utf-8

# In[1]:


#data 
x = [10,9,2,15,10,16,11,16]
y=[95,80,10,50,45,98,38,93]


# In[3]:


#plot distribution
import matplotlib.pyplot as plt
plt.plot(x,y,'b*')


# In[4]:


def estimate_coefficients(x,y):
    import numpy as np
    #number of observations
    N = np.size(x)
    
    #calculate mean for both x and y
    mean_x,mean_y = np.mean(x) , np.mean(y)
    
    #calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - N * mean_y * mean_x
    SS_xx = np.sum(x*x) - N * mean_x * mean_x
    
    #calulating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = mean_y - b_1 * mean_x
    
    return (b_0,b_1)


# In[5]:


def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 


# In[6]:


import numpy as np
x = np.array([10,9,2,15,10,16,11,16])
y=np.array([95,80,10,50,45,98,38,93])

# estimating coefficients 
b = estimate_coefficients(x, y) 
print("Estimated coefficients:\nb_0 = {} b_1 = {}".format(b[0], b[1])) 
  
# plotting regression line 
plot_regression_line(x, y, b) 

