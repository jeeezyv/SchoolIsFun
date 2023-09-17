# This module contains the People class, which is used to create a list of people and the different types of people in our system
# Create a class called Person which is the base class from which other classes will inherit
class Person:

    # Creating the properties of the Person class
    id = 0
    first_name = ""
    last_name = ""
    
    # A person has an ID, first name and last name 
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    # The id property is a unique identifier for each person
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        # Check if the id is a positive integer, if not raise an exception
        if id < 0:
            raise ValueError("ID must be a positive integer")
        self.id = id

    # The string representation of a person is their first name and last name
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# Create a person called Susan Jones with ID 2
new_person = Person(2, "Susan", "Jones")
# Print out Susan's details:
#  Print the Susan's ID
print("Susan's ID: ", new_person.id)
#  Print the Susan's first name
print("First Name:", new_person.first_name)
#  Print the Susan's last name
print("Last Name:", new_person.last_name)

# Change the person's last name to Smith-Jones
new_person.last_name = "Smith-Jones"


# Print out the person's details again
print("Susan's Id: ", new_person.id)
print("First Name: ", new_person.first_name)
print("Last Name: ", new_person.last_name)


# Create a class called course
# A course is a class that a student can take and an instructor can teach
class Course:
    course_number = 0
    couse_name = ""
    description = ""
    department = ""
    credits = 0

    # A course has a course ID, course name, description, department and credits
    def __init__(self, course_number, course_name, description, department, credits):
        self.course_number = course_number
        self.course_name = course_name
        self.description = description
        self.department = department
        self.credits = credits

    # The course number is a unique identifier for each course which must be greater than 0
    def set_course_number(self, course_number):
        if course_number < 0:
            raise ValueError("Course number must be a positive integer")
        self.course_number = course_number
    
    # The course ID is a combination of the department and course number
    # It can't be set directly, but can be retrieved
    def course_id(self):
        return f'{self.department}{self.course_number}'
    
    # The string representation of a course is the ID and the course name
    def __str__(self):
        return f'{self.course_id()} {self.course_name}'

# Create a class called Instructor which inherits from the Person class
# An instructor is a person who teaches one or more courses
class Instructor(Person):
    courses_teaching = []

    # An instructor has an ID, first name, last name, and first year teaching
    def __init__(self, id, first_name, last_name, first_year_teaching):
        # Initialize the Person class
        super().__init__(id, first_name, last_name)
        self.first_year_teaching = first_year_teaching

    # An instructor can teach a course
    def add_course(self, course):
        self.courses_teaching.append(course)

    # An instructor can stop teaching a course
    def remove_course(self, course):
        self.courses_teaching.remove(course)

    # An instructor can get a list of courses they are teaching
    def get_courses(self):
        return self.courses_teaching
    
   
    
isys_1234 = Course(1234, "Introduction to Programming", "This course introduces students to programming", "ISYS", 3)
isys_5713 = Course(course_number=5713, 
                   course_name="Advanced Programming", 
                   description="This course introduces students to advanced programming", 
                   department="ISYS",
                   credits= 3)
print(isys_1234)
print(isys_5713)

# Create an instructor called Alex Abbott , he started teaching in 2015 and teaches ISYS1234

Alex_Abbot = Instructor(1,"Alex","Abbot",2015)

Alex_Abbot.add_course(isys_1234)

# Alex_Abbot.courses_teaching.append(isys_1234)

# Print out the instructor's details
print("PRofessor Abbot's ID: ", Alex_Abbot.id)
print("First Name: ",Alex_Abbot.first_name)
print("Last Name: ",Alex_Abbot.last_name)
print("First Year Teaching: ",Alex_Abbot.first_year_teaching)

# Print out the courses the instructor is teaching

courses = Alex_Abbot.get_courses()
for c in courses:
    print(c)




# Add a new course for the instructor to teach (ISYS5713)

Alex_Abbot.add_course(isys_5713)

# Print out the courses the instructor is teaching
courses = Alex_Abbot.get_courses()
for c in courses:
    print(c)

# Remove a course for the instructor to teach

Alex_Abbot.remove_course(isys_1234)

# Print out the courses the instructor is teaching

courses = Alex_Abbot.get_courses()
for c in courses:
    print(c)

# Step 3 
# Create a student class. It should be a subclass of Person, but also have a list of courses they are currently taking and a current grade point average (int)

class Student(Person):
    enrolled_courses = {}

    # grade_point_avg = sum(self.enrolled_courses.values())/len(self.enrolled_courses)

    def __init__(self, id, first_name, last_name, grade_point_avg):
        # Initialize the Person class
        super().__init__(id, first_name, last_name)
        self.grade_point_avg = grade_point_avg

    
    
    # def add_student_course(self):
    #    self.enrolled_courses.update()
    

    def add_student_course_2(self, key, value):
        self.enrolled_courses[key] = value
    
    def grade_point_avg_calc(self):
        x = 0
        l = 0
        for key, values in self.enrolled_courses.items():
            if values  == 'N/A':
                pass
            else: 
                 x = x + values
                 l = l +1
                 return (x/l)
        
    def remove_course(self, value):
        del self.enrolled_courses[value]

    def update_GPA(self):
        self.grade_point_avg = sum(self.enrolled_courses.values())/len(self.enrolled_courses)

    def update_GPA_2(self): 
        x = 0
        l = 0
        for key, values in self.enrolled_courses.items():
            if values  == 'N/A':
                pass
            else: 
                 x = x + values
                 l = l +1
        self.grade_point_avg=(x/l)

    
            
        
# Create a student object for a student called Susan Smartinez, you can choose her GPA and which courses she is taking

Susan_Smartinez = Student(1995, 'Susan', 'Smartinez', grade_point_avg= 0 )

Susan_Smartinez.add_student_course_2("isys_1234_Fall_2023", 4.0)
Susan_Smartinez.add_student_course_2("isys_5713_Fall 2023", 4.0)

# Add a course, remove a course, and update her GPA. Show the results of each step along the way

#add course

Susan_Smartinez.add_student_course_2("ACCT_5859_Fall_2023", "N/A")

# print courses

print("Susan's Courses:", list(Susan_Smartinez.enrolled_courses))

# remove a course

Susan_Smartinez.remove_course("isys_1234_Fall_2023")


# Print Susan's courses
print("Susan's Courses Updated:", list(Susan_Smartinez.enrolled_courses))


# Calculate Susan's GPA

print("Calculating Susan's GPA:", Susan_Smartinez.grade_point_avg_calc())

# update Susan's GPA

Susan_Smartinez.update_GPA_2()

# Print her GPA
print("Susan's Updated GPA:", Susan_Smartinez.grade_point_avg)





# print(sum(Susan_Smartinez.enrolled_courses.values())/len(Susan_Smartinez.enrolled_courses))



    


