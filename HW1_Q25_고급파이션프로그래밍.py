#!/usr/bin/env python
# coding: utf-8

# # Homework 1 - Numpy

# For all the questions, print the results with a variable of your choice (e.g., Z)

# #### 1. Import the numpy package under the name `np` 

# In[26]:


import numpy as np


# #### 2. Create a vector with values ranging from 10 to 49 

# In[27]:


a=np.arange(10,50)
a


# #### 3. Reverse a vector (first element becomes last) 

# In[28]:


a_r=a[::-1]
a_r


# #### 4. Create a 3x3 matrix with values ranging from 0 to 8 

# In[29]:


a=np.arange(0,9).reshape(3,3)
a


# #### 5. Find indices of non-zero elements from [1,2,0,0,4,0] 

# In[30]:


b=np.array([1,2,0,0,4,0])
bool_idx= np.where(b!=0)
print(bool_idx)


# #### 6. Create a 3x3 identity matrix 

# In[31]:


a=np.eye(3,3)
a


# #### 7. Create a 3x3x3 array with random values 

# In[32]:


a=np.random.random((3,3,3))
a


# #### 8. Create a 10x10 array with random values and find the minimum and maximum values 

# In[33]:


c=np.random.random((10,10))
c_max=np.max(c)
c_min=np.min(c)
print('Maximum value is ',c_max) 
print('Minimum value is ',c_min)


# #### 9. Create a checkerboard 8x8 matrix using np.array([0,1],[1,0]) and the tile function  

# In[34]:


a=np.array([[0,1],[1,0]])
ans=np.tile(a,(4,4))
ans


# #### 10. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) 

# In[35]:


a=np.arange(0,15).reshape(5,3)
b=np.arange(0,6).reshape(3,2)
print(a.dot(b))


# #### 11. Create a 5x5 matrix with row values ranging from 0 to 4 using tile function as follows:
# 
array([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])
# In[37]:


a=np.arange(0,5)
b=np.tile(a,(5,1))
b_=np.asmatrix(b)
print(b_)
print(type(b_))


# #### 12. Create a 5x5 matrix with row values ranging from 0 to 4 using broadcasting
# 

# In[38]:


a=np.zeros((5,5))
b=np.arange(5,dtype='int')
print(a+b)


# #### 13. Create a random vector of size 10 and sort it 

# In[39]:


a = np.random.randint(0,50,(1,10))
a.sort()
print(a.reshape(2,5))


# #### 14. Subtract the mean of each row
# 
# X = np.random.rand(5,10)

# In[40]:


x=np.random.rand(5,10)
for row in x:
    mean=np.mean(row)
    print(row-mean)


# #### 15. Create, 10 by 10 multiplication table from 1 to 10

# In[41]:


a=np.arange(1,11)
b=a.reshape(10,1)
print(a*b)


# #### 16. How to get the diagonal of a dot product? 
# 
# A = np.random.uniform(0,1,(5,5))
# B = np.random.uniform(0,1,(5,5))

# In[42]:


A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))
print(np.diagonal(A.dot(B)))


# #### 17. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?

# In[43]:


a=np.array([1,2,3,4,5])
n=np.zeros(len(a)+3*(len(a)-1))
#print(n)
n[::4]=a
print(n)


# #### 18. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B?
# 
# A = np.random.randint(0,5,(8,3))
# B = np.random.randint(0,5,(2,2))

# In[ ]:


##A = np.random.randint(0,5,(8,3))
##B = np.random.randint(0,5,(2,2))
##print(B)
##for row in B:


# #### 19. How to swap two rows of an array? Generate an array from 0 to 24, and reshape it 5 by 5 and swap first two rows of the array

# In[44]:


a=np.arange(0,25)
a_=a.reshape((5,5))
b_=np.copy(a_)
a_[0]=a_[1]
a_[1]=b_[0]
print(a_)


# #### 20. How to find the most frequent value in an array? 
# 
# Z = np.random.randint(0,10,50). hint: np.bincount, np.argmax

# In[45]:


from collections import Counter

Z = np.random.randint(0,10,50)

freq = np.bincount(Z)

freq_ = np.max(freq)

count = Counter(Z)

val = np.array(list(count.values()))
idx = np.array(list(count.keys()))
chk = (val == freq_)

ans = idx[chk]

print('The most frequent values in the given array:', ans)


# #### 21. How to get the n largest values of an array?
# 
# start with 
# Z = np.arange(10000);
# np.random.shuffle(Z)
# , Hint: np.argsort

# In[46]:


print('Enter the n value')
n=input()
n=int(n)
Z=np.arange(10000)
np.random.shuffle(Z)
ans=np.argsort(Z)[-n:]
Z_= Z[ans]
print(Z_[0])


# #### 22. Given a two dimensional array, how to extract unique rows? 
# 
# Hint: np.unique

# In[48]:


a=np.random.randint(0,2, (5,3))
unique_rows = np.unique(a, axis=0)
print(unique_rows)


# #### 23. How to compute averages using a sliding window over an array? 
# 
# make a function with two arguments, arry and size of the sliding window, def moving_avg(arr, n)
# 

# In[2]:


import numpy as np


# In[3]:


def moving_avg(arr, n):
    arr_tmp = np.hstack([arr,arr])
    avg = np.mean(arr[0:n])

    for i in range(1,len(arr)):
        tmp = np.mean(arr_tmp[i:i+n])
        avg = np.hstack([avg, tmp])
        print(avg)  
    return avg

arr = np.arange(1,11)
a = int(input('Enter the size of sliding window:'))

moving_avg_array = moving_avg(arr, a)
mean = np.mean(moving_avg_array)
print("computed average using a sliding window over an array:", mean)


# #### 24. Find the indices of elements from 4 by 4 random matrix (0-1) which are larger than 0.5
# 
# Print a list of tuples indicating the index for row and column
# 

# In[78]:


a=np.random.random((4,4))
#print(a)
idx=(a>0.5).nonzero()
temp = [*zip(idx[0],idx[1])]
print(temp)


# #### 25. Write a function returning distance between two points
Test the function to check whether function is working correctly
Hint: There are two arguments of function indicating two points
# In[82]:


def Distance(point1, point2):
    ans= math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    return ans


# In[83]:


Distance((1,2),(3,4))


# In[84]:


Distance((0,0),(3,4))

