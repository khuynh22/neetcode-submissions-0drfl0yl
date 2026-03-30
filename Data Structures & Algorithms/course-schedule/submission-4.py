class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return True
        if not prerequisites:
            return True
        course_track = defaultdict(list)
        for preq in prerequisites:
            with_preq, no_preq = preq[0], preq[1]
            course_track[no_preq].append(with_preq)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if course_track[course] == []:
                return True
            
            visit.add(course)
            for pre in course_track[course]:
                if not dfs(pre):
                    return False
            
            visit.remove(course)
            course_track[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True