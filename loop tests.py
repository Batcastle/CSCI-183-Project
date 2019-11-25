#!/usr/bin/env python
# coding: utf-8

# ## Project Algo ##

# # Matrix Parser #

# In[60]:


#LOOPS THROUGH A MATRIX
def parser(A,start,end):
    row=0
    col=start
    noback=[]
    path=[]
    while True:
        if col == end:
            break
        for i in noback:
            if row==i:
                row=row+1
        if A[row][col]>0:
            path.append([row,col])
            noback.append(col)
            col=row
            row=0
        else:
            row=row+1
    print(path)


# In[ ]:





# In[62]:


parser(A,0,3)


# In[42]:


A = [[0, 2, 3,4,5], 
    [0, 0, 6,7,8],
    [0, 6, 0,9,10],
    [0,7,9,0,11],
    [5,8,10,11,0]]


# In[ ]:




