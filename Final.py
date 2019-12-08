#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def options(data):
    option_view=''
    for i in data:
        option_view=option_view+ ' ' + str(i)
    return(option_view)

def grab(data):
    lencheck=''
    for i in data:
        lencheck=str(i)
    return(lencheck)

def cleanup(A):
    fresh=[]
    for i in range(len(A)):
        if A[i] in fresh:
            continue
        else:
            fresh.append(A[i])
    return fresh

def Trueval(A,paths):
    pathval=[]
    for i in range(len(paths)):
        total=0
        for j in range(len(paths[i])):
            total=total+A[paths[i][j][0]][paths[i][j][1]]
        pathval.append(total)
    return(pathval)

def optimize(A,path):
    val=9999999999999999999999999999999
    best=[]
    Check=Trueval(A,path)
    for i in range(len(Check)):
        if Check[i]<val:
            val=Check[i]
            best=i
    return([val,best])

def pathfinder(A,start,end):
    if start>end:
        c=start
        start=end
        end=c
    B=np.array(list.copy(A))
    row=0
    col=start   #initialize row and column indices
    noback=[]   #list that saves columns that cannot be returned to
    working_paths=[]     #list of indices traversed, aka path taken
    path_attempt=[]
    q=0 #used for possible range vals
    p=0 # ""
    while p<len(B[0]):
        if col==end:
            working_paths.append(path_attempt)
            path_attempt=[]
            B=np.array(list.copy(A))
            q+=1
            row=0
            col=start
            noback=[]
            if len(B[0])-q==0:
                p+=1
                q=0
            for i in range(p,len(B[0])-q):
                B[i]=0
                B[:,i]=0
        if row>len(B[0])-1:
            B=np.array(list.copy(A))
            row=0
            col=start
            noback=[]
            path_attempt=[]
            q+=1
            if len(B[0])-q==0:
                p+=1
                q=0
            for i in range(p,len(B[0])-q):
                B[i]=0
                B[:,i]=0
        for i in noback:
            if row==i:
                row=row+1
        if B[row][col]>0:
            path_attempt.append([row,col])
            noback.append(col)
            col=row
            row=0
        else:
            row+=1
    return(working_paths)

def run(A,D):
    p=''
    q=cleanup(pathfinder(A[grab(A)],int(D[0])-1,int(D[1])-1))
    for i in range(D[2]):
        c=optimize(A[D[3+i]],q)
        p=p+'The optimal path for %s is %s with the value %s'%(D[3+i],q[c[1]],c[0])+'\n'
    return print(p)   


# In[5]:


AA={'PathLength':[[0,1,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]],'MPG':[[0,1,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]]}
AAA=[[0,1,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]]
A={'PathLength':[[0,1,1],[1,0,1],[1,1,0]],'MPG':[[0,2,3],[2,0,4],[3,4,0]],'Walking':[[0,9,30],[9,0,4],[30,4,0]]}


# In[11]:


Display=[]
print('Parameters for Start Location/End Location are the integers 1-' + str(len(A[grab(A)][0])))
try:
    Display.append(int(input('\nStart Location: ')))
    Display.append(int(input('\nEnd Location: ')))
    Display.append(int(input('\nAmount of variables (options will include: ' + str(options(A)) + ' ):')))
    for i in range(0,Display[2]):
        Display.append(input('\nVariable ' + str(i+1) + '\n'))
    run(A,Display)
except:
    print('Please pay attention to the prompts and enter the data exactly as displayed, keep in mind that each word in the options is a different variable name ')


# In[ ]:





# In[ ]:



