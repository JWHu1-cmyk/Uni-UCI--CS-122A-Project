
# Hu: chmod +x myscript.sh && ./myscript.sh
# Hu: optimal to run mysql commands directly in mysql
# mysql -u root -p
# # type password
# USE cs122a;
# SELECT * FROM employees;
# # note commands won't execute without ';'
# EXIT;

python3 project.py import test_data
python3 project.py insertStudent testID test@uci.edu Alice NULL Wong