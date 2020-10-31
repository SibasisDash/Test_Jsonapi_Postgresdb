import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="mydb", user='postgres', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
#sql1 = '''CREATE database mydb''';

# Creating a database
#cursor.execute(sql1)

#Droping CURRENCY table if already exists.
cursor.execute("DROP TABLE IF EXISTS CURRENCY")
#Creating table as per requirement
sql2 ='''CREATE TABLE CURRENCY(
   CURR VARCHAR(10) NOT NULL
)'''
cursor.execute(sql2)

sql4 = '''INSERT INTO CURRENCY VALUES('EUR'),('USD'),('GBP'),
        ('CAD'),('NZD'),('INR'),('JPY')'''

cursor.execute(sql4)

#Droping historical data table if already exists.
cursor.execute("DROP TABLE IF EXISTS hist_data")
#Creating table as per requirement
sql3 ='''CREATE TABLE hist_data(
   ID INT NOT NULL,
   DATE DATE NOT NULL,
   EUR float,
   USD float,
   CAD float,
   NZD float,
   INR float,
   JPY float,
   GBP float
)'''
cursor.execute(sql3)


# Closing the connection
conn.close()
