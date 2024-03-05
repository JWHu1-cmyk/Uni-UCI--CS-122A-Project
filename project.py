import sys
import mysql.connector
import csv
import os


#use YYYY-MM-DD

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

def drop_table(connection):

    create_table_query = "DROP TABLE administratormanagemachines"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
   
    create_table_query = "DROP TABLE studentusemachinesinproject"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
   
    create_table_query = "DROP TABLE projects"     
    connect = connection.cursor()
    connect.execute(create_table_query) 


    create_table_query = "DROP Table useremail"     
    connect = connection.cursor()
    connect.execute(create_table_query) 

    create_table_query = "DROP TABLE students"     
    connect = connection.cursor()
    connect.execute(create_table_query) 

    create_table_query = "DROP TABLE administrators"     
    connect = connection.cursor()
    connect.execute(create_table_query) 

    create_table_query = "DROP TABLE courses"     
    connect = connection.cursor()
    connect.execute(create_table_query) 



    create_table_query = "DROP TABLE machines"     
    connect = connection.cursor()
    connect.execute(create_table_query) 

    create_table_query = "DROP TABLE Users"     
    connect = connection.cursor()
    connect.execute(create_table_query) 


   

def create_tables(connection):
    create_table_query = "CREATE TABLE Users (UCINetID VARCHAR(255) PRIMARY KEY, Firstname VARCHAR(255), Middlename VARCHAR(255), Lastname VARCHAR(255)  );"     
    connect = connection.cursor()
    connect.execute(create_table_query)

    create_table_query = "CREATE TABLE UserEmail (UCINetID VARCHAR(255) NOT NULL, Email VARCHAR(255),  PRIMARY KEY (UCINetID, Email), FOREIGN KEY (UCINetID) REFERENCES Users (UCINetID) );"
    connect = connection.cursor()
    connect.execute(create_table_query)

    create_table_query = "CREATE TABLE Students (UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID) ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)
 
    create_table_query = "CREATE TABLE Administrators (UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID)ON DELETE CASCADE);"
    connect = connection.cursor()
    connect.execute(create_table_query)

    create_table_query = "CREATE TABLE Courses (CourseID INT PRIMARY KEY NOT NULL,Title VARCHAR(100),Quarter VARCHAR(20));"
    connect = connection.cursor()
    connect.execute(create_table_query)

    
    create_table_query = "CREATE TABLE Projects (ProjectID INT PRIMARY KEY NOT NULL,Name VARCHAR(100),Description TEXT,CourseID INT NOT NULL,FOREIGN KEY (CourseID) REFERENCES Courses(CourseID));"
    connect = connection.cursor()
    connect.execute(create_table_query)



    create_table_query = "CREATE TABLE Machines (MachineID INT PRIMARY KEY NOT NULL,IPAddress VARCHAR(15),OperationalStatus VARCHAR(50),Location VARCHAR(255));"
    connect = connection.cursor()
    connect.execute(create_table_query)

    #add managae and use rel tables

    create_table_query = "CREATE TABLE StudentUseMachinesInProject (ProjectID INT,StudentUCINetID VARCHAR(255),MachineID INT,StartDate DATE,EndDate DATE,PRIMARY KEY (ProjectID, StudentUCINetID, MachineID),FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),FOREIGN KEY (StudentUCINetID) REFERENCES Students(UCINetID),FOREIGN KEY (MachineID) REFERENCES Machines(MachineID));"
    connect = connection.cursor()
    connect.execute(create_table_query)

    create_table_query = "CREATE TABLE AdministratorManageMachines (AdministratorUCINetID VARCHAR(20),MachineID INT,PRIMARY KEY (AdministratorUCINetID, MachineID),FOREIGN KEY (AdministratorUCINetID) REFERENCES Administrators(UCINetID),FOREIGN KEY (MachineID) REFERENCES Machines(MachineID));"
    connect = connection.cursor()
    connect.execute(create_table_query)







def import_data(folderName:str, connection):

    try:

        drop_table(connection)


        
        pass
    
    except:
        print("NO Tables to drop")

    #read folder files, add tables and return(Table - (Number of users,Number of machine, Number of Course))
    
    file_name = "admins.csv"
    file_path = os.path.join(folderName, file_name)

    create_tables(connection)



    # with open(file_path,'r') as file:





    





if __name__ == "__main__":

    args = sys.argv

    connection = connect_to_database()




    print(args)

    if args[1] == "import":
        import_data(folderName=args[2],connection=connection)
        

