# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:32:46 2016

@author: njuzc
"""


#-*- coding: utf-8 -*-
#!/usr/bin/python

#Email:  boyce.ywr@gmail.com
import random
import copy
  
''''' 
随机生成0~10000000之间的数值 
'''  
def getrandata(num):  
    a=[]  
    i=0  
    while i<num:  
        a.append(random.randint(0,100))  
        i+=1  
    return a  
    
s = getrandata(30)    




# --------------------------------------------------------------------------------------    
# bubble_sort
'''
算法思想：每次从最后开始往前滚，邻接元素两两相比，小元素交换到前面
第一轮循环把最小的元素上浮至第一个位置，第二小的元素上浮至第二个位置，依次类推
'''
def bubbleSort(a):
	l=len(a)-2
	i=0
	while i<l:
		j=l
		while j>=i:
			if(a[j+1]<a[j]):
				a[j],a[j+1]=a[j+1],a[j]
			j-=1
		i+=1

s_bubble = copy.copy(s)
bubbleSort(s_bubble)



# --------------------------------------------------------------------------------------    
# Insert sort
''''' 
被注释掉的部分是c语言数组普通的插入方式 
未被注释的部分则是使用python列表的插入和删除特性改善的 
'''  
def insertSort(arr):  
    for i in range(1,len(arr)):  
        ''''' 
        tmp=arr[i] 
        j=i 
        while j>0 and tmp<arr[j-1]: 
            arr[j]=arr[j-1] 
            j-=1 
        arr[j]=tmp 
        '''  
        j=i  
        while j>0 and arr[j-1]>arr[i]:  
            j-=1  
        arr.insert(j,arr[i])  
        arr.pop(i+1)  

s_insert = copy.copy(s)
insertSort(s_insert)




# --------------------------------------------------------------------------------------    
# shell_sort
def shellSort(arr):  
    dist=len(arr)/2  
    while dist>0:  
        for i in range(dist,len(arr)):  
            tmp=arr[i]  
            j=i  
            while j>=dist and tmp<arr[j-dist]:  
                arr[j]=arr[j-dist]  
                j-=dist  
            arr[j]=tmp  
        dist/=2  



# -------------------------------------------------------------------------------------- 
# 归并排序（新开空间）
def mergesort(seq):  
    if len(seq)<=1:  
        return seq  
    mid=int(len(seq)/2)  
    left=mergesort(seq[:mid])  
    right=mergesort(seq[mid:])  
    return merge(left,right)  
  
def merge(left,right):  
    result=[]  
    i,j=0,0  
    while i<len(left) and j<len(right):  
        if left[i]<=right[j]:  
            result.append(left[i])  
            i+=1  
        else:  
            result.append(right[j])  
            j+=1  
    result+=left[i:]  
    result+=right[j:]  
    return result  
  
if __name__=='__main__':  
    seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]  
    print(mergesort(seq))  



   
# merge_sort 1  归并排序
''''' 
使用新分配的空间存储合并得到的新列表 
arr：  原始列表（数组） 
s：    需合并的第一段空间起始点 
m：    需合并的第二段空间起始点 
e：    需合并的第二段空间结束点 
'''  
def mergeWithNewSpace(arr,s,m,e):  
    i,j=s,m  
    t=0  
    newArr=[]  
    while i<m and j<=e:  
        if(arr[i]<arr[j]):  
            newArr.append(arr[i])  
            i+=1  
            t+=1  
        else:  
            newArr.append(arr[j])  
            j+=1  
            t+=1  
    if i>=m:  
        t=0  
        for i in range(s,j):  
            arr[i]=newArr[t]  
            t+=1  
    else:  
        t=0  
        for i in range(i,m):  
            newArr.append(arr[i])  
        for i in range(s,e+1):  
            arr[i]=newArr[t]  
            t+=1  
    del newArr  
def mergePassWithNewSpace(arr, n, d):  
    i=0  
    while i<(n-d) and i<(n+1-2*d):  
        mergeWithNewSpace(arr,i,i+d,i+2*d-1)  
        i=i+2*d  
    if i<n-d:  
        mergeWithNewSpace(arr,i,i+d,n-1)  
    else:  
        mergeWithNewSpace(arr,i-2*d,i,n-1)  
def mergeSortWithNewSpace(arr):  
    d=1  
    while d<len(arr):  
        mergePassWithNewSpace(arr,len(arr),d)  
        d*=2  

# merge_sort 2
''''' 
不分配新的空间存储合并得到的列表 
而是使用原列表使用插入方式存储 
arr：  原始列表（数组） 
s：    需合并的第一段空间起始点 
m：    需合并的第二段空间起始点 
e：    需合并的第二段空间结束点 
被注释掉的部分是c语言数组普通的插入方式
未被注释的部分则是使用python列表的插入和删除特性改善的 
'''  
def mergeWithoutNewSpace(arr,s,m,e):  
    i,j=s,m  
    while i<m and j<=e:  
        if arr[i]>arr[j]:  
            ''''' 
            tmp=arr[j] 
            k=j 
            while k>i: 
                arr[k]=arr[k-1] 
                k-=1 
            arr[i]=tmp 
            '''  
            arr.insert(i,arr[j])  
            arr.pop(j+1)  
            j+=1  
            m+=1  
        else:  
            i+=1  
''''' 
arr：  原始列表（数组） 
n：    数组大小 
d：    区间大小 
'''  
def mergePassWithoutNewSpace(arr, n, d):  
    i=0  
    while i<(n-d) and i<(n+1-2*d):  
        mergeWithoutNewSpace(arr,i,i+d,i+2*d-1)  
        i=i+2*d  
    if i<n-d:  
        mergeWithoutNewSpace(arr,i,i+d,n-1)  
    else:  
        mergeWithoutNewSpace(arr,i-2*d,i,n-1)  
def mergeSortWithoutNewSpace(arr):  
    d=1  
    while d<len(arr):  
        mergePassWithoutNewSpace(arr,len(arr),d)  
        d*=2  




# --------------------------------------------------------------------------------------    
# heap_sort
'''
大根堆：在一棵完全二叉树中，对于任意节点，满足性质arr[i]>=arr[2*i], arr[i]>=arr[2*i+1]  从上到下降序
小根堆：在一棵完全二叉树中，对于任意节点，满足性质arr[i]<=arr[2*i], arr[i]<=arr[2*i+1]  从上到下升序
'''  

'''
假定除了start位置的顶点外，以start位置为root的这棵二叉树是一个大根堆 
向下调整start位置的节点至合适的位置，使得这棵树重新恢复为一个大根堆 
'''  
def adjust(arr,start,size):  
    tmp=arr[start]  
    j=2*start+1  
    while j<size:  
        if j<size-1 and arr[j]<arr[j+1]:  
            j+=1  
        if tmp>=arr[j]:  
            break  
        arr[start]=arr[j]  
        start=j  
        j=2*j+1  
    arr[start]=tmp  

def buildHeap(arr):  #从一堆乱序的元素列表中建立大根堆 
    size=len(arr)  
    for i in range(size/2-1,-1,-1):  
        adjust(arr,i,size)  

def heapSort(arr):  
    size=len(arr)  
    buildHeap(arr)  
    ''''' 
    建立大根堆后，第一个元素为列表的最大元素，将它跟最后一个元素交换，列表大小-1 
    重新调整列表为大根堆，重复此操作直到最后一个元素 
    '''  
    for i in range(size-1,0,-1):  
        arr[i],arr[0]=arr[0],arr[i]  
        adjust(arr,0,i)  




# --------------------------------------------------------------------------------------    
# quick_sort
import sys  
''''' 
这个函数的作用是，从区间的第一个，最后一个和最中间的位置上选出一个中间大小的值，并把它放置在区间的第一个位置上 
这样有效消除预排序的最坏情况 
'''  
def median(a,start,end):  
    center=(start+end)/2  
    if a[start]>a[center]:  
        a[start],a[center]=a[center],a[start]  
    if a[start]>a[end]:  
        a[start],a[end]=a[end],a[start]  
    if a[center]>a[end]:  
        a[center],a[end]=a[end],a[center]  
    a[start],a[center]=a[center],a[start] 
    
def doSwap(a,start,end):  
    if start>=end:  
        return  
    i,j=start,end  
    median(a,start,end)  
    tmp=a[start]  
    while(True):  
        while(a[j]>tmp and i<j):  
            j-=1  
        if i<j:  
            a[i]=a[j]  
            i+=1  
        while(a[i]<tmp and i<j):  
            i+=1  
        if i<j:  
            a[j]=a[i]  
            j-=1  
        else:  
            break   #i和j相等的时候跳出  
    a[i]=tmp  
    doSwap(a,start,i-1)  
    doSwap(a,j+1,end)  

def quickSort(a):  
    #设置递归深度为10000000，放置数据量过大时超出递归最大深度发生exception  
    sys.setrecursionlimit(1000000)  
    doSwap(a,0,len(a)-1)  
    


