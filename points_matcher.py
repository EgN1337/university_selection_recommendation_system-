import sqlite3


def points_matcher(points, additional_points):
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()

    cursor.execute('''SELECT UNIVERSITY_NAME, UNIVERSITY_FACULTY, FACULTY_MINIMAL_POINTS FROM University 
                                       INNER JOIN Faculties ON (University.ID = Faculties.UNIVERSITY)''')
                                       
    result = cursor.fetchall()

    maximum_points = 310
    
    result_list = []
    
    user_points = int(points) + int(additional_points)
    
    for item in result:
        university_points = float(item[2])
        
        if user_points < university_points:
            result_list.append((item[0], item[1], 0))
        else:
            result_list.append((item[0], item[1], float((user_points - university_points)/(maximum_points-university_points))))
    return result_list