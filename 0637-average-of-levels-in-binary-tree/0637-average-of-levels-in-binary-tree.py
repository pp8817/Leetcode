from collections import deque

# TreeNode 정의
# class TreeNode:
#     def __init__(self, val: float = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_sum / level_count)
        
        return result