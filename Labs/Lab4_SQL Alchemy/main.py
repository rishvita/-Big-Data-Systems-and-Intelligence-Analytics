# coding=utf-8

from student import Student
from base import Session, engine, Base

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()

st1 = Student(2, 'Rishvita Reddy', 25, 'Boston MA', 'rr@example.com')
st2 = Student(3, 'Kanika Negi', 25, '678 West Ave, Boston MA', 'kn@example.com')


session.add(st1)
session.add(st2)
session.commit()
session.close()
