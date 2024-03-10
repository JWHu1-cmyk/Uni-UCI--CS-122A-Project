import sys
import mysql.connector



#use YYYY-MM-DD

def connect_to_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zippy",
         
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)



def import_data(folderName:str, connection):
    try:
        connect = connection.cursor()
        connect.execute("SHOW TABLES")
        tables = connect.fetchall()

        for i in tables:
            command = f"DROP TABLE {i[0]}"
            connect.execute(command)
            print(f"Dropped: {i[0]}")
    except:
        print("NO Tables to drop")


    pass




if __name__ == "__main__":

    args = sys.argv

    connection = connect_to_database()




    print(args)

    if args[1] == "import":
        import_data(folderName=args[2],connection=connection)
        

