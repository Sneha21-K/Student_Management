
#steps to connect pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://DataGeniuses:datageniunes@cluster0.8ayuvn1.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#getting the database name and setting collections
db=client.get_database('Management')
records=db.student


#menu for the student management system
def first_menu():
    print('Enter your profile')
    print('1)Admin')
    print('2)Teacher')
    print('3)Student')

#admin menu
def admin_menu():
    print('Welcome Admin !!')
    print('1)View Database')
    print('2)Update a record')
    print('3)Delete a record')
    print('4)Search a record')
    print('5)Update fees')
    

#teacher menu
def teacher_menu():
    print('Welcome Teacher !!')
    print('1)Create your profile')
    print('2)Update Course Info')
    print('3)Add marks')
    print('4)Update attendence')
    

#student menu
def student_menu():
    print('Welcome Student !!')
    print('1)Create your profile')
    print('2)View course info')
    print('3)View personal info')
    print('4)View attendence')
    
    

while(True):
    first_menu()
    profile=int(input())
    if profile==1:
        admin_menu()
        break
    elif profile==2:
        teacher_menu()
        break
    elif profile==3:
        student_menu()
        break
    else:
        print('invalid input')
        break

# student section

#student profile creation and adding data into database
def student_info_insert():
    try:
        
        stuName = input('Enter Name :')
        stuId = input('Enter Roll Number :')
        stuContact = input('Enter Contact Number :')
        stuAddress = input('Enter Address :')
        
        db.student.insert_many([
            {
                "name": stuName,
                "roll_no":stuId,
                "contact":stuContact,
                "address":stuAddress
        }])
        print ('\nCreated your profile Successfully\n')
    
    except Exception as e:
        print(e)
    

while(True):
    student_menu()
    action=int(input())
    if action==1:
        student_info_insert()
        break
#    elif action==2:
#        course_info()
#    elif profile==3:
#        personal_info()
#    elif profile==4:
#        view_attendence() 
    else:
        print('invalid input')
        break
    
    

#Teacher section

def teacher_info_insert():
    try:
        
        teaName = input('Enter Name :')
        teaId = input('Enter ID Number :')
        teaCourse = input('Enter Alloted course :')
        
        
        db.teacher.insert_many([
            {
                "name": teaName,
                "id_no":teaId,
                "course":teaCourse,
                
        }])
        print ('\nCreated your profile Successfully\n')
    
    except Exception as e:
        print(e)
    

while(True):
    teacher_menu()
    act=int(input())
    if act==1:
        teacher_info_insert()
        break
#    elif action==2:
#        update_course_info()
#    elif profile==3:
#        add_marks()
#    elif profile==4:
#        update_attendence() 
    else:
        print('invalid input')
        break

#admin section

db=client.get_database('Management')
stu_data = db["student"]

#roll_no=int(input("Enter the roll no: "))
def view_database():
    for x in stu_data.find({},{ "_id": 0 }):
        print(x)

while(True):
    admin_menu()
    act=int(input())
    if act==1:
        view_database()
        break
#    elif action==2:
#        update_course_info()
#    elif profile==3:
#        add_marks()
#    elif profile==4:
#        update_attendence() 
    else:
        print('invalid input')
        break