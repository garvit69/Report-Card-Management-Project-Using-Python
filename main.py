#Shreya Shah code 201112204 SEM 3 CSE SEC 2
import MySQLdb
import csv
import random
from os import remove, rename
import matplotlib.pyplot as pp
def createdb():
 sq = 'create database admissionform'
 try:
 cursor.execute(sq)
 print('Database called admissionform has been created.')
 except:
 print('Database already exists.')
def newadm():
 fin = open('student.txt', 'r')
 c = 0
 for data in fin:
 c += 1
 if c >= 1:
 admno = c + 1001
 elif c == 0:
 admno = 1001
 fout = open('student.txt', 'a')
 n = input('Please enter your name=?')
 na = n.upper()
 ro = int(input('Please enter your roll no=?'))
 cla = int(input('Please enter your class[11/12]=?'))
 while not (cla > 10 and cla <= 12):
 print('ERROR!This is a wrong input.Please input a valid 
class[11/12].')
 cla = int(input('Please enter your class=?'))
 sec = input('Please enter your section[A-Z/a-z]=?')
 while not (sec >= 'A' and sec <= 'Z' or sec >= 'a' and sec <= 'z'):
 print('ERROR!This is a wrong input.Please input a valid section[AZ/a-z].')
 sec = input('Please enter your section[A-Z]=?')
 s = sec.upper()
 cl = str(cla) + '-' + s
 ge = input('Please enter your gender[M/F]=?')
 gen = ge.upper()
 while not (len(gen) == 1):
 print('Please type either M or F')
 ge = input('Please enter your gender[M/F]=?')
 gen = ge.upper()
 ddob = int(input('Please enter your birth date[1-31]=?'))
 mdob = int(input('Please enter your birth month number[1-12]=?'))
 ydob = int(input('Please enter your birth year=?'))
 mdays = 0
 if mdob == 1 or mdob == 3 or mdob == 5 or mdob == 7 or mdob == 8 or mdob 
== 10 or mdob == 12:
 mdays = 31
 elif mdob == 4 or mdob == 6 or mdob == 9 or mdob == 11:
 mdays = 30
 elif mdob == 2:
 if ydob % 4 == 0 and ydob % 100 != 0 or ydob % 400 == 0:
 mdays = 29
 else:
 mdays = 28
 year = 2021
 age = year - ydob
 if age == 19 or age == 18 or age == 17 or age == 16 or age == 15 or age 
== 14:
 if ddob >= 1 and ddob <= mdays:
 print('Date is Valid')
 else:
 print('Date is invalid')
 ddob = int(input('Please enter your birth date[1-31]=?'))
 mdob = int(input('Please enter the no. of your birth month[1-
12]=?'))
 ydob = int(input('Please enter year of date of birth=?'))
 else:
 print('Date is invalid')
 ddob = int(input('Please enter your birth date[1-31]=?'))
 mdob = int(input('Please enter the no. of your birth month[1-12]=?'))
 ydob = int(input('Please enter year of date of birth=?'))
 dob = str(ddob) + '/' + str(mdob) + '/' + str(ydob)
 fn = input('Please enter name of your father=?')
 fname = fn.upper()
 mn = input('Please enter name of your mother=?')
 mname = mn.upper()
 pno = int(input('Please enter your phone number=?'))
 subc = input('Please enter your stream code[SB/SE/CI/SC/CM/HU]=?')
 scode = subc.upper()
 arr = str(admno) + ',' + na + ',' + str(ro) + ',' + str(cl) + ',' + gen + 
',' + dob + ',' + fname + ',' + mname + ',' + str(pno) + ',' + scode + '\n'
 fout.write(arr)
 fin.close()
 fout.close()
def modif():
 fin = open('student.txt')
 ad = int(input('Adm No.=?'))
 record = fin.readlines()
 found = 0
 for x in range(len(record)):
 line = record[x].strip()
 arr = line.split(',')
 if ad == int(arr[0]):
 print('These are the options you can modify.')
 print('1.NAME')
 print('2.ROLL NUMBER')
 print('3.CLASS or SECTION')
 print('4.DATE OF BIRTH')
 print('5.NAME OF FATHER')
 print('6.NAME OF MOTHER')
 print('7.PHONE NUMBER')
 print('8.SUBJECT CODE')
 print('9.EXIT')
 choice = input('What you want to modify[1-9]=?')
 if choice in '123456789':
 if choice == '1':
 arr[1] = input('New Name=?')
 elif choice == '2':
 arr[2] = str(int(input('New roll no=?')))
 elif choice == '3':
 cla = int(input('Please enter your class[11/12]=?'))
 while not (cla > 10 and cla <= 12):
 print('ERROR!This is a wrong input.Please input a 
valid class[11/12].')
 cla = int(input('Please enter your class=?'))
 sec = input('Please enter your section[A-Z/a-z]=?')
 while not (sec >= 'A' and sec <= 'Z' or sec >= 'a' and 
sec <= 'z'):
 print('ERROR!This is a wrong input.Please input a 
valid section[A-Z/a-z].')
 sec = input('Please enter your section[A-Z]=?')
 s = sec.upper()
cl = str(cla) + s
arr[3] = cl
 elif choice == '4':
 ddob = int(input('Please enter your birth date[1-31]=?'))
 mdob = int(input('Please enter your birth month[1-
12]=?'))
 ydob = int(input('Please enter year of date of birth=?'))
 mdays = 0
if mdob == 1 or mdob == 3 or mdob == 5 or mdob == 7 or 
mdob == 8 or mdob == 10 or mdob == 12:
 mdays = 31
 elif mdob == 4 or mdob == 6 or mdob == 9 or mdob == 11:
 mdays = 30
 elif mdob == 2:
 if ydob % 4 == 0 and ydob % 100 != 0 or ydob % 400 == 
0:
 mdays = 29
 else:
 mdays = 28
 year = 2021
age = year - ydob
 if not (
 age == 19 or age == 18 or age == 17 or age == 16 
or age == 15 or age == 14 and ddob >= 1 and ddob <= mdays):
 print('Date is invalid')
 ddob = int(input('Please enter your birth date[1-
31]=?'))
 mdob = int(input('Please enter the no. of your birth 
month[1-12]=?'))
 ydob = int(input('Please enter year of date of 
birth=?'))
 dob = str(ddob) + '/' + str(mdob) + '/' + str(ydob)
 arr[5] = str(dob)
 elif choice == '5':
 arr[6] = input('New Name of Father=?')
 elif choice == '6':
 arr[7] = input('New Name of Mother=?')
 elif choice == '7':
 arr[8] = str(int(input('New Mobile No=?')))
 elif choice == '8':
 arr[9] = input('New Stream[SB/SE/CI/SC/CM/HU]=?')
 found = 1
 record[x] = ','.join(arr) + '\n'
 if found == 1:
 fout = open('student.txt', 'w')
 fout.writelines(record)
 fout.close()
 else:
 print('Admission number not found')
def delete():
 fin = open('student.txt', 'r')
 fout = open('temp.txt', 'w')
 ad = int(input('Adm No.=?'))
 found = 0
 for data in fin:
 line = data.strip()
 arr = line.split(',')
 if ad == int(arr[0]):
 found = 1
 else:
 fout.write(data)
 if found == 1:
 print('You have successfully deleted the details.Thank you')
 else:
 print('Admission no. was not found')
 fout.close()
 fin.close()
 remove('student.txt')
 rename('temp.txt', 'student.txt')
def displ():
 fin = open('student.txt', 'r')
 ad = int(input('Adm No.=?'))
 found = 0
 for data in fin:
 line = data.strip()
 arr = line.split(',')
 if int(arr[0]) == ad:
 print(arr)
 found = 1
 if found == 0:
 print('Admission no. was not found')
 fin.close()
def graph():
 x = []
 y = []
 with open('student.txt', 'r') as csvfile:
 plots = csv.reader(csvfile, delimiter=',')
 for row in plots:
 x.append(row[1])
 y.append(row[3])
 pp.scatter(x, y, label='Graph!')
 pp.xlabel("Student's Name")
 pp.ylabel('Class of Student')
 pp.title('Number of Students enrolled per class.')
 pp.legend()
 pp.show()
def marks_grade_calculation():
 fin = open('student.txt', 'r')
 found = 0
 record = fin.readlines()
 ad = int(input('Please enter Admission No. to enter marks for='))
 for x in range(len(record)):
 line = record[x].strip()
 arr = line.split(',')
 if ad == int(arr[0]):
 found = 1
 print(arr)
 if arr[9] == 'SB':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF MATHS=?'))
 m3 = float(input('MARKS OF PHYSICS=?'))
 m4 = float(input('MARKS OF CHEMISTRY=?'))
 m5 = float(input('MARKS OF BIOLOGY=?'))
 elif arr[9] == 'SE':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF MATHS=?'))
 m3 = float(input('MARKS OF PHYSICS=?'))
 m4 = float(input('MARKS OF CHEMISTRY=?'))
 m5 = float(input('MARKS OF ECONOMICS=?'))
 elif arr[9] == 'CI':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF ECONOMICS=?'))
 m3 = float(input('MARKS OF ACCOUNTANCY=?'))
 m4 = float(input('MARKS OF BUISNESS STUDIES=?'))
 m5 = float(input('MARKS OF INFORMATICS PRATICES=?'))
 elif arr[9] == 'SC':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF MATHS=?'))
 m3 = float(input('MARKS OF PHYSICS=?'))
 m4 = float(input('MARKS OF CHEMISTRY=?'))
 m5 = float(input('MARKS OF COMPUTER SCIENCE=?'))
 elif arr[9] == 'CM':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF MATHS=?'))
 m3 = float(input('MARKS OF ECONOMICS=?'))
 m4 = float(input('MARKS OF ACCOUNTANCY=?'))
 m5 = float(input('MARKS OF BUSINESS STUDIES=?'))
 elif arr[9] == 'HU':
 m1 = float(input('MARKS OF ENGLISH=?'))
 m2 = float(input('MARKS OF HISTORY=?'))
 m3 = float(input('MARKS OF GEOGRAPHY=?'))
 m4 = float(input('MARKS OF ECONOMICS=?'))
 m5 = float(input('MARKS OF POLITICAL STUDICAL STUDIES=?'))
 tot = m1 + m2 + m3 + m4 + m5
 avg = tot / 5
 for k in range(5):
 subj = input('Please enter subject[sub1/sub2/sub3/sub4/sub5] 
you want to know the grade for=?')
 subject = subj.lower()
 if subject == 'sub1':
 if m1 >= 60:
 gr1 = 'A'
status1 = 'PASS'
 elif m1 >= 50 and m1 < 60:
 gr1 = 'B'
status1 = 'PASS'
 elif m1 >= 40 and m1 < 50:
 gr1 = 'C'
 status1 = 'PASS'
 elif m1 >= 33 and m1 < 40:
 gr1 = 'D'
status1 = 'PASS'
 else:
 gr1 = 'E'
status = 'FAIL'
print('You have failed in this subject.')
 print('Grade Calculated for this subject which is=', gr1)
 elif subject == 'sub2':
 if m2 >= 60:
 gr2 = 'A'
status2 = 'PASS'
 elif m2 >= 50 and m2 < 60:
 gr2 = 'B'
status2 = 'PASS'
 elif m2 >= 40 and m2 < 50:
 gr2 = 'C'
 status2 = 'PASS'
 elif m2 >= 33 and m2 < 40:
 gr2 = 'D'
status2 = 'PASS'
 else:
 gr2 = 'E'
status2 = 'FAIL'
 print('You have failed in this subject.')
 print('Grade Calculated for this subject which is=', gr2)
 elif subject == 'sub3':
 if m3 >= 60:
 gr3 = 'A'
 status3 = 'PASS'
 elif m3 >= 50 and m3 < 60:
 gr3 = 'B'
status3 = 'PASS'
 elif m3 >= 40 and m3 < 50:
 gr3 = 'C'
 status3 = 'PASS'
 elif m3 >= 33 and m3 < 40:
 gr3 = 'D'
status3 = 'PASS'
 else:
 gr3 = 'E'
status3 = 'FAIL'
 print('You have failed in this subject.')
 print('Grade Calculated for this subject which is=', gr3)
 elif subject == 'sub4':
 if m4 >= 60:
 gr4 = 'A'
 status4 = 'PASS'
 elif m4 >= 50 and m4 < 60:
 gr4 = 'B'
status4 = 'PASS'
 elif m4 >= 40 and m4 < 50:
 gr4 = 'C'
status4 = 'PASS'
 elif m4 >= 33 and m4 < 40:
 gr4 = 'D'
status4 = 'PASS'
 else:
 gr4 = 'E'
status4 = 'FAIL'
 print('You have failed in this subject.')
 print('Grade Calculated for this subject which is=', gr4)
 else:
 if m5 >= 60:
 gr5 = 'A'
status5 = 'PASS'
 elif m5 >= 50 and m5 < 60:
 gr5 = 'B'
status5 = 'PASS'
 elif m5 >= 40 and m5 < 50:
 gr5 = 'C'
status5 = 'PASS'
 elif m5 >= 33 and m5 < 40:
 gr5 = 'D'
status5 = 'PASS'
 else:
 gr5 = 'E'
status5 = 'FAIL'
print('You have failed in this subject.')
 print('Grade Calculated for this subject which is=', gr5)
 lis = str(arr[0]) + ',' + arr[1] + ',' + arr[9] + ',' + str(gr1) 
+ ',' + str(m1) + ',' + str(
 gr2) + ',' + str(m2) + ',' + str(gr3) + ',' + str(m3) + ',' + 
str(gr4) + ',' + str(m4) + ',' + str(
 gr5) + ',' + str(m5) + ',' + str(tot) + ',' + str(avg) + ',' 
+ str(status1) + ',' + str(
 status2) + ',' + str(status3) + ',' + str(status4) + ',' + 
str(status5) + ',' + arr[6] + ',' + arr[
 7] + ',' + arr[3] + '\n'
 print('Grade1', 'Marks1', 'Grade2', 'Marks2', 'Grade3', 'Marks3', 
'Grade4', 'Marks4', 'Grade5', 'Marks5',
 'TOTAL', 'AVG_MARK', sep=' \t')
 print(gr1, m1, gr2, m2, gr3, m3, gr4, m4, gr5, m5, tot, avg, 
sep=' \t')
 found = 1
 if found == 1:
 fout = open('result.txt', 'a')
 fout.write(lis)
 fout.close()
 else:
 print('Sorry.The Admission No. was not found in the file.')
def display():
 fin = open('student.txt', 'r')
 found = 0
 record = fin.readlines()
 cursor.execute('use admissionform')
 sq2 = 'create table stud(Admission numeric(6),Name char(25),Roll 
numeric(2),Class char(4),Father char(25),Mother char(25),Stream char(2))'
 try:
 cursor.execute(sq2)
 except:
 cursor.execute('drop table stud')
 cursor.execute(sq2)
 finally:
 for x in range(len(record)):
 line = record[x].strip()
 arr = line.split(',')
 adno = int(arr[0])
 name = arr[1]
 ro = int(arr[2])
 clas = arr[3]
 fname = arr[6]
 mname = arr[7]
 stream = arr[9]
 sq1 = 'insert into stud 
values({},"{}",{},"{}","{}","{}","{}")'.format(adno, name, ro, clas, fname, 
mname,
 
stream)
 cursor.execute(sq1)
 cursor.execute('select * from stud ')
 data = cursor.fetchall()
 for da in data:
 for d in da:
 print(d, end='\t')
 print()
 db.commit()
def swrl():
 fin = open('result.txt', 'r')
 found = 0
 record = fin.readlines()
 cursor.execute('use admissionform')
 sq1 = 'create table result(Admission numeric(6),Name char(25),Stream 
char(2),GRADE_SUB1 char(1),MARKS_SUB1 float,GRADE_SUB2 char(1),MARKS_SUB2 
float,GRADE_SUB3 char(1),MARKS_SUB3 float,GRADE_SUB4 char(1),MARKS_SUB4 
float,GRADE_SUB5 char(1),MARKS_SUB5 float,TOTAL_MARKS float,AVG_MARKS float)'
 try:
 cursor.execute(sq1)
 except:
 cursor.execute('drop table result')
 cursor.execute(sq1)
 finally:
 for x in range(len(record)):
 line = record[x].strip()
 arr = line.split(',')
 adno = int(arr[0])
 name = arr[1]
 stream = arr[2]
 grade1 = arr[3]
 marks1 = float(arr[4])
 grade2 = arr[5]
 marks2 = float(arr[6])
 grade3 = arr[7]
 marks3 = float(arr[8])
 grade4 = arr[9]
 marks4 = float(arr[10])
 grade5 = arr[11]
 marks5 = float(arr[12])
 totalmark = float(arr[13])
 avgmark = float(arr[14])
 sq1 = 'insert into result 
values({},"{}","{}","{}",{},"{}",{},"{}",{},"{}",{},"{}",{},{},{})'.format(ad
no,
 
name,
 
stream,
 
grade1,
 
marks1,
grade2,
marks2,
grade3,
 
marks3,
 
grade4,
 
marks4,
 
grade5,
 
marks5,
 
totalmark,
 
avgmark)
 cursor.execute(sq1)
 cursor.execute('select * from result order by admission')
 data = cursor.fetchall()
 for da in data:
 for d in da:
 print(d, end='\t')
 print()
 db.commit()
def mos():
 admiss = int(input('Enter the admission number of student=?'))
 
print('``````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````
````````````')
 print(
 ' FIRST 
TERM REPORT CARD 
')
 
print('``````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````
````````````')
 print(
 ' NAME OF SCHOOL : 
JAYSHREE PERIWAL INTERNATIONAL SCHOOL, JAIPUR 
')
 print()
 print(
 ' 
ACADEMIC YEAR : 2021-2022 
')
 with open('student.txt', mode='r') as csvfile:
 record = csv.reader(csvfile,delimiter=',')
 ch=0
 while ch==0:
 found=0
 for arr in record:
 if len(arr):
 if int(arr[0])==admiss:
 found = 1
print("FATHER'S NAME : ", 
arr[6],"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t","Attendance : 
",random.uniform(50.00,99.99))
 print("MOTHER'S NAME : ", arr[7])
 print("STUDENT'S NAME :", arr[1])
 print('ADMISSION NUMBER :', arr[0])
 print('CLASS OF THE STUDENT :', arr[3])
 print('ROLL NUMBER OF STUDENT :', int(arr[2]))
 print('STREAM : ', arr[9])
 print()
with open('result.txt', mode='r') as csvfile:
 record = csv.reader(csvfile, delimiter=',')
 while True:
 for arr in record:
 if len(arr):
 if int(arr[0]) == admiss:
 if (arr[2]=="SB"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 print('ENGLISH\t\t\t', 
arr[4],'\t\t\t', arr[3])
 
print('MATHS\t\t\t',arr[6],'\t\t\t', arr[5])
 
print('PHYSICS\t\t\t',arr[8],'\t\t\t', arr[7])
 
print('CHEMISTRY\t\t\t',arr[10],'\t\t\t', arr[9])
 
print('BIOLOGY\t\t\t',arr[12],'\t\t\t', arr[11])
 elif (arr[2]=="SE"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 print('ENGLISH 
\t\t\t',arr[4],' \t\t\t', arr[3])
 print('MATHS 
\t\t\t',arr[6],' \t\t\t', arr[5])
 print('PHYSICS 
\t\t\t',arr[8],' \t\t\t', arr[7])
 
print('CHEMISTRY\t\t\t',arr[10],'\t\t\t\t',arr[9])
 
print('ECONOMICS\t\t\t',arr[12],'\t\t\t\t', arr[11])
 elif (arr[2]=="CI"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 
print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
 
print('ECONOMICS\t\t\t',arr[6],'\t\t\t', arr[5])
 
print('ACCOUNTANCY\t\t\t',arr[8],'\t\t\t', arr[7])
 print('BUISNESS 
STUDIES\t\t\t',arr[10],'\t\t\t', arr[9])
 print('INFORMATICS 
PRACTICES\t \t',arr[12],'\t\t\t', arr[11])
 elif (arr[2]=="SC"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 
print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
 
print('MATHS\t\t\t',arr[6],'\t\t\t', arr[5])
 
print('PHYSICS\t\t\t',arr[8],'\t\t\t', arr[7])
 
print('CHEMISTRY\t\t\t',arr[10],'\t\t\t', arr[9])
 print('COMPUTER SCIENCE\t 
\t', arr[12],'\t\t\t', arr[11])
 elif (arr[2]=="CM"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 
print('ENGLISH\t\t\t',arr[4],'\t\t\t', arr[3])
 print('MATHS\t\t\t', 
arr[6],'\t\t\t', arr[5])
 
print('ECONOMICS\t\t\t',arr[8],'\t\t\t', arr[7])
 
print('ACCOUNTANCY\t\t\t',arr[10],'\t\t\t', arr[9])
 print('BUISNESS STUDIES 
\t\t',arr[12],'\t\t\t', arr[11])
 elif (arr[2]=="HU"):
 print('SUBJECT\t\t\tMARKS 
OBTAINED\t\t\tGRADE')
 print('ENGLISH\t\t\t', 
arr[4],'\t\t\t', arr[3])
 print('HISTORY\t\t\t', 
arr[6],'\t\t\t', arr[5])
 print('GEOGRAPHY\t\t\t', 
arr[8],'\t\t\t', arr[7])
 print('ECONOMICS\t\t\t', 
arr[10],'\t\t\t', arr[9])
 print('POLITICAL SCIENCE 
\t\t',arr[12],'\t\t\t', arr[11])
 print()
print('TOTAL MARKS OBTAINED : ', 
float(arr[13]),'\tAVERAGE OF THE STUDENT : ', float(arr[14]))
 else:
 print('Admission number not found!!')
 ch+=1
 break
db = MySQLdb.connect('localhost', 'root', 'password_of_your_mysql')
cursor = db.cursor()
ch = 1
while ch:
 print('0.CREATE A NEW DATABASE')
 print('1.NEW ADMISSION')
 print('2.MODIFICATION')
 print('3.DELETION')
 print('4.DISPLAY A PARTICULAR RECORD')
 print('5.DISPLAY THE ENTIRE TABLE')
 print('6.DISPLAY GRAPHICALLY')
 print('7.MARKS ENTRY AND GRADE DISPLAY ')
 print('8.REPORT CARD')
 print('9.EXIT FROM MENU')
 cho = input('Please input your choice[0-9]=?')
 if cho == '0':
 createdb()
 if cho == '1':
 newadm()
 elif cho == '2':
 modif()
 elif cho == '3':
 delete()
 elif cho == '4':
 displ()
 elif cho == '5':
 display()
 elif cho == '6':
 graph()
 elif cho == '7':
 marks_grade_calculation()
 elif cho == '8':
 while True:
 print('Please select from below options:')
 print('1.RESULT OF ALL THE STUDENTS')
 print('2.MARKSHEET OF A PARTICULAR STUDENT')
 print('3.EXIT FROM MENU')
 choice = input('CHOICE[1-5]=?')
 if choice == '1':
 swrl()
 elif choice=='2':
 mos()
 elif choice == '3':
 print('You have exited from menu')
 break
 elif cho == '9':
 print('You have exited from menu')
 break
