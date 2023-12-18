import sqlite3

def subjects_matcher(list1):
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()

    cursor.execute('''SELECT UNIVERSITY_NAME, UNIVERSITY_FACULTY, SUBJECTS FROM University 
                                   INNER JOIN Faculties ON (University.ID = Faculties.UNIVERSITY)''')
                                  
    result = cursor.fetchall()
    
    result_list = []
    current_list = list(list1.split(", "))
    
    for item in result:
        num = 0
        for item2 in current_list:
            if item2 in item[2]:
                num += 1
        koef = num / 3
        current_values = (item[0], item[2], koef)
        result_list.append(current_values)
    return result_list
