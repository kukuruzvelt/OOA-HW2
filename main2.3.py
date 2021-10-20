class Group:
    """ Class for working with a group. """
    __max_size_of_group = 20

    def __init__(self, students):
        """ Checks arguments against values and initializes class variables. """
        if (isinstance(students, list) and len(students) < Group.__max_size_of_group
                and all(isinstance(x, Student) for x in students) and all(students.count(x) == 1 for x in students)):
            self.__students = students
        else:
            raise TypeError("wrong arguments")

    def __count_average_score(self, student):
        """ Counts and returns an average score. """
        average_score = 0.0
        for mark in student.get_grades():
            average_score += mark
        return average_score / len(student.get_grades())

    def return_top_five(self):
        """ Returns top 5 students by average score. """
        group = dict()
        result = list()
        for student in self.__students:
            group[student] = self.__count_average_score(student)
        sorted_keys = sorted(group, key=group.get)
        for i in range(1, 6):
            result.append(sorted_keys[len(sorted_keys) - i])
        return result


class Student:
    """ Class for working with a student. """

    def __init__(self, name, surname, record_book_number, grades):
        """ Checks arguments against values and initializes class variables. """
        if (isinstance(name, str) and isinstance(surname, str)
                and isinstance(record_book_number, int) and isinstance(grades, list)):
            self.__name = name
            self.__surname = surname
            self.__record_book_number = record_book_number
            self.__grades = grades
        else:
            raise TypeError("wrong arguments")

    def __str__(self):
        return self.__name + " " + self.__surname

    def get_grades(self):
        """ Returns grades. """
        return self.__grades


try:
    s1 = Student("1", "a", 1, [1])
    s2 = Student("2", "b", 2, [2])
    s3 = Student("3", "c", 3, [3])
    s4 = Student("4", "d", 3, [4])
    s5 = Student("5", "e", 3, [5])
    s6 = Student("6", "f", 3, [6])
    s7 = Student("7", "g", 3, [7])
    s8 = Student("8", "h", 3, [8])
    s9 = Student("9", "i", 3, [9])
    g = Group([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    g = g.return_top_five()
    for i in g:
        print(i)
except TypeError as e:
    print(e)
