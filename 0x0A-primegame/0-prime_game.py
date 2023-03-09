#!/usr/bin/python3

def isWinner(x, nums):
    ben, maryam = 0, 0
    for round in range(x):
        n = nums[round]
        num_n = [x for x in range(1, n+1)]
        print(num_n)
        maryam_p = 2
        
