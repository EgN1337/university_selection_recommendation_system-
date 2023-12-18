# https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
import sqlite3
import math

# Creating database for saving models' properties and rules
connection = sqlite3.connect("studentDataBase.db")

cursor = connection.cursor()

# Data base creation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rules(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        RULE_DESCRIPTION TEXT NOT NULL
    )
''')
connection.commit()

'''=------------------------------------------------------------------------------------------='''

# University table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS University(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UNIVERSITY_NAME TEXT NOT NULL,
        ROOM_AVAILABILITY BOOLEAN NOT NULL CHECK (ROOM_AVAILABILITY IN (0, 1)),
        ACTIVITIES TEXT,
        UNIVERSITY_CITY TEXT NOT NULL 
    )
''')
connection.commit()

'''=------------------------------------------------------------------------------------------='''

#
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Faculties(
        FACULTIES_SET_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UNIVERSITY INT NOT NULL,
        UNIVERSITY_FACULTY TEXT NOT NULL,
        FACULTY_MINIMAL_POINTS INTEGER NOT NULL,
        SUBJECTS TEXT NOT NULL,
        FOREIGN KEY (UNIVERSITY) REFERENCES University (ID)
    )
''')
connection.commit()
connection.close()

'''=------------------------------------------------------------------------------------------='''


# User class
class User:
    def __init__(self, id, name, points, additional_points, room_wish, faculty, city):
        self.id = id
        self.name = name
        self.points = points
        self.additional_points = additional_points
        self.room_wish = room_wish
        self.faculty = faculty
        self.city = city

    def all_points(self):
        return int(self.points) + int(self.additional_points)

    def user_info(self):
        return self.name + self.city


'''=------------------------------------------------------------------------------------------='''


# University class
class University:
    def __init__(self, id, name, room_availibility, faculties, activities, city):
        self.id = id
        self.name = name
        self.room_availibility = room_availibility
        self.faculties = faculties
        self.activities = activities
        self.city = city

    def university_common_info(self):
        result_1 = "University name: " + str(self.name) + "\n"
        result_2 = "In which city we are locating: " + str(self.city) + "\n"
        result_3 = "Our faculties: " + str(self.faculties) + "\n"
        if (self.room_availibility == True):
            result_4 = "We can offer you any place in our beautiful residence!"
        else:
            result_4 = "But we can't still offer you any place in our beautiful residence :( Cause we do not have this opportunity"
        result = result_1 + result_2 + result_3 + result_4
        return result


'''=------------------------------------------------------------------------------------------='''

# For test.py
name = ""
subjects = ""
points = ""
additional_points = ""
city = ""
new_city = ""
residence = ""
label = False

def print_current_result():
    if residence == 'Да':
        result_residence = "Есть необходимость в предоставлении общежития"
    else:
        result_residence = "Нет необходимости в предоставлении общежития"
    print( f"Информация о Вас: \n"
           f"Ваше имя: {name}; \n"
           f"Город проживания: {city}; \n"
           f"Готовность к переезду в другой город: {new_city}; \n"
           f"Предметы, которые Вы сдавали: {subjects}; \n"
           f"Количество баллов за предметы: {points}; \n"
           f"Дополнительные баллы: {additional_points}; \n"
           f"Общее количество баллов: {str(int(points) + int(additional_points))}; \n"
           f"{result_residence}. \n")


'''=------------------------------------------------------------------------------------------='''

from geopy.geocoders import Nominatim




def location_finder(address):
    geolocator = Nominatim(user_agent="main")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return (latitude, longitude)

from geopy.distance import geodesic 

def distance_finder(user_address, university_address):
    result = geodesic(user_address, university_address).km
    return result

min_distance = []
def minimum_distance_between_city():
    
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()
    cursor.execute('''SELECT UNIVERSITY_NAME, UNIVERSITY_CITY FROM University''')
    query_result = cursor.fetchall()
    connection.close()
    
    for item in query_result:
        current_distance = distance_finder(location_finder(city), location_finder(item[1]))
        current_values_list = (current_distance, item[0])
        min_distance.append(current_values_list)
    min_distance.sort()
    for item2 in min_distance:
        print(item2)
            
def nearest_city_to_live_finder():
    result_list = []
    if (new_city == "Да" or new_city == "Конечно"):
        
        minimum = float(min_distance[0][0])
        maximum = float(min_distance[len(min_distance)-1][0])
        #print(minimum)
        for item in min_distance:
            #print(item[0])
            if minimum < item[0]:
                current = item[0]
                break
        for item in min_distance:
            if item[0] == minimum:
                result_list.append((item[1],0))
            elif item[0] == current:
                result_list.append((item[1],1))
            else:
                result_list.append((item[1],float(abs(current - item[0])/(abs(maximum-minimum)))))
    else:
        minimum = float(min_distance[0][0])
        maximum = float(min_distance[len(min_distance)-1][0])
        average = maximum - minimum
        for item in min_distance:
            result_list.append((item[1], 1 - float(item[0])/average))
    return result_list
                


'''=------------------------------------------------------------------------------------------='''

#def for all rules printing
def rules_printer():
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()
    
    cursor.execute('''
                       SELECT * FROM Rules;
                   ''')
                   
    result = cursor.fetchall()
    
    string = ""
    
    for item in result:
        string += str(item) + "\n"
    
    return string


'''=------------------------------------------------------------------------------------------='''

#rule_adder
def rule_adder(string):
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()
    
    cursor.execute(f"INSERT INTO RULES (RULE_DESCRIPTION) VALUES ('{str(string)}')")
    connection.commit()


'''=------------------------------------------------------------------------------------------='''

#rule deleter
def rule_deleter(string):
    connection = sqlite3.connect("studentDataBase.db")

    cursor = connection.cursor()
    
    cursor.execute(f"DELETE FROM Rules WHERE ID = {int(string)}")
    connection.commit()


