#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 25/01/10 17:40:15

@author: Changzhi Sun
"""


def isValid(s: str) -> bool:
    stack_count = 0
    for char in s:
        if char in "({[":
            stack_count += 1
        elif char in ")}]":
            if stack_count == 0:
                return False
            stack_count -= 1
    return stack_count == 0

print(isValid("([)]"))
