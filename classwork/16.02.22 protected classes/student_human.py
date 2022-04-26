class Human:
    def init(self,age,name,country):
        self.age = age
        self.name = name
        self.country = country
    
    def say(self):
        print(f'{self.age}  {self.name} {self.country}')

class Student(Human):
    def init(self, age, name, country,study):
        super().init(age, name, country)
        self.study = study

    def say(self):
        super().say()
        print(f'{self.study}')