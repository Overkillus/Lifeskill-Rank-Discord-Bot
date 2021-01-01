import sqlite3
from sqlite3 import Error
 
def initialise_database():
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        
        # Creates a table with all servers if not exists (1st time only)
        sql_create_server_table = """ CREATE TABLE IF NOT EXISTS servers (
                                id integer PRIMARY KEY,
                                server_name text NOT NULL UNIQUE
                            ); """
        cursor.execute(sql_create_server_table)
        connection.commit()

        # Creates a table with all players if not exists (1st time only) 
        sql_create_player_table = """ CREATE TABLE IF NOT EXISTS players (
                                id integer PRIMARY KEY,
                                server_id integer NOT NULL,
                                nick text NOT NULL,
                                lifeskill_json text NOT NULL,
                                date text NOT NULL
                            ); """
        cursor.execute(sql_create_player_table)

    connection.close()
 
 # Attempts connection with database
def establish_connection():
    for i in range(50):
        connection = None
        try:
            connection = sqlite3.connect('bdo_database.db')
            break
        except Error as e:
            print(e)
    return connection
 
 # Inserts single player entry in json format (with message date)
def insert_entry(server_id, nick, lifeskill_json, date):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_insert_entry = """INSERT INTO players (server_id, nick, lifeskill_json, date) VALUES (?,?,?,?)"""
        data_tuple = (server_id, nick, lifeskill_json, date)
        cursor.execute(sql_insert_entry, data_tuple)
        connection.commit()
    connection.close()
 
 # Inserts server into server table
def insert_server(server_name):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_insert_entry = """INSERT INTO servers (server_name) VALUES (?)"""
        data_tuple = (server_name,)
        cursor.execute(sql_insert_entry, data_tuple)
        connection.commit()
    connection.close()
 
 
 # Retrieve server id if name is known
def get_server_id(server_name):
    result = None
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        query = """SELECT id FROM servers WHERE server_name=?"""
        data_tuple = (server_name, )
        cursor.execute(query, data_tuple)
        result = cursor.fetchone()
        print(result)
        if result != None:
            result = result[0]
    connection.close()

    # no connection and no result to be handled
    return result

# Retrieve all player and server entries
def get_all_player_entries():
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        # player part
        query = """SELECT * FROM players"""
        cursor.execute(query)
        player_result = cursor.fetchall()
        print(player_result)
        
        # server part
        query = """SELECT * FROM servers"""
        cursor.execute(query)
        server_result = cursor.fetchall()
        print(server_result)
    
    connection.close()
    return player_result

def get_newest_unique_player_entries():
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        sql_get_newest = """SELECT mt.*     
                            FROM players mt INNER JOIN
                                (
                                    SELECT nick, MAX(date) AS MaxDate
                                    FROM players
                                    GROUP BY nick
                                ) t ON mt.nick = t.nick AND mt.date = t.MaxDate"""
        cursor.execute(sql_get_newest)
        result = cursor.fetchall()
    connection.close()
    return result 

def get_local_newest_unique_player_entries(server_id):
    connection = establish_connection()
    with connection:
        cursor = connection.cursor()
        query = """SELECT mt.*     
                            FROM players mt INNER JOIN
                                (
                                    SELECT nick, MAX(date) AS MaxDate
                                    FROM players
                                    GROUP BY nick
                                ) t ON mt.nick = t.nick AND mt.date = t.MaxDate WHERE server_id=?"""
        data_tuple = (server_id, )
        cursor.execute(query, data_tuple)
        result = cursor.fetchall()
    connection.close()
    return result 
