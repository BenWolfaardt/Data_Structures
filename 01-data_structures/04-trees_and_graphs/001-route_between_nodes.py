#------------------------------------------------------Question------------------------------------------------------#

# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

#--------------------------------------------------------Tips--------------------------------------------------------#

# 127 - Two well-known algorithms can do this. What are the tradeoffs between them?

# It may be worth discussing with your interviewer the tradeoffs between breadth-first search and depth-first
# search for this and other problems.

#------------------------------------------------------Solution------------------------------------------------------#

# This problem can be solved by just simple graph traversal, such as depth-first search or breadth-first search.
# We start with one of the two nodes and, during traversal, check if the other node is found. We should mark
# any node found in the course of the algorithm as "already visited" to avoid cycles and repetition of the
# nodes.

import unittest
from collections import deque

# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R

# Depth First Search

# depth-first search is a bit simpler to implement since it can be done with simple recursion.

def isRouteDepthFirstSearch(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or isRouteDepthFirstSearch(graph, node, end, visited):
                return True
    return False

# Breadth First Search

# Breadth-first search can also be useful to find the shortest path, whereas depth-first search may traverse one 
# adjacent node very deeply before ever going onto the immediate neighbors.

def isRouteBreadthFirstSearch(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                if adjacent == end:
                    return True
                else: 
                    queue.append(adjacent)
        visited.add(node)
    return False

#--------------------------------------------------------Tests-------------------------------------------------------#

class Test(unittest.TestCase):

    graph = {
        # node "A" and all of its neighbours in the [] brackets
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        # [start, end, expected]
        ("A", "L", True), # is there a route between the "A" and "L", yes, "True"
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False), # is there a route between the "Q" and "G", no,  "False"
        ("R", "A", False),
        ("P", "B", False),
    ]

    def testIsRoute(self):
        for [start, end, expected] in self.tests:
            actual = isRouteDepthFirstSearch(self.graph, start, end)
            assert actual == expected
        
    def testIsRouteBreadthFirstSearch(self):
        for [start, end, expected] in self.tests:
            actual = isRouteBreadthFirstSearch(self.graph, start, end)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()
