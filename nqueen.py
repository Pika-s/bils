#!/usr/bin/env python
# coding: utf-8

# In[1]:


N =8


# In[2]:


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end="")
        print()   


# In[3]:


def isSafe(row,col,sc,bsc,rl,scl,bscl):
    if(rl[row] or scl[sc[row][col]] or bscl[bsc[row][col]]):
        return False
    return True


# In[4]:


def solveNQueensUtil(board,col,sc,bsc,rl,scl,bscl):
    if(col>=N):
        return True
    
    for i in range(N):
        if(isSafe(i,col,sc,bsc,rl,scl,bscl)):
            board[i][col]=1
            rl[i]=True
            scl[sc[i][col]]=True
            bscl[bsc[i][col]]=True
            
            if(solveNQueensUtil(board,col+1,sc,bsc,rl,scl,bscl)):
                return True
            
            #backtracking
            board[i][col]=0
            rl[i]=False
            scl[sc[i][col]]=False
            bscl[bsc[i][col]]=False
            
    return False   


# In[5]:


def solveNQueens():
    
    board = [[0 for i in range(N)] for j in range(N)]
    sc = [[0 for i in range(N)] for j in range(N)]
    bsc = [[0 for i in range(N)] for j in range(N)]
    
    rl=[False]*N
    
    x = 2*N -1
    scl = [False]*x
    bscl = [False]*x
    
    for rr in range(N):
        for cc in range(N):
            sc[rr][cc]= rr+cc
            bsc[rr][cc]=rr-cc+7
    
    if(solveNQueensUtil(board,0,sc,bsc,rl,scl,bscl)==False):
        print("Solution nonexixtent")
    
    print("Solution exists/n")
    
    printSolution(board)
    
    return True             


# In[6]:


solveNQueens()


# In[ ]:




