class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map and fill them with the the key num of courses value empty list
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        print(preMap)
        # create a set to see which one already got visited
        visited = set()

        def dfs(course):
            # if the course we visit is already in visited loop is detected
            
            if course in visited:
                return False
            # if the prerequisite is empty return true
            if preMap[course] == []:
                return True

            # add courses to set
            visited.add(course)
            # print(visited)

            # loop over the prerequisites in the map
            for pre in preMap[course]:
                # print(preMap[course])
                if not dfs(pre): return False
            visited.remove(course)
            # set the course to [] if it passed 
            # so if it runs next it will 
            # not do the whole loop again 
            preMap[course] = []
            return True

        # loop over all the courses and run dfs
        for c in range(numCourses):
            if not dfs(c): return False
        return True