from base import Session
from student import Student

session = Session()

def get_all_data():
    print('Getting All Data')

    students = session.query(Student).all()
    for student in students:
        print(student.id)
        print(student.name)
        print(student.age)
        print(student.address)


def update_record():
    session.query(Student) \
        .filter(Student.id == 3) \
        .update({Student.name: 'Nidhi Goyal', Student.address: 'Jersey City, NJ', Student.email: 'ng@example.com'})

    session.commit()

get_all_data()
#update_record()
