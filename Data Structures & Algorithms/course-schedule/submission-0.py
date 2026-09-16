class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #course is a node, prerequisite is an edge
        #as long as no cycle is detected, it's valid

        #set an adjacency list to store courses & pre reqs
        #map it to an empty list
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #a set to store all courses in the DFS path
        visited = set()

        #dfs function to traverse graph
        def dfs(crs):
            #edge case: if course is traversed already
            if crs in visited:
                return False
            #edge case: if course has no prereqs
            if preMap[crs] == []:
                return True
            
            #append the course to visited
            visited.add(crs)
            #dfs through the prereqs of the course
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            #remove the course once it's visited
            visited.remove(crs)
            #set the course to empty list if dfs runs on it again
            preMap[crs] = []
            return True
        #call dfs on all the courses in the graph
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        


        