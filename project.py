import sys
import mysql.connector
import csv
import os


def connect_to_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zippy",
            database = "cs122a"
         
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)

def add_user(UCINetID, First, Middle, Last,connection):
    user_query = "INSERT INTO Users (UCINetID, Firstname, Middlename, Lastname)VALUES ('{}', '{}', '{}', '{}');".format(UCINetID, First, Middle, Last)
    
    cursor = connection.cursor()

    cursor.execute(user_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_email(UCINetID, Email,connection):
    email_query = "INSERT INTO UserEmail (UCINetID, Email)VALUES ('{}','{}' )".format(UCINetID, Email)
    
    cursor = connection.cursor()

    cursor.execute(email_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_student(UCINetID,connection):
    student_query = "INSERT INTO Students (UCINetID)VALUES ('{}' )".format(UCINetID)
    cursor = connection.cursor()

    cursor.execute(student_query)

    # Committing the changes
    connection.commit()
    cursor.close()
   
def add_admins(UCINetID, connection):
    admins_query = "INSERT INTO Administrators (UCINetID)VALUES ('{}' )".format(UCINetID)
    cursor = connection.cursor()

    cursor.execute(admins_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_course(CourseID,Title,Quarter,connection):
    course_query = "INSERT INTO Courses (CourseID, Title, Quarter)VALUES ('{}', '{}', '{}')".format(CourseID,Title,Quarter)

    cursor = connection.cursor()

    cursor.execute(course_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_project(ProjectID,Name,Description,CourseID,connection):
    
    course_query = "INSERT INTO Projects (ProjectID, Name, Description, CourseID) VALUES ('{}', '{}', '{}','{}')".format(ProjectID,Name,Description,CourseID)

    cursor = connection.cursor()

    cursor.execute(course_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_machine(MachineID ,Hostname, IPAddress ,OperationalStatus,Location,connection):
    machine_query = "INSERT INTO Machines (MachineID, Hostname, IPAddress, OperationalStatus, Location)VALUES ( '{}','{}','{}','{}','{}')".format(MachineID ,Hostname, IPAddress ,OperationalStatus,Location)
    cursor = connection.cursor()

    cursor.execute(machine_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_use(ProjectID,StudentUCINetID,MachineID,StartDate,EndDate,connection):
    use_query = "INSERT INTO StudentUseMachinesInProject (ProjectID ,StudentUCINetID ,MachineID ,StartDate ,EndDate ) VALUES  ('{}', '{}', '{}','{}','{}')".format(ProjectID,StudentUCINetID,MachineID,StartDate,EndDate)
    cursor = connection.cursor()

    cursor.execute(use_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def add_mange(UCINetID,MachineID,connection):
    manage_query = "INSERT INTO AdministratorManageMachines (AdministratorUCINetID, MachineID)VALUES ('{}','{}'  )".format(UCINetID,MachineID)
    cursor = connection.cursor()

    cursor.execute(manage_query)

    # Committing the changes
    connection.commit()
    cursor.close()

def get_table_size(table_name,connection):

    cursor = connection.cursor()

    cursor.execute("SELECT count(*) FROM {}".format(table_name))

    size = cursor.fetchone()[0]

    cursor.close()

    return size

def deleteStudent(UCINetID,connection):
    delete = "DELETE FROM Students WHERE UCINetID = '{}'".format(UCINetID)
    cursor = connection.cursor()

    cursor.execute(delete)

    # Committing the changes
    connection.commit()
    cursor.close()

def deleteUser(UCINetID,connection):
    delete = "DELETE FROM Users WHERE UCINetID = '{}'".format(UCINetID)
    cursor = connection.cursor()

    cursor.execute(delete)

    # Committing the changes
    connection.commit()
    cursor.close()



def drop_table(connection):

    create_table_query = "DROP TABLE administratormanagemachines"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP TABLE studentusemachinesinproject"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()
      
    create_table_query = "DROP TABLE projects"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP Table useremail"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP TABLE students"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP TABLE administrators"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP TABLE courses"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()


    create_table_query = "DROP TABLE machines"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    create_table_query = "DROP TABLE Users"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()

    connect.close()
 
def create_tables(connection):
    create_table_query = "CREATE TABLE Users (UCINetID VARCHAR(255) PRIMARY KEY, Firstname VARCHAR(255), Middlename VARCHAR(255), Lastname VARCHAR(255)  );"     
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

    create_table_query = "CREATE TABLE UserEmail (UCINetID VARCHAR(255) NOT NULL, Email VARCHAR(255),  PRIMARY KEY (UCINetID, Email), FOREIGN KEY (UCINetID) REFERENCES Users (UCINetID) ON DELETE CASCADE );"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

    create_table_query = "CREATE TABLE Students (UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID) ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

    create_table_query = "CREATE TABLE Administrators (UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID)ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

    create_table_query = "CREATE TABLE Courses (CourseID INT PRIMARY KEY NOT NULL,Title VARCHAR(100),Quarter VARCHAR(20));"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()
    
    create_table_query = "CREATE TABLE Projects (ProjectID INT PRIMARY KEY NOT NULL,Name VARCHAR(100),Description TEXT,CourseID INT NOT NULL,FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()


    create_table_query = "CREATE TABLE Machines (MachineID INT PRIMARY KEY NOT NULL, Hostname VARCHAR(255), IPAddress VARCHAR(15),OperationalStatus VARCHAR(50),Location VARCHAR(255));"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()
    #add managae and use rel tables

    create_table_query =" CREATE TABLE StudentUseMachinesInProject (ProjectID INT,StudentUCINetID VARCHAR(20),MachineID INT,StartDate DATE,EndDate DATE, PRIMARY KEY (ProjectID, StudentUCINetID, MachineID),FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),FOREIGN KEY (StudentUCINetID) REFERENCES Students(UCINetID),FOREIGN KEY (MachineID) REFERENCES Machines(MachineID) ON DELETE CASCADE);"

    
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

    create_table_query = "CREATE TABLE AdministratorManageMachines (AdministratorUCINetID VARCHAR(20),MachineID INT,PRIMARY KEY (AdministratorUCINetID, MachineID),FOREIGN KEY (AdministratorUCINetID) REFERENCES Administrators(UCINetID),FOREIGN KEY (MachineID) REFERENCES Machines(MachineID) ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

def import_data(folderName:str, connection):
    try:
        drop_table(connection)
    
        print("did try")
    except:
        print("NO Tables to drop")

    #read folder files, add tables and return(Table - (Number of users,Number of machine, Number of Course))
    file_name = "admins.csv"
    file_path = os.path.join(folderName, file_name)

    create_tables(connection)

    with open(f"{folderName}/users.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_user(row[0],row[1],row[2],row[3],connection)
            
    with open(f"{folderName}/emails.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_email(row[0],row[1],connection)
            
    with open(f"{folderName}/students.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_student(row[0],connection)
            
    with open(f"{folderName}/admins.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_admins(row[0],connection)
            
    with open(f"{folderName}/courses.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_course(row[0],row[1],row[2],connection)


    with open(f"{folderName}/projects.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_project(row[0],row[1],row[2],row[3],connection)

    with open(f"{folderName}/machines.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_machine(row[0],row[1],row[2],row[3],row[4],connection)




    with open(f"{folderName}/use.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_use(row[0],row[1],row[2],row[3],row[4],connection)


    with open(f"{folderName}/manage.csv","r") as f:
        csv_reader = csv.reader(f)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Process each row
            add_mange(row[0],row[1],connection)

if __name__ == "__main__":

    args = sys.argv

    connection = connect_to_database()

    print(args)
    if args[1] == "import":
        import_data(folderName=args[2],connection=connection)
        print(str(get_table_size("Users",connection))+","+str(get_table_size("Machines",connection))+","+str(get_table_size("Courses",connection)))

    elif args[1]  == "insertStudent":
        try:
            add_user(args[2],args[4],args[5],args[6],connection)
            add_student(args[2],connection)
            add_email(args[2],args[3],connection)
            print( True)
        except:
            print(False)     
    elif args[1] == "addEmail":
        try:        
            add_email(args[2],args[3],connection)
            print(True)
        except:
            print(False)
    elif args[1] ==  "deleteStudent":
        try:
            deleteUser(args[2],connection)
            deleteStudent(args[2],connection)
            print(True)
        except:
            print(False)
    elif args[1] =="insertMachine":
        try:
            add_machine(args[2],args[3],args[4],args[5],args[6],connection)
            print(True)
        except:
            print(False)
    elif args[1] == "insertUse":
        try:
            add_use(args[2],args[3],args[4],args[5],args[6],connection)
            print(True)
        except:
            print(False)