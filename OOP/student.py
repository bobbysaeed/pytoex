import random


class Student:
    educational_platform = "youtube PersianPython"

    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [
            f"salam, man {self.name} hastam va dore Object Oriented ra tamasha kardam",
            f"chetori man {self.name} hastam va {self.age} sal sen daram",
        ]

        greeting = random.choice(greetings)

        return greeting


def instance_creation(student_names):
    return [Student(name) for name in student_names]


if __name__ == "__main__":
    names = ["Narges", "Sara", "Hassan", "Nima"]

    for student in instance_creation(names):
        print(student.greet())
