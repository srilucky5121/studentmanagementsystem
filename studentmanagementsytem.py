class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def enroll(self, course):
        self.courses[course.name] = course

    def assign_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name].grades[self.name] = grade
        else:
            print("Course not found.")

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0

        for course in self.courses.values():
            if self.name in course.grades:
                grade = course.grades[self.name]
                credits = course.credits
                total_credits += credits
                total_grade_points += grade * credits

        if total_credits == 0:
            return 0

        return total_grade_points / total_credits


class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.grades = {}


# Example usage
student1 = Student("Srilakshmi")
student2 = Student("varshini")

course1 = Course("Math", 3)
course2 = Course("English", 4)

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course2)

student1.assign_grade("Math", 85)
student1.assign_grade("English", 90)
student2.assign_grade("English", 95)

print(student1.calculate_gpa())  # Output: 87.5
print(student2.calculate_gpa())  # Output: 95.0
