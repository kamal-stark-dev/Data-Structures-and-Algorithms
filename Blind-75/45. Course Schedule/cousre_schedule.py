from collections import deque

class Solution:
    """
    Problem:
        You are given `numCourses` courses and prerequisite pairs where
        [course, prerequisite] means the prerequisite course must be
        completed before the course.

        Return True if it is possible to finish all courses, otherwise False.

    Approach:
        1. Model the courses and prerequisites as a directed graph.
        2. A cycle in the graph means there is a circular dependency,
           making it impossible to finish all courses.
        3. Detect cycles using either DFS or Topological Sort.

    Constraints:
        - 1 <= numCourses <= 2000
        - 0 <= prerequisites.length <= 5000
        - Each prerequisite pair contains exactly two courses.
        - All course numbers are in the range [0, numCourses - 1].
        - All prerequisite pairs are unique.

    Notes:
        - [a, b] represents a directed dependency: b -> a.
        - The problem can be reduced to detecting whether the directed
          graph contains a cycle.
    """

    def course_schedule_dfs(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Intuition:
            A course can be completed only after all of its prerequisites
            have been completed.

            If while exploring the prerequisites of a course we encounter
            that same course again before finishing its DFS traversal, we
            have found a cycle.

            A cycle represents a circular dependency. For example:

                Course 0 -> Course 1 -> Course 0

            Course 0 requires Course 1, while Course 1 requires Course 0,
            so neither course can be completed first.

            We therefore use a `visited` set to keep track of courses that
            are currently being explored.

        Algorithm:
            1. Build an adjacency list where:
                   courses[course] = list of prerequisites for that course.

            2. For every course, perform DFS:
                - If the course has no prerequisites, it can be completed.
                - If the course is already in `visited`, we found a cycle.
                - Add the current course to `visited`.
                - Recursively explore all its prerequisites.
                - Remove the course from `visited` after all its
                  prerequisites have been successfully explored.

            3. Once a course and all of its prerequisites have been
               successfully processed, set `courses[course] = []`.
               This acts as memoization and prevents processing the same
               dependency chain again.

            4. If any DFS detects a cycle, return False.

            5. If every course can be processed without finding a cycle,
               return True.

        Time:
            O(V + E)

            V = number of courses
            E = number of prerequisite relationships

            Every course and prerequisite relationship is processed
            a constant number of times. The memoization optimization
            prevents repeated traversal of already-processed courses.

        Space:
            O(V + E)

            - O(V + E) for the adjacency list.
            - O(V) for the visited set.
            - O(V) maximum recursion depth in the worst case.
        """

        def dfs(course: int) -> bool:
            if not courses[course]: # no prerequisites
                return True

            if course in visited: # cycle detected
                return False

            visited.add(course)

            for prereq in courses[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)

            # optimization
            courses[course] = []

            return True

        courses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        visited = set()

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

    def course_schedule_topological_sort(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Intuition:
            We can also solve the problem using Topological Sort.

            In a valid course schedule, a course can be taken only when
            all of its prerequisites have already been completed.

            Therefore, we start with courses having zero prerequisites
            (indegree = 0). These courses can be completed immediately.

            After completing a course, we remove its outgoing dependency
            edges. This may cause other courses to have indegree 0, meaning
            they are now ready to be completed.

            If we are able to process all courses, there is no cycle.
            If some courses remain unprocessed, they must be part of a
            cycle or depend on a cycle.

        Algorithm:
            1. Build a directed graph using an adjacency list.

               For prerequisite [course, prereq], create:

                   prereq -> course

               because `prereq` must be completed before `course`.

            2. Calculate the indegree of every course.
               `indegree[course]` represents the number of prerequisites
               that course still has.

            3. Add every course with indegree 0 to a queue.
               These courses have no remaining prerequisites and can be
               taken immediately.

            4. While the queue is not empty:
                - Remove a course from the queue.
                - Count it as completed.
                - Visit all courses that depend on it.
                - Decrease their indegree because one prerequisite
                  has now been completed.
                - If a course's indegree becomes 0, add it to the queue.

            5. At the end:
                - If `visited_courses == numCourses`, all courses can be
                  completed, so return True.
                - Otherwise, some courses could not be processed because
                  of a cycle, so return False.

        Time:
            O(V + E)

            V = number of courses
            E = number of prerequisite relationships

            Each course is added to and removed from the queue at most once,
            and each prerequisite edge is processed once.

        Space:
            O(V + E)

            - O(V + E) for the adjacency list.
            - O(V) for the indegree array.
            - O(V) for the queue in the worst case.
        """

        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            # setting node from prereq to course
            # (representing we need to complete prereq first)
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        visited_courses = 0
        while queue:
            course = queue.popleft()
            visited_courses += 1

            for neighbor in adj[course]:
                # remove connection from prereq to course
                # (representing prereq has been done)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_courses == numCourses

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # (numCourses: int, prerequisites: list[list[int]], expected bool)
        (
            2,
            [[1, 0]],
            True
        ),
        (
            2,
            [[1, 0], [0, 1]],
            False
        ),
        (
            6,
            [[1, 0], [1, 2], [2, 3], [2, 4], [2, 5], [3, 1], [4, 5]],
            False
        ),
    ]

    for numCourses, prerequisites, expected in test_cases:
        result = solution.course_schedule_topological_sort(numCourses, prerequisites)

        assert result == expected, (
            f"\n\nTest case failed!\n"
            f"numCourses = {numCourses}\n"
            f"prerequisites = {prerequisites}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

        print(
            f"numCourses = {numCourses}\n"
            f"prerequisites = {prerequisites}\n"
            f"expected = {expected}\n"
            f"got = {result}\n"
        )

    print("#######################")
    print("All test cases passed!!")
    print("#######################")