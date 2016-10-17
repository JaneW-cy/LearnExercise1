#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
import sys
(n,m,k) = map(int,sys.stdin.readline().strip().split())
student = []
for i in range(n):
    student.append(map(int,sys.stdin.readline().strip().split()))

print student	
"""
(n,m,k) = (2,2,100)
student = [[1600012345, 500, 2, 1, 400, 2, 300], [1600054321, 1100, 1, 2, 300]]
	
# jiedian
class ListNode:
	def __init__(self,s,list):
		self.stuid = s[0]
		self.office = list[0]
		self.time = list[1]
		self.next = None

# linked list		
def LinkedList(s):
	if not s:
		return None
	num_office = (len(s)-3)/2
	head0 = ListNode(s,s[3:5])
	head = head0
	for i in range(1,num_office):
		head.next = ListNode(s,s[3+2*i:5+2*i])
		head = head.next
	return head0

student1 = LinkedList(student[1])

while student1:
    print (student1.office,student1.time)
    student1 = student1.next




