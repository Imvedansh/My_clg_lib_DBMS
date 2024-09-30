import mysql.connector

# Database connection configuration
config = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': 'your_mysql_host',
    'database': 'your_database_name'
}

def create_students_table():
    """Creates the 'students' table if it doesn't exist."""
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                date_of_birth DATE,
                major VARCHAR(255)
            )
        """
        cursor.execute(create_table_query)
        cnx.commit()
        print("Students table created successfully.")

    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

def insert_student(first_name, last_name, date_of_birth, major):
    """Inserts a new student record into the 'students' table."""
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        insert_query = """
            INSERT INTO students (first_name, last_name, date_of_birth, major)
            VALUES (%s, %s, %s, %s)
        """
        data = (first_name, last_name, date_of_birth, major)
        cursor.execute(insert_query, data)
        cnx.commit()
        print("Student record inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

def get_all_students():
    """Retrieves and prints all student records from the 'students' table."""
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        students = cursor.fetchall()

        for student in students:
            print(student)

    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

if __name__ == "__main__":
    create_students_table()

    # Example usage:
    insert_student("Alice", "Smith", "2002-07-15", "Computer Science")
    insert_student("Bob", "Johnson", "2001-03-22", "Engineering")

    get_all_students()