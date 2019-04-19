
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt

#data
#P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16,
#0.85] P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]

x_points = [0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3]
y_points = [0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]

plt.plot(x_points,y_points,'b*')
plt.show()


# In[18]:


#Let's say initial centroids are denoted by m1 and m2 and as per given information m1=P1 and m2=P8
#It is asked to have 2 clusters.

def euclideanDistance(point,x,y):
    return math.sqrt(((point[0]-x)**2) + ((point[1]-y)**2))
    

def returnCluster(m1,m2,x,y):
    dist1 = euclideanDistance(m1,x,y)
    dist2 = euclideanDistance(m2,x,y)
    
    if dist1<dist2:
        return 1
    elif dist1>=dist2:
        return 2

m1=[0.1,0.6]
m2=[0.3,0.2]

import math
difference = math.inf
threshold=0.02

cluster1=[]
cluster2=[]
while difference > threshold:
    print(m1)
    print(m2)
    print('*************************')
    cluster1=[]
    cluster2=[]
    #step1 assign all points to nearest cluster
    for i in range(len(x_points)):
        clusterNumber = returnCluster(m1,m2,x_points[i],y_points[i])
        point = [x_points[i],y_points[i]]
        if clusterNumber == 1:
            cluster1.append(point)
        else:
            cluster2.append(point)
            
    
    #step2 calculate new centroid
    #for cluster1
    xSum=0.0
    ySum=0.0
    for i in range(len(cluster1)):
        xSum+=cluster1[i][0]
        ySum+=cluster1[i][1]
    
    xSum = xSum/len(cluster1)
    ySum = ySum/len(cluster1)
    
    
    m1old = m1
    m1=[]
    m1 = [xSum,ySum]
    #for cluster2
    xSum=0.0
    ySum=0.0
    for i in range(len(cluster2)):
        xSum+=cluster2[i][0]
        ySum+=cluster2[i][1]
    
    xSum = xSum/len(cluster2)
    ySum = ySum/len(cluster2)
    
    
    m2old=m2
    m2=[]
    m2 = [xSum,ySum]
    
    #step3 averaging difference of adjustment
    #m1 and m1old
    xAvg = 0.0
    yAvg = 0.0
    
    xAvg = math.fabs(m2[0]-m2old[0])+ math.fabs(m1[0]-m1old[0])
    xAvg = xAvg / 2
    
    yAvg = math.fabs(m2[1]-m2old[1])+ math.fabs(m1[1]-m1old[1])
    yAvg = yAvg/2
    
    if xAvg>yAvg:
        difference = xAvg
    else:
        difference=yAvg

        
    print('difference = ',difference)
        
        
        
            
            
        
    
    


# In[17]:


#plotting cluster1
print(m1)
print(m2)
print(cluster1)
print(cluster2)
x1 = [x[0] for x in cluster1]
y1 = [x[1] for x in cluster1]

plt.plot(x1,y1,'ro')

x2 = [x[0] for x in cluster2]
y2 = [x[1] for x in cluster2]

plt.plot(x2,y2,'g^')

plt.show()



