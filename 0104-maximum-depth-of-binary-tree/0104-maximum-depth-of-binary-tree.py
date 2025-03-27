from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            for _ in range(len(q)):
                t = q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            depth += 1

        return depth
        