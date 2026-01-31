"""
Problem: Two Sum
Given an array of integers nums and an integer target, return the indices of the two numbers 
that add up to the target. You may assume that each input has exactly one solution, and 
you may not use the same element twice.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    """
    Find two numbers in the array that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices whose values sum to target
    """
    # Dictionary to store value -> index mapping
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    # No solution found
    return []


# Test Cases
if __name__ == "__main__":
    # Test case 1
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test 1 passed: [2, 7, 11, 15], target=9 -> [0, 1]")
    
    # Test case 2
    assert twoSum([3, 2, 4], 6) == [1, 2]
    print("Test 2 passed: [3, 2, 4], target=6 -> [1, 2]")
    
    # Test case 3
    assert twoSum([3, 3], 6) == [0, 1]
    print("Test 3 passed: [3, 3], target=6 -> [0, 1]")
    
    # Test case 4
    assert twoSum([-1, -2, -3, 5, 6, 7], 1) == [3, 4]
    print("Test 4 passed: [-1, -2, -3, 5, 6, 7], target=1 -> [3, 4]")
    
    print("\nAll tests passed!")
