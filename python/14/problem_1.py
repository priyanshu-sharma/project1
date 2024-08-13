from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldnew = {}
        def bfs(node):
            if node in oldnew:
                return oldnew[node]
            copy = Node(node.val)
            oldnew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(bfs(nei))
            return copy
        return bfs(node) if node else None
