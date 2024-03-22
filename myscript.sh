


# Hu: chmod +x myscript.sh && ./myscript.sh




python3 project.py import test_data
python3 -c "print()"

python3 project.py insertStudent testID test@uci.edu Alice NULL Wong
python3 -c "print()"

# Hu: run 'python3 project.py insertStudent testID test@uci.edu Alice NULL Wong' the second time should result in fail
# Hu: run 
#     'python3 project.py getTableContent Students' 
#     'python3 project.py getTableContent Users'
#     'python3 project.py getTableContent UserEmail'
# to verify

python3 project.py addEmail testID test@gmail.com
python3 -c "print()"

# Hu: run 'python3 project.py addEmail testID test@gmail.com' the second time should result in fail
# Hu: run 'python3 project.py getTableContent UserEmail' to verify

# python3 project.py deleteStudent testID 
# HuL you rerun delet command, 'Success' still would be outputted
# Hu: run 'python3 project.py getTableContent Students' to verify
# Hu: run 'python3 project.py getTableContent Users' to verify

# python3 project.py deleteStudent_in_batch Students
# python3 -c "print()"

# Hu: run 'python3 project.py getTableContent Students' to verify
# Hu: run 'python3 project.py getTableContent Users' to verify

python3 project.py insertMachine 102 test.com 192.168.10.5 Active “DBH 1011”
python3 -c "print()"

# Hu: run 'python3 project.py insertMachine 102 test.com 192.168.10.5 Active “DBH 1011”' the second time should result in fail
# Hu: run 'python3 project.py getTableContent machines' to verify

# python3 project.py insertStudent testID test@uci.edu Alice NULL Wong
# python3 project.py insertUse 1 testID 102 2023-01-09 2023-03-10
# Hu: run 'python3 project.py insertUse 1 testID 102 2023-01-09 2023-03-10' the second time should result in fail
# python3 project.py insertUse 2005 testID 102 2023-01-09 2023-03-10
# Hu: should result in "fail", ProjectID{2005} does not exist
# Hu: run
#     python3 project.py getTableContent Projects
#     python3 project.py getTableContent Students
#     python3 project.py getTableContent Machines
# to see avaiable IDs.

python3 project.py updateCourse 1 "Intro to db managment"
python3 -c "print()"

# Hu: when I re run the command it still should still output "success"
python3 project.py updateCourse 1287 "Intro to db managment"
python3 -c "print()"

# Hu: should result in "fail", CourseID{1287} does not exist
# Hu: run
#     python3 project.py getTableContent Courses
# to see avaiable IDs.
# Hu: run "python3 project.py getTableContent Courses" tro see if the course title is updated.

python3 project.py updateCourse_in_batch Courses "Intro to db managment"
python3 -c "print()"

# Hu: run "python3 project.py getTableContent Courses" tro see if the course title is updated.
 
python3 project.py listCourse testID
python3 -c "print()"

# Hu: run "python3 project.py getTableContent StudentUseMachinesInProject" to see available [UCINetID:int];
# Hu: run 
#     python3 project.py getTableContent Courses
#     python3 project.py getTableContent Projects
#     python3 project.py getTableContent StudentUseMachinesInProject
# to see how tables JOIN

python3 project.py listCourse_in_batch StudentUseMachinesInProject
python3 -c "print()"

# Hu: run to see overall analytics
 
python3 project.py popularCourse 10
python3 -c "print()"

# Hu: verify via python3 project.py getTableContent Courses

python3 project.py getTableContent Machines
python3 -c "print()"

python3 project.py adminEmails 102
# Hu: funct 10, should return nothing as 102 is not a MachineID;
python3 project.py adminEmails_in_batch AdministratorManageMachines
# Hu: funct 10
# Hu: verify with 'python3 project.py getTableContent AdministratorManageMachines'



python3 project.py getTableContentFunct11 StudentUseMachinesInProject
# Hu: funct 11
# generate custome query base on the output
# StudentUseMachinesInProject (ProjectID ,StudentUCINetID ,MachineID ,StartDate ,EndDate)
# python3 project.py activeStudent [machineId: int] [N:int] [start:date] [end:date]
python3 project.py activeStudent 1 2 2020-01-01 2020-12-01
python3 project.py activeStudent 2 2 2020-01-01 2020-12-01
python3 project.py activeStudent 3 2 2020-01-01 2020-12-01
python3 project.py activeStudent 4 2 2020-01-01 2020-12-01
python3 project.py activeStudent 6 2 2020-01-01 2020-12-01
python3 project.py activeStudent 6 1 2020-06-01 2020-06-20
python3 project.py activeStudent 6 1 2020-07-01 2020-07-20
# Hu: difficult to systemize the tests.