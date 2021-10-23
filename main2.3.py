class Group:
    """ Class for working with a group. """
    __max_size_of_group = 20

    def __init__(self, students):
        """ Initializes variables. """
        self.students=students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        """ Sets students. """
        if not isinstance(students, list):
            raise TypeError("argument is not a list")
        if not len(students) < Group.__max_size_of_group:
            raise ValueError("too many students")
        if not all(isinstance(x, Student) for x in students):
            raise TypeError("not only students in list")
        if not all(self.__check(x, students) == 1 for x in students):
            raise ValueError("some students has same record book number")
        self.__students = students

    def addStudent(self, student):
        """ Adds students. """
        if not isinstance(student, Student):
            raise TypeError("argument is not a Student")
        if not self.__check(student, self.__students) == 0:
            raise ValueError("this student is already in the group")
        if len(self.__students) == 20:
            raise ValueError("the group is already complete")
        self.__students.append(student)

    def __check(self, student, students):
        """ Checks if student is already in list. """
        num = 0
        for s in students:
            if s.record_book_number == student.record_book_number:
                num += 1
        return num

    def __count_average_score(self, student):
        """ Counts and returns an average score. """
        average_score = 0.0
        for mark in student.grades:
            average_score += mark
        return average_score / len(student.grades)

    def return_top_five(self):
        """ Returns top 5 students by average score. """
        self.__students.sort(key=lambda student: student.grades, reverse=True)
        return self.__students[:5]


class Student:
    """ Class for working with a student. """

    def __init__(self, name, surname, record_book_number, grades):
        """ Initializes variables. """
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book_number(self):
        """ Returns name. """
        return self.__record_book_number

    @property
    def grades(self):
        """ Returns grades. """
        return self.__grades

    @name.setter
    def name(self, name):
        """ Sets name. """
        if not isinstance(name, str):
            raise TypeError("argument is not a string")
        if not name:
            raise ValueError("name is empty")
        self.__name = name

    @surname.setter
    def surname(self, surname):
        """ Sets surname. """
        if not isinstance(surname, str):
            raise TypeError("argument is not a string")
        if not surname:
            raise ValueError("surname is empty")
        self.__surname = surname

    @record_book_number.setter
    def record_book_number(self, record_book_number):
        """ Sets record book number. """
        if not isinstance(record_book_number, int):
            raise TypeError("argument is not an int")
        self.__record_book_number = record_book_number

    @grades.setter
    def grades(self, grades):
        """ Sets grades. """
        if not isinstance(grades, list):
            raise TypeError("argument is not a list")
        if not all(isinstance(x, int) for x in grades):
            raise TypeError("not only ints in list")
        if not all(0 < x < 100 for x in grades):
            raise ValueError("wrong grade")
        self.__grades = grades

    def addGrade(self, grade):
        """ Adds a grade. """
        if not isinstance(grade, int):
            raise TypeError("argument is not an int")
        if not 0 < grade < 100:
            raise ValueError("wrong grade")
        self.__grades.append(grade)

    def __str__(self):
        return self.__name + " " + self.__surname


try:
    st1 = Student("1", "a", 1, [1])
    st2 = Student("2", "b", 2, [2])
    st3 = Student("3", "c", 3, [3])
    st4 = Student("4", "d", 4, [4])
    st5 = Student("5", "e", 5, [5])
    st6 = Student("6", "f", 6, [6])
    st7 = Student("7", "g", 7, [7])
    st8 = Student("8", "h", 8, [8])
    st9 = Student("9", "i", 9, [9])
    gr = Group([st1, st2, st3, st4, st5, st6, st7, st8, st9])
    gr = gr.return_top_five()
    for i in gr:
        print(i)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
