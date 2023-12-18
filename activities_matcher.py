import sqlite3

def act_matcher():
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()

    cursor.execute('''SELECT UNIVERSITY_NAME, ACTIVITIES FROM University''')
                                       
    result = cursor.fetchall()
    
    result_list = []
    
    for item in result:
        result_list.append((item[0], float(act_counter(item[1])/4)))
    
    return result_list
        
def act_counter(string):
    return len(list(string.split(", ")))
    
