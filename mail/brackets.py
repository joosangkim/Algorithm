# coding=utf-8
"""
Given an integer N, find the number of possible balanced parentheses with N opening and closing brackets.
Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
"""
def brackets(ans, n, cur, open, close):
    if len(cur) == n*2:
        ans.append(cur)
        return
    
    if open < n:
        brackets(ans, n,cur+"(",open+1,close)
    
    if open > close:
        brackets(ans, n,cur+")",open,close+1)

ans = []
brackets(ans, 3, "", 0,0)
print(ans)

# result: ['((()))', '(()())', '(())()', '()(())', '()()()']

