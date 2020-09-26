import sqlite3
from sqlite3 import Error
 
def initialise_database(server_name):
   
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_create_server_table = """ CREATE TABLE IF NOT EXISTS servers (
                                id integer PRIMARY KEY,
                                server_name text NOT NULL UNIQUE,
                            ); """
        insert_server
        server_id = get_server_id(server_name)
 
        sql_create_table = """ CREATE TABLE IF NOT EXISTS """ + server_id + """_players (
                                id integer PRIMARY KEY,
                                nick text NOT NULL,
                                lifeskill_json text NOT NULL,
                                date text NOT NULL
                            ); """
        cursor.execute(sql_create_table)
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
        sql_insert_entry = """INSERT INTO """ + server_id + """_players (nick, lifeskill_json, date) VALUES (?,?,?)"""
        data_tuple = (nick, lifeskill_json, date)
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

