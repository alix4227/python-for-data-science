from dataclasses import dataclass


@dataclass
class Student:
    grade: int
    name: str
    firstname: str
    classe: str

def main():
    student1 = Student(16, "CRUSOE", "Alix", '5B')
    student2 = Student(20, "CRUSOE", "Al", '5B')
    liste = [student2, student1]
    liste_final = sorted(liste, key=lambda student: (student.grade))
    print(liste_final)

if __name__ == '__main__':
    main()