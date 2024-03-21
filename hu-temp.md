def emails_of_admin(machineID,connection):
        
    query = """
        SELECT A.UCINetID, U.Firstname, U.Middlename, U.Lastname, GROUP_CONCAT(UE.Email, ';') AS EmailList
        FROM Administrators A
        INNER JOIN Users U ON A.UCINetID = U.UCINetID
        INNER JOIN UserEmail UE ON A.UCINetID = UE.UCINetID
        INNER JOIN AdministratorManageMachines AMM ON A.UCINetID = AMM.AdministratorUCINetID
        WHERE AMM.MachineID = {}
        GROUP BY A.UCINetID, U.Firstname, U.Middlename, U.Lastname
        ORDER BY A.UCINetID ASC;
    """.format(machineID)

    cursor = connection.cursor()



    elif args[1] ==  "updateCourse_in_batch":
        rows = get_table_contents(args[2], connection)
        for row in rows:
            try:
                update_Course(row[0], args[3], connection)
                print("update " + str(row[0]) + " Success")
            except Exception as e:
                print("update " + str(row[0]) + " Fail")
                print(f"Fail: {str(e)}")





python3 project.py deleteStudent testID
// kept on getting success.
// should this be the behavior. I mean i am delete nothin because the testID does not exist in table.



convert all
        except Exception as e:
            print(f"Fail: {str(e)}")
to 
        except:
            print("Fail")



def drop_table(connection):
# input standard sql DROP TABLE commands into connection.cursor().execute()
    create_table_query = "DROP TABLE administratormanagemachines"     
    connect = connection.cursor()
    connect.execute(create_table_query) 
    connection.commit()
// hu: feel like would be better if we do 'DROP TABLE IF EXISTS tableName';





# Hu: optimal to run mysql commands directly in mysql
# mysql -u root -p
# # type password
# USE cs122a;
# SELECT * FROM employees;
# # note commands won't execute without ';'
# EXIT;



all tables
Users (UCINetID, Firstname, Middlename, Lastname)
UserEmail (UCINetID, Email)
Students (UCINetID)
Administrators (UCINetID)
Courses (CourseID, Title, Quarter)
Projects (ProjectID, Name, Description, CourseID)
Machines (MachineID, Hostname, IPAddress, OperationalStatus, Location)
StudentUseMachinesInProject (ProjectID ,StudentUCINetID ,MachineID ,StartDate ,EndDate)
AdministratorManageMachines (AdministratorUCINetID, MachineID)

Hu: run
    python3 project.py getTableContent Projects
    python3 project.py getTableContent Students
    python3 project.py getTableContent Machines
to see avaiable IDs.
python3 project.py getTableContent StudentUseMachinesInProject



    create_table_query =" CREATE TABLE StudentUseMachinesInProject( ProjectID INT,StudentUCINetID VARCHAR(20), MachineID INT, StartDate DATE, EndDate DATE, PRIMARY KEY (ProjectID, StudentUCINetID, MachineID), FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID), FOREIGN KEY (StudentUCINetID) REFERENCES Students(UCINetID) ON DELETE CASCADE, FOREIGN KEY (MachineID) REFERENCES Machines(MachineID) ON DELETE CASCADE );"
    connect = connection.cursor()
    connect.execute(create_table_query)
    connection.commit()

Fail: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`cs122a`.`studentusemachinesinproject`, CONSTRAINT `studentusemachinesinproject_ibfk_1` FOREIGN KEY (`ProjectID`) REFERENCES `projects` (`ProjectID`))




    create_table_query =" CREATE TABLE StudentUseMachinesInProject( ProjectID INT,StudentUCINetID VARCHAR(20), MachineID INT, StartDate DATE, EndDate DATE, PRIMARY KEY (ProjectID, StudentUCINetID, MachineID), FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID), FOREIGN KEY (StudentUCINetID) REFERENCES Students(UCINetID) ON DELETE CASCADE, FOREIGN KEY (MachineID) REFERENCES Machines(MachineID) ON DELETE CASCADE );"

    create_table_query = "CREATE TABLE AdministratorManageMachines( AdministratorUCINetID VARCHAR(20), MachineID INT, PRIMARY KEY (AdministratorUCINetID, MachineID), FOREIGN KEY (AdministratorUCINetID) REFERENCES Administrators(UCINetID) ON DELETE CASCADE, FOREIGN KEY (MachineID) REFERENCES Machines(MachineID) ON DELETE CASCADE );"
    // do not know if ON DELETE CASADE is necessary. I mean it's not specificed