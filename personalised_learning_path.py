class User:
    def __init__(self, user_id, interests, past_courses, performance):
        self.user_id = user_id
        self.interests = interests
        self.past_courses = past_courses
        self.performance = performance

class Course:
    def __init__(self, course_id, title, prerequisites, difficulty):
        self.course_id = course_id
        self.title = title
        self.prerequisites = prerequisites
        self.difficulty = difficulty

class LearningPlatform:
    def __init__(self, courses):
        self.courses = courses
    
    def generate_personalized_learning_path(self, user):
        recommended_courses = []
        for course in self.courses:
            # Check if the user has already completed this course or it's in progress
            if course.course_id not in user.past_courses:
                # Check if the user's interests match the course topic
                if any(topic in course.title.lower() for topic in user.interests):
                    # Check if the user meets the prerequisites for this course
                    if all(prereq in user.past_courses for prereq in course.prerequisites):
                        recommended_courses.append(course)
        return recommended_courses

# Sample data
courses = [
    Course(1, "Introduction to Python Programming", [], "Beginner"),
    Course(2, "Data Structures and Algorithms in Python", [1], "Intermediate"),
    Course(3, "Machine Learning Fundamentals", [1, 2], "Advanced"),
    Course(4, "Web Development with Django", [1], "Intermediate"),
    Course(5, "Natural Language Processing", [3], "Advanced")
]

user1 = User(1, ["python", "machine learning"], [1, 2], {"Introduction to Python Programming": 90, "Data Structures and Algorithms in Python": 85})


platform = LearningPlatform(courses)

# Generate personalized learning paths for users
user1_learning_path = platform.generate_personalized_learning_path(user1)

# Display recommended courses for each user
print("User 1 Recommended Courses:")
for course in user1_learning_path:
    print(course.title)
