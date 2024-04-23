"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.


example: 
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""
from typing import List

class Solution: 

    #method 1

    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        print("orginal numslist: ", nums)
        print("size", size)

        i = 0 
        while i < size: 
            if nums[i] == val:
                print("nums[i] == val", i)
                for j in range(i+1, size):
                    print("j: ", j)
                    nums[j - 1] = nums [j]
                size -= 1 
                i -= 1
            i += 1 

        return size

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     slow = 0 
    #     fast = 0 
    #     size = len(nums)
    #     while fast < size: 
    #         if nums[fast] != val: 
    #             nums[slow] = nums[fast]
    #             slow += 1 
    #         fast += 1
    #     return slow


def main():
    solution = Solution()
    test_case = [
        ([0,1,2,3,4,5], 3),
        #([0,1,2,2,3,0,4,2], 2)
    ]

    for nums, val in test_case:
        result = solution.removeElement(nums, val)
        print(f"({nums}, {val}) -> {result}")

# Run the main function
if __name__ == "__main__":
    main()
