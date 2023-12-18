import sqlite3

connection = sqlite3.connect("studentDataBase.db")

cursor = connection.cursor()

cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("rsreu",1,"sports, art, science, foreign languages", "Ryazan")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("rsu",0,"sports, art, teaching, foreign languages", "Ryazan")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("rgatu",1,"sports, handworking", "Ryazan")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("msu",0,"science, jurisprudense, foreign languages", "Moscow")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("mifi",1,"physics", "Moscow")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("mgtu",0,"sports, art, science, foreign languages", "Moscow")
''')
cursor.execute('''
    INSERT INTO University (UNIVERSITY_NAME, ROOM_AVAILABILITY, ACTIVITIES, UNIVERSITY_CITY) VALUES ("spbgu",0,"sports, art, science, foreign languages", "Saint-Petersburg")
''')

cursor.execute('''
    SELECT * FROM University
''')

connection.commit()

result = cursor.fetchall()

for item in result:
    print(str(item))