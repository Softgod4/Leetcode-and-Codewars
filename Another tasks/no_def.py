# Создайте класс "Студент", который будет представлять информацию о студентах в университете. 
# Класс должен иметь следующие атрибуты: имя, возраст, курс, средний балл. 
# Также класс должен иметь методы для 
# установки и получения значений атрибутов.

class Students():
    def __init__(self, name, age, course, balls):
        self.set_name = lambda name_arg: setattr(self, 'name', name_arg)
        self.set_age = lambda age_arg: setattr(self, 'age', age_arg)
        self.set_course = lambda course_arg: setattr(self, 'course', course_arg)
        self.set_balls = lambda grade_arg: setattr(self, 'balls', balls_arg)

        self.get_name = lambda: self.name
        self.get_age = lambda: self.age
        self.get_course = lambda: self.course
        self.get_balls = lambda: self.set_balls

        self.set_name(name)
        self.set_age(age)
        self.set_course(course)
        self.set_balls(balls)