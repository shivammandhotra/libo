import psycopg2
from psycopg2 import sql

def connect_to_postgres(dbname, user, password, host='localhost', port=5432):
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("PostgreSQL connection closed")

# Example usage
if __name__ == "__main__":
    conn = connect_to_postgres('your_dbname', 'your_user', 'your_password')
    # Perform database operations
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                SELECT a.column_name
                FROM table_a a
                LEFT JOIN table_b b ON a.column_name = b.column_name
                WHERE b.column_name IS NULL
            """
            cursor.execute(query)
            result = cursor.fetchall()
            values_in_a_not_in_b = [row[0] for row in result]
            print("Values in table_a but not in table_b:", values_in_a_not_in_b)
            cursor.close()
        except Exception as e:
            print(f"Error: {e}")
    close_connection(conn)