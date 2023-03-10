#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Q2. program to reverse the letters of a string

def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # returns the reverse string to the caller function  
     
str = "zahra"    # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  


# In[28]:


#Q5. The cost of stock on each day is given in an array A[] of size N. Find all the segments
#of days on which you buy and sell the stock so that in between those days your profit is
#maximum.

def find_max_profit(A):
    n = len(A)
    if n == 0:
        return "No Profit"
    min_price = A[0]
    max_profit = 0
    buy_day = sell_day = 0
    start = 0
    for i in range(1, n):
        if A[i] < min_price:
            min_price = A[i]
            start = i
        else:
            profit = A[i] - min_price
            if profit > max_profit:
                max_profit = profit
                buy_day = start
                sell_day = i
    if max_profit == 0:
        return "No Profit"
    else:
        return (buy_day, sell_day)


A = [7, 1, 5, 3, 6, 4]
result = find_max_profit(A)
if result == (1, 4):
    print(1)
else:
    print(0)

A = [7, 6, 4, 3, 1]
result = find_max_profit(A)
if result == "No Profit":
    print(1)
else:
    print(0)








# In[26]:


#Q6. Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check
#whether it contains any cycle or not

def hasCycle(V, adj):
    visited = [False] * V
    stack = [False] * V

    def DFS(node):
        visited[node] = True
        stack[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if DFS(neighbor):
                    return True
            elif stack[neighbor]:
                return True

        stack[node] = False
        return False

    for node in range(V):
        if not visited[node]:
            if DFS(node):
                return True


# In[ ]:




