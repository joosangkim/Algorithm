# coding=utf-8
"""
Given an array of integers and a target integer, find two indexes of the array element that sums to the target number. O(n)
ex)
Input: [2, 5, 6, 1, 10], t: 8
Output: [0, 2] // arr[0] + arr[2] = 8

Set: [(2,6), (5,3), (6,2),(1,7)]
"""

def getIdx(arr, target): 
  d = {k: v for v, k in enumerate(arr)} # n
  for v in d : # n
    if target - v in d.keys(): #O(1)
      return [d[v], d[target - v]]
  return [-1, -1]


arr = [5, 2, 6, 1, 10]
target = 8 
print(getIdx(arr, target))