class Person:
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다")


person_1 = Person("유재석")
person_1.talk()
person_2 = Person("박명수")
person_2.talk()