from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database System")
        self.root.geometry("1350x800+0") #dimensions
        self.root.configure(bg="gainsbro")

if __name__=="__main__":
    root=TK()
    application=Employee(root)
    root.mainloop

from typing import List
class Solution:
    def twoSum(self, nums: List[int(input().split())], target: int(input())) -> List[int]:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if target == nums[i]+nums[j]:
                        return [i,j]
                    
                    
num = list(map(int,input().split()))
target = int(input())

s = Solution()
print(s.twoSum(num,target))