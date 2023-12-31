import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='test'
)

mycursor = mydb.cursor()

def create_patient_load():
    sql = "insert into Patient1 values(%s, %s, %s, %s, %s, %s, %s)"
  
    val = [(1, "Patient 1", 56, "M", "AB-", "p1@gmail.com", 9590632784),
        (2, "Patient 2", 37, "F", "O-", "p2@gmail.com", 9467892345),
        (3, "Patient 3", 75, "F", "O+", "p3@yahoo.co.in", 9854327867),
        (4, "Patient 4", 23, "M", "A+", "p4@gmail.com", 9456789234),
        (5, "Patient 5", 17, "M", "AB+", "p5@gmail.com", 9782456792),
        (6, "Patient 6", 19, "M", "O+", "p6@gmail.com", 8723456724),
        (7, "Patient 7", 33, "F", "AB-", "p7@gmail.com", 7692354921),
        (8, "Patient 8", 99, "M", "O+", "p8@gmail.com", 7923456723),
        (9, "Patient 9", 3, "M", "B-", "p9@yahoo.com", 9492356724),
        (10, "Patient 10", 12, "M", "O+", "p10@gmail.com", 8236704562)]
  
    mycursor.executemany(sql, val)
    mydb.commit()
