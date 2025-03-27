# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que1 = deque([p])
        que2 = deque([q])

        while que1 and que2:
            cur1, cur2 = que1.popleft(), que2.popleft()
            if not cur1 and not cur2:
                continue
            if not cur1 or not cur2:
                return False
            if cur1.val != cur2.val:
                return False

            que1.append(cur1.left)
            que1.append(cur1.right)
            que2.append(cur2.left)
            que2.append(cur2.right)
            

        return not que1 and not que2
        