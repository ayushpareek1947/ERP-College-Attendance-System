#ERP PROJECT


import pyrebase
import smtplib

config = {
  "apiKey": "apiKey",
  "authDomain": "erproject-dd24e-default-rtdb.firebaseapp.com",
  "databaseURL": "https://erproject-dd24e-default-rtdb.firebaseio.com",
  "storageBucket": "erproject-dd24e-default-rtdb.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("Student").push({"DAY":""})
db.child("Faculty").push({"DAY":""})                 
student=["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"]
faculty=["f1","f2","f3","f4","f5"]
st={}
data,data1='',''
st1={}
fa={}
fa1={}
i=1
import schedule
import time
def j():
    global i
    import pandas as pd
    st1.update({i:st})
    data=pd.DataFrame(st1)
    print(data)
    data.to_csv('student.csv')
    fa1.update({i:fa})
    data1=pd.DataFrame(fa1)
    print(data1)
    data1.to_csv('faculty.csv')
    i=i+1  
while(1):
    schedule.every(10).seconds.do(j)
    schedule.run_pending()
    time.sleep(1)
    f=input("enter 's' for student,enter 'f' for faculty")
    f=f.upper()
    if(f=="S"):
        name=input("enter student name")
        if name in student:
            a=input("enter 'a' for absent,enter 'l' for leave,enter 'p' for present")
            a=a.upper()
            if(a=="L"): #please change sender and receiver's email id for this function to work 
                import smtplib
                server =smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("sender@gamil.com","akki@9510")
                message=name+"is on leave"
                server.sendmail("sender@gamil.com","receiver@gamil.com",message)
                a="A"
            st.update({name:a})
            from datetime import datetime
            now = datetime.now() # current date and time
            date_time = now.strftime("%d-%m-%Y")
            db.child("Student").child("DAY").child(date_time).update({name:a})
           
    if(f=="F"):
        name=input("enter faculty name")
        if name in faculty:
            a=input("enter 'a' for absent,enter 'l' for leave,enter 'p' for present")
            a=a.upper()
            if(a=="L"):
                import smtplib
                server =smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("sender@gamil.com","akki@9510")
                message=name+"is on leave"
                server.sendmail("sender@gamil.com","receiver@gamil.com",message)
                a="A"
            fa.update({name:a})
            from datetime import datetime
            now = datetime.now() # current date and time
            date_time = now.strftime("%d-%m-%Y")
            db.child("Faculty").child("DAY").child(date_time).update({name:a})
