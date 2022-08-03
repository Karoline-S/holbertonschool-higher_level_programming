#!/usr/bin/python3

"""Module for interacting with mysql database with"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")

    cur = conn.cursor()
    state_name = sys.argv[4]

    cur.execute("SELECT name FROM cities \
    WHERE state_id = ( \
    SELECT id FROM states WHERE name = %s) \
    ORDER BY id", {state_name})
    query_rows = cur.fetchall()
    print(', '.join(row[0] for row in query_rows))
    cur.close()
    conn.close()
