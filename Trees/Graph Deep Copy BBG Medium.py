""" Graph Deep Copy
Medium
Given a reference to a node within an undirected graph, create a deep copy (clone) of the graph. The copied graph must be completely independent of the original one. This means you need to make new nodes for the copied graph instead of reusing any nodes from the original graph.

Example:

Constraints:
The value of each node is unique.

Every node in the graph is reachable from the given node.
 """
from ds import GraphNode
from collections import deque
"""
Definition of GraphNode:
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
"""

#BFS approach to traverse the graph and create a deep copy
def graph_deep_copy(node: GraphNode) -> GraphNode:
    if not node:
        return None

    #create hashmap so same node doesn't get repeatedly copied
    #key value is original node w its copy
    old_to_new= {node: GraphNode(node.val)}
    #typical queue of BFS approach
    queue = deque([node])

    while queue:
        #look at leftmost (oldest in queue) node
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = GraphNode(neighbor.val)
                queue.append(neighbor)
            #build the node connections (neighbors)
            old_to_new[curr].neighbors.append(old_to_new[neighbor])
    return old_to_new[node]
#O(n) time, O(n) space where n is the number of nodes in the graph

#DFS approach to traverse the graph and create a deep copy
def clone_graph(node):
    if not node:
        return None

    old_to_new = {}

    def dfs(curr):
        if curr in old_to_new:
            return old_to_new[curr]   # already cloned — just return the existing clone

        clone = Node(curr.val)
        old_to_new[curr] = clone       # record BEFORE recursing into neighbors — this is the key line

        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)