from collections import defaultdict

class CourseScheduler:
    def __init__(self):
        self.graph = defaultdict(list)
        self.completed = set()

    def add_prerequisite(self, course, prerequisite):
        self.graph[course].append(prerequisite)

    def topological_sort(self):
        stack = []
        visited = set()

        def dfs(course):
            if course in visited:
                return
            visited.add(course)
            for prereq in self.graph[course]:
                dfs(prereq)
            stack.append(course)

        graph_copy = self.graph.copy()  # Make a copy of the graph
        for course in graph_copy:        # Iterate over the copy
            dfs(course)

        return stack[::-1]

    def resolve_dependencies(self):
        completion_order = self.topological_sort()

        # Check for circular dependencies
        if len(completion_order) != len(self.graph):
            print("Circular dependencies detected. Cannot resolve dependencies.")
            return

        optimized_order = []
        for course in completion_order:
            if all(prereq in self.completed for prereq in self.graph[course]):
                optimized_order.append(course)
                self.completed.add(course)

        return optimized_order

# Example usage
if __name__ == "__main__":
    scheduler = CourseScheduler()
    scheduler.add_prerequisite("Data Structures", "Algorithms")
    scheduler.add_prerequisite("Algorithms", "Mathematics")
    scheduler.add_prerequisite("Database Management", "Algorithms")
    scheduler.add_prerequisite("Mathematics", "Linear Algebra")
    scheduler.add_prerequisite("Linear Algebra", "Calculus")

    print("Original Dependencies:")
    for course, prereqs in scheduler.graph.items():
        print(f"{course}: {prereqs}")

    print("\nOptimized Course Completion Order:")
    completion_order = scheduler.resolve_dependencies()
    if completion_order:
        for i, course in enumerate(completion_order, 1):
            print(f"{i}. {course}")
    else:
        print("Failed to resolve dependencies due to circular dependencies.")
