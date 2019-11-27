#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function to take easiest path and return it. Returns False if there is no valid path
def pathfinder(A,start,end):
    row=0
    col=start   #initialize row and column indices
    noback=[]   #list that saves columns that cannot be returned to
    path=[]     #list of indices traversed, aka path taken
    try:
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
    except:
        return(False)
    return(path)


# In[ ]:


A[path[len(path)-1][0]][path[len(path)-1][1]]=0 #sets the last node used to 0


# In[ ]:


#attempt to create a list of possible paths.
masterlist=[]
while True:
    storedpath=pathfinder(A,0,2)  #runs the pathfinder function
    if storedpath==False:         #if there is no possible path, pathfinder returns False and loop ends
        break
    else:                         #here's where im hitting issues. this part should add paths to 'masterlist' but doesn't seem to be
        masterlist.append(storedpath)  
        A[storedpath[len(storedpath)-1][0]][storedpath[len(storedpath)-1][1]]=0
        print(storedpath)
        continue

