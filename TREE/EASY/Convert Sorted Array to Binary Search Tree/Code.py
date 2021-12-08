# PROBLEM LINK:- https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution:
    def solve(self, nums, start, end):
        if start <= end:
            mid = start + (end - start)//2;
            root = TreeNode(nums[mid])
            root.left = self.solve(nums, start, mid-1)
            root.right = self.solve(nums, mid+1, end)
            return root
        
        return None
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.solve(nums, 0, len(nums) - 1)
