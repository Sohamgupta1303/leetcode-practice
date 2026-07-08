class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for prereq in prerequisites:
            course, pre = prereq[0], prereq[1]
            adj[course].append(pre)
        
        # for each of the courses, we need to make sure 
        # that each of its prerequisites are completable. 
        # we go through numCourses and for each course, we look at 
        # the adjacency list. If its empty, we can take this course
        # if it isnt empty, we recursively call helper on that course to 
        # make sure that we can take it. when we call helper() on a course, 
        # we first need to make sure that we havent already seen that course
        # ie: we arent in a cycle. 

        def helper(course: int, visited: Set[int]) -> bool:
            if course in visited:
                return False
            if not adj[course]:
                return True

            visited.add(course)
            prereqs = adj[course]
            while prereqs:
                prereq = prereqs[-1]
                if not helper(prereq, visited):
                    return False
                prereqs.remove(prereq)
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not helper(course, set()): return False

        return True



       

        





        


            

        