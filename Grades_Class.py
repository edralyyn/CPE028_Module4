class Grades_Class:
    def __init__(self, Course_Code, Course_Units, Course_Grade):
        self.Course_Code = Course_Code
        self.Course_Units = Course_Units
        self.Course_Grade = Course_Grade
    def __str__(self):
        return f"{self.Course_Code}({self.Course_Units})"