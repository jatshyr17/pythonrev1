class Solution:
  def rotate(self, nums, k):
    """
    Rotates an array to the right by k steps using extra space.

    Args:
        nums: The original integer array.
        k: The number of positions to rotate by (non-negative).

    Returns:
        A new array with the rotated elements.
    """
   
    n = len(nums) 
    temp1 = nums[k:]
    temp2 = nums[:k]  # Store first k elements
    return temp1 + temp2 # Shift remaining elements and append temp

        
