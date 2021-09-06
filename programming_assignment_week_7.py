# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:23:58 2021

@author: ADMIN
"""
#week 7 program 1
# Given a matrix with M rows and N columns,  you are required to check if the matrix is a Zero-One Matrix. A Zero-One or a Binary matrix is a matrix in which all the elements are either 0 or 1.

# Input Format

# The first line of the input contains two space separated integers M and N  which  represents  the  number  of  rows  and  the  number  of  columns  respectively.  

# Next M lines represent the elements in M rows with each line containing N space separated integers.

n,m=map(int,input().split())
b=0

for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        for k in temp:
            if k!=0 and k!=1:
                b=b+1
                break

if b==0:
    print("Yes",end="")
else:
    print("No",end="")



#week 7 program 2
# Given an integer input 'n', print a palindromic triangle of n lines as shown in the example.

# Input Format:

# The input contains a number n (n < 10)

# Output Format:

# Print n lines corresponding to the number triangle
n=int(input(""))
for i in range(1,n+1):
  for j in range(0,i):
    print(j+1,end="")
  for k in range(j,0,-1):
      print(k,end="")
  print()
  #week 7 program 3
  
# Given a N X N square matrix, transform the Matrix into a Lower Triangular Matrix by setting all the elements except the lower triangle as zero.

# ​​A Lower triangular matrix is a square matrix (where the number of rows and columns are equal) where all the elements above the diagonal are zero.

n=int(input())
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        l.append(temp)


for i in range(n):
    for j in range(n):
        if i<j:
            if j==n-1:
                print(0,end="")
            else:
                print(0,end=" ")
        else:
            if j==n-1:
                print(l[i][j],end="")
            else:
                print(l[i][j],end=" ")
        
    if i!=n-1:
      print()