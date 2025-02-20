
class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
    def add_grade(self, grade):
        self.grades.append(grade)
    def average(self):
        return sum(self.grades) / len(self.grades)


    def show(self):
        print(f"Name is: {self.name}, Surname is {self.surname},  average marks is {Student.average(self)} ")


obj1 = Student("Maks", "Shevchyk", [11,8,9])
obj1.show()
obj2 = Student("Abd", "asdasd", [11,10,11])
obj2.show()
obj3 = Student("Abidas", "asdas", [8,9,7])
obj3.show()
# студента з оцінкою вище 4 не виведу бо не получаєьбся і не знаю як
"________________Task2___________________________________"
class Store:
    def __init__(self,name, addres):
        self.name = name
        self.addres = addres
    def show(self):
        print(f"Store name is {self.name}, addres of shop is {self.addres}")
class Shop1(Store):
    def __init__(self, name, addres, product):
        super().__init__(name, addres)
        self.product = product
    def show(self):
        print(f"Store name is {self.name}, addres of shop is {self.addres}, count of products {self.product}")
class Shop2(Store):
    def __init__(self, name, addres,product, el_product):
        super().__init__(name, addres)
        self.el_product = el_product
        self.product = product
    def show(self):
        print(f"Store name is {self.name}, addres of shop is {self.addres}, count of products {self.product}, el_products {self.el_product}")
obj1 = Shop1("WV", "German", "1,000,000")
obj1.show()
obj2 = Shop2("BMW", "German", "100,000", "10,000")
obj2.show()
"-----------Task3 Nevmiu pracuvati s failami"
"---------Task4"
mark_list = [2, 3, 4, 5, 5]
for mark in mark_list:
    if mark >= 4:
        print(f"Студент з оцінкою {mark} - здав предмет.")

"--------------Task5"
investments = [
    "Rolls Royce - 1300",
    "Audi - 150",
    "Microsoft - 20",
    "BMW - 215"
]
company_name = "BMW"
print(f"Інвестиції у {company_name}:")
for investment in investments:
    if company_name in investment:
        print(investment)
