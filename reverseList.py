#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 定义一个节点类
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# 定义反转函数		
def reverseList(head):
    if not head:
        return head
    
    prev = None
    while head:
        nextnode = head.next
#        prev = head
        head.next = prev
        prev = head
        head = nextnode

    return prev

# 定义一个函数，创建各节点之间的链表指针
def LinkedList1(s):
	if not s:
		return None
	tmp = ListNode(s[-1])
	for i in range(len(s)-2,-1,-1):
		head = ListNode(s[i])
		head.next = tmp
		tmp = head
	return head
	
def LinkedList2(s):
	if not s:
		return None
	head0 = ListNode(s[0])
	head = head0
	for i in range(1,len(s)):
		head.next = ListNode(s[i])
		head = head.next
	
	return head0
	
# 主体操作
s = [1,2,3,4]
"""
head = ListNode(s[0])
p1 = ListNode(s[1])
p2 = ListNode(s[2])
p3 = ListNode(s[3])
head.next = p1
p1.next = p2
p2.next = p3
p3.next = None	
"""

p1 = reverseList(LinkedList1(s))
p2 = reverseList(LinkedList2(s))
while p1:
    print p1.data
    p1 = p1.next
	
if p2: print "yoho~"

while p2:
    print p2.data
    p2 = p2.next









'''
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# 定义反转函数		
def reverseList(head):
    if not head:
        return head
    
    prev = None
    while head:
        nextnode = head.next
        head.next = prev
        prev = head
        head = nextnode

    return prev
    
    
    
def LinkedList2(s):
	if not s:
		return None
	head0 = ListNode(s[0])
	head = head0
	for i in range(1,len(s)):
		head.next = ListNode(s[i])
		head = head.next
	
	return head0
 
 
p2 = reverseList(LinkedList2(s))
while p1:
    print p1.data
    p1 = p1.next
'''
    