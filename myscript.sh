


# Hu: chmod +x myscript.sh && ./myscript.sh




python3 project.py import test_data

python3 project.py insertStudent testID test@uci.edu Alice NULL Wong
# Hu: run 'python3 project.py insertStudent testID test@uci.edu Alice NULL Wong' the second time should result in fail
# Hu: run 
#     'python3 project.py getTableContent Students' 
#     'python3 project.py getTableContent Users'
#     'python3 project.py getTableContent UserEmail'
# to verify

python3 project.py addEmail testID test@gmail.com
# Hu: run 'python3 project.py addEmail testID test@gmail.com' the second time should result in fail
# Hu: run 'python3 project.py getTableContent UserEmail' to verify

python3 project.py deleteStudent testID 
# Hu: run 'python3 project.py getTableContent Students' to verify
# Hu: run 'python3 project.py getTableContent Users' to verify

python3 project.py deleteStudent_in_batch Students
# Hu: run 'python3 project.py getTableContent Students' to verify
# Hu: run 'python3 project.py getTableContent Users' to verify

python3 project.py insertMachine 102 test.com 192.168.10.5 Active “DBH 1011”
# Hu: run 'python3 project.py insertMachine 102 test.com 192.168.10.5 Active “DBH 1011”' the second time should result in fail
# Hu: run 'python3 project.py getTableContent machines' to verify

python3 project.py insertStudent testID test@uci.edu Alice NULL Wong
python3 project.py insertUse 1 testID 102 2023-01-09 2023-03-10
# Hu: run 'python3 project.py insertUse 1 testID 102 2023-01-09 2023-03-10' the second time should result in fail
python3 project.py insertUse 2005 testID 102 2023-01-09 2023-03-10
# Hu: should result in "fail", ProjectID{2005} does not exist
# Hu: run
#     python3 project.py getTableContent Projects
#     python3 project.py getTableContent Students
#     python3 project.py getTableContent Machines
# to see avaiable IDs.

python3 project.py updateCourse 1 "Intro to db managment"
# Hu: when I re run the command it still should still output "success"
python3 project.py updateCourse 1287 "Intro to db managment"
# Hu: should result in "fail", CourseID{1287} does not exist
# Hu: run
#     python3 project.py getTableContent Courses
# to see avaiable IDs.
# Hu: run "python3 project.py getTableContent Courses" tro see if the course title is updated.

python3 project.py updateCourse_in_batch Courses "Intro to db managment"
# Hu: run "python3 project.py getTableContent Courses" tro see if the course title is updated.
 
python3 project.py listCourse testID
# Hu: run "python3 project.py getTableContent StudentUseMachinesInProject" to see available [UCINetID:int];
# Hu: run 
#     python3 project.py getTableContent Courses
#     python3 project.py getTableContent Projects
#     python3 project.py getTableContent StudentUseMachinesInProject
# to see how tables JOIN

python3 project.py listCourse_in_batch StudentUseMachinesInProject
# Hu: run to see overall analytics
 
python3 project.py popularCourse 10
# Hu: verify via python3 project.py getTableContent Courses


python3 project.py getTableContent Machines