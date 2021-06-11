#ERP PROJECT

   
dict={}
dict1={}
import pyrebase
import smtplib
import pandas as pd
import csv
from csv import writer
from csv import reader
config = {
  "apiKey": "apiKey",
  "authDomain": "erproject-dd24e-default-rtdb.firebaseapp.com",
  "databaseURL": "https://erproject-dd24e-default-rtdb.firebaseio.com",
  "storageBucket": "erproject-dd24e-default-rtdb.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%d-%m-%Y")
F=db.child("Faculty").child("DAY").child(date_time).get()
S=db.child("Student").child("DAY").child(date_time).get()


Fkey=[]
Fdetail=[]

for i in F.each():
    Fkey.append(i.key())
    Fdetail.append(i.val())


Skey=[]
Sdetail=[]

for i in S.each():
    Skey.append(i.key())
    Sdetail.append(i.val())
#print(Skey)# print name
#print(Sdetail)# present or absent

fnme = ["f1", "f2", "f3", "f4","f5"]
snme = ["s1", "s2", "s3", "s4","s5", "s6", "s7", "s8", "s9","s10"]

dict.update{'Name': fnme}
df = pd.DataFrame(dict)
df.to_csv('Faculty.csv')

dict1.update{'Name': fnme,  date_time: Fdetail}
ds = pd.DataFrame(dict1)
ds.to_csv('Faculty1.csv')

csv1 = pd.read_csv('Faculty.csv')
csv2 = pd.read_csv('Faculty1.csv')
merged = csv1.merge(csv2, on='Name')
merged.to_csv("Faculty2.csv", index=False)
