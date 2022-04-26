class Student:
    def __eq__(self, s):
        return (self.name == s.name) and (self.age == s.age)

s1 = Student()
s2 = Student()
print(s1 == s2)