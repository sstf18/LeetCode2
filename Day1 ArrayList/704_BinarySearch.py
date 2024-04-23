"""
Given an array of integers "nums" which is sorted in ascending order, and an integer "target" in "nums"
if "target" exsits, then return its index. Otherwise, return -1. 

For example: 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

solution: 
left, right, middle. 
middle = left + (right - left)//2 

"""


from typing import List # used to annotate variables or function parameters/return to specify that they are supposed to be list.
# from ast import List       used to meta-programming, not in regular programming task. 



class Solution: 
    def search(self, nums: List[int], target:int) -> int: 
        left = 0 
        right = len(nums)
        middle = 0 

        while left < right: 
            print("right", right)
            print("left", left)
            print("right - left", (right - left))
            middle = left + (right - left)//2
            print("middle" , middle)
            if nums[middle] == target: 
                print("nums[mid] = target")
                return  middle
            elif nums[middle] < target: 
                print("nums[mid] < target")
                left = middle + 1
            elif nums[middle] > target: 
                print("nums[mid] > target")
                right = middle
        return -1

def main():
    # Create an instance of the solution class 
    solution = Solution()

    # define test cases
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),   # Normal case
        #([1, 2, 3, 4, 5], 6),   # Target not in list
        #([], 1),                # Empty list
        #([1], 1),               # Single element, target is present
        #([1], 2)                # Single element, target is absent
    ]

    # Test each case
    for nums, target in test_cases: 
        result = solution.search(nums, target)
        print(f"search({nums}, {target}) -> {result}")

# Run the main function
if __name__ == "__main__":
    main()