from typing import List, Dict
from flask import Flask
import json
import pymysql
app = Flask(__name__)



def initialDB():
    # Open database connection
    db = pymysql.connect("db","myuser","mypaswd","db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM favorite_colors")

    # Fetch a single row using fetchone() method.
    # data = cursor.fetchone()
    data = [{nn: color} for (nn, color) in cursor]
    print ("Database version : \{0} ".format(data))

    # disconnect from server
    cursor.close()
    db.close()
    return data


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': initialDB()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')