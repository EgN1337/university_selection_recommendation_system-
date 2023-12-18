import sqlite3

connection = sqlite3.connect("studentDataBase.db")

cursor = connection.cursor()

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (1, "Computer Science Faculty", 240, "Математика, Физика, Русский, Информатика")
               ''')
              
cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (1, "Faculty of Automation and Information Technology in Management", 210, "Математика, Физика, Русский")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (1, "Faculty of Engineering and Economics", 230, "Математика, Обществознание, Русский")
               ''')


cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (6, "Computer Science Faculty", 240, "Математика, Физика, Русский, Информатика")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (6, "Computer Science and Management systems", 220, "Математика, Физика, Русский")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (6, "Engineering business and Management", 230, "Математика, Обществознание, Русский")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (7, "Computer Science Faculty", 230, "Математика, Физика, Русский, Информатика")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (7, "Faculty of Medicine", 240, "Русский, Химия, Биология")
               ''')

cursor.execute('''
                   INSERT INTO Faculties (UNIVERSITY, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS, SUBJECTS) 
                   VALUES (7, "Faculty of Psychology", 200, "Русский, Обществознание, Математика")
               ''')


connection.commit()











