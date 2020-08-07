#!/usr/bin/env python3
"""Prints the data found in the states table"""
from sys import argv
import MySQLdb

#  ----------------   TASK ---------------
# Write a script that takes in an argument and displays all
# values in the states table of hbtn_0e_0_usa where
# name matches the argument.
#
# Your script should take 4 arguments: mysql username,
#       mysql password, database name and state name searched
#       (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running
#       on localhost at port 3306
# You must use format to create the SQL query with the user input
# Results must be sorted in ascending order by states.id
# Results must be displayed as they are in the example below
# Your code should not be executed when imported

# ----------------- MASTER PLAN -------------------
# Pull in the valus from argv
# Our python script is going to be executed with args in this format
#                       ./0-select_states.py root root hbtn_0e_0_usa

# With the arguments finally in, now's the time to give the args to
# the MYSQL.connect module
# -   USAGE: db = MySQLdb.connect(host=MY_HOST,
#                                 user=MY_USER, passwd=MY_PASS, db=MY_DB)
# -   Then, execute the ||| cur = db.cursor() ||| module
# -   Then, enter your SQL commands in the exec module:
# -                 cur.execute("SQL QUERY")
# -                 rows = cur.fetchall() - This command pulls all the data
# -                 and then we would print out the details with a for loop
# -   Close the connections on the cursor, followed by the database

if __name__ == "__main__":
    # Rename and set the varibles for readability
    user, passwd, database = argv[1], argv[2], argv[3]

    # Plug in the values
    db = MySQLdb.connect('localhost', user, passwd, database)

    # Create a cursor to navigate the database
    lookup = db.cursor()

    # Use the cursor to execute the command
    lookup.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # Fetch all the data
    ma_dayta = lookup.fetchall()

    # Print out the data fetched
    name = 1
    for states in ma_dayta:
        if states[name][0] == 'N':
            print(states)

    # Cleanup
    lookup.close()
    db.close()
