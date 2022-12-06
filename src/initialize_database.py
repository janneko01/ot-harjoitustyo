from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists sheets;
    """)
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table sheets (
            game_name text,
            id integer,
            num1 INT,  num2 INT,  num3 INT,  num4 INT,  num5 INT,
            num6 INT,  num7 INT,  num8 INT,  num9 INT,  num10 INT,
            num11 INT, num12 INT, num13 INT, num14 INT, num15 INT,
            num16 INT, num17 INT, num18 INT, num19 INT, num20 INT,
            num21 INT, num22 INT, num23 INT, num24 INT, num25 INT
        );
    """)
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
