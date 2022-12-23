"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.

Approach:
Bipartite Graph, BFS Traversal
"""

class Solution:
    GROUPINDEX = -1
    DEBUG = False

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        if not dislikes or len(dislikes) <= 1:
            return True

        dislikeGraph = self.createGraph(n, dislikes)
        if Solution.DEBUG: print(dislikeGraph)

        groupMap = {}
        visitedMap = {}
        
        for x in range(n):
            i = x + 1

            iGroupId = self.determineGroup(i, dislikeGraph, groupMap)
            groupMap[i] = iGroupId

            if not self.partitionNode(i, iGroupId, dislikeGraph[i], groupMap, visitedMap):
                return False
            
            if Solution.DEBUG: print("[", i, "] - GroupMap : ", groupMap)        
        
        return True

    def determineGroup(self, i: int, dislikeGraph: dict, groupMap: dict) -> int:
        """
        For determining the Group Index of a node, run a Breadth First Search of the Node and run it down its children
        We have to check if a node is already in the groupMap and depending on the depth multiply it with 1 or -1 to return
        the index for the node.  
        """
        if Solution.DEBUG: print("Determine Group Index - [", i ,"]")

        # If i is already pre-determined by a dislike before, the index should be in the groupMap
        if i in groupMap.keys():
            if Solution.DEBUG: print("Group index already exists for [", i ,"]")
            return groupMap[i]

        # Visited will act for if a node was visited and also act for storing the depth of the node
        visited = {}
        queue = []
        visited[i] = 0
        queue.append(i)

        while queue:
            n = queue.pop()
            depth = visited[n]
            for dislike in dislikeGraph[n]:
                if dislike not in visited:
                    visited[dislike] = depth + 1
                    queue.append(dislike)
                    if dislike in groupMap.keys():
                        groupIndex = (Solution.GROUPINDEX**visited[dislike]) * groupMap[dislike]
                        if Solution.DEBUG: print ("[", i ,"] Dislike found [", \
                            dislike, "] Dislike Group [", groupMap[dislike], \
                            "] Depth of disklike [", visited[dislike], "]", \
                            " Commputed Group Index is [", groupIndex, "]")
                        
                        return groupIndex
        
        if Solution.DEBUG: print("[", i ,"] Group index not found by traversing graph.  Returning default value -1")
        return Solution.GROUPINDEX



    def partitionNode(self, i: int, iIndex: int, dislikeList: list[int], groupMap: dict, visitedMap: dict) -> bool:
        if Solution.DEBUG: print("Partition Node [", i , "] iIndex [", iIndex, "] DislikeList[", dislikeList, "]" )
        if i in visitedMap.keys():
            return True
        else:
            visitedMap[i] = 1
        
        dislikeIndex = Solution.GROUPINDEX * iIndex

        if not dislikeList:
            return True
                
        for y in dislikeList:
            if y in groupMap.keys() and groupMap[y] != dislikeIndex:
                if Solution.DEBUG: print("Y is ", y, " DislikeIndex ", dislikeIndex, " i is ", i, " iIndex is ", iIndex, "groupMap is ", groupMap)
                return False
            groupMap[y] = dislikeIndex 

        return True

    def createGraph(self, n: int, dislikes: list[list[int]]) -> dict:
        dislikeGraph = {}

        for i in range(n):
            dislikeGraph[i+1] = []

        for dislike in dislikes:
            x,y = dislike
            dislikeGraph[x].append(y)
        
        for y in dislikeGraph:
            dislikeGraph[y].sort()
        return dislikeGraph    