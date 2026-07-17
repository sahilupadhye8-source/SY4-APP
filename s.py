def student(name,rollno):
    print("name;",name,"rollno;",rollno)

def student_name(name,rollno):
    print("name;",name,"rollno;",rollno)

def student_default(name,rollno,Class="sy4"):
    print("name;",name,"rollno;",rollno,"class;",Class)

def student_length(*sub):
    print("subject:",*sub)

student("piyush",21)
student_name(rollno=22,name="rahul")
student_default("rohan",23)
student_length("python")
          
    