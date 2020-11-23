import sqlite3
from sqlite3 import Error
 
def initialise_database(server_name):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        
        # Creates a table with all servers if not exists (1st time only)
        sql_create_server_table = """ CREATE TABLE IF NOT EXISTS servers (
                                id integer PRIMARY KEY,
                                server_name text NOT NULL UNIQUE,
                            ); """
        cursor.execute(sql_create_server_table)

        # Creates a table with all players if not exists (1st time only) 
        sql_create_player_table = """ CREATE TABLE IF NOT EXISTS players (
                                id integer PRIMARY KEY,
                                server_id integer NOT NULL,
                                nick text NOT NULL,
                                lifeskill_json text NOT NULL,
                                date text NOT NULL,
                            ); """
        cursor.execute(sql_create_player_table)

        # Checks if server in table, otherwise adds to table
        server_id = get_server_id(server_name)
        if server_id == None: 
            insert_server(server_name)

        connection.close()
 
def establish_connection():
    for i in range(50):
        connection = None
        try:
            connection = sqlite3.connect('bdo_database.db')
            break
        except Error as e:
            print(e)
    return connection
 
 
def insert_entry(server_id, nick, lifeskill_json, date):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_insert_entry = """INSERT INTO players (server_id, nick, lifeskill_json, date) VALUES (?,?,?)"""
        data_tuple = (server_id, nick, lifeskill_json, date)
        cursor.execute(sql_insert_entry, data_tuple)
        connection.commit()
        connection.close()
 
def insert_server(server_name):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_insert_entry = """INSERT INTO servers (server_name) VALUES (?)"""
        data_tuple = (server_name)
        cursor.execute(sql_insert_entry, data_tuple)
        connection.commit()
        connection.close()
 
 
 
def get_server_id(server_name):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        query = "SELECT id FROM servers WHERE server_name=?"
        data_tuple = (server_name)
        cursor.execute(query, data_tuple)
        result = cursor.fetchone()
        print(result)
        return result
    return None

