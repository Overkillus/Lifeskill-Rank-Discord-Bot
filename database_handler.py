import sqlite3

def initialise_database:
    sql_create_table = "CREATE TABLE IF NOT EXISTS lifeskills"

def insert_entry(nick, time, data_json):
    connection = sqlite3.connect('bdo_database.db')
    cursor = connection.cursor